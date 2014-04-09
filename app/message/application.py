#coding:utf-8
from router import ProtoRouter
from packet import login,chat

import logging
log = logging.getLoget("application")
log.setLevel(logging.DEBUG)

import os
import sys
import inspect
app_path = os.path.abspath(
		os.path.dirname(inspect.getfile(inspect.currentframe())))
app_path += "/.."
sys.path.append(app_path)

from models import UserModel,DeviceModel,TokenModel,MessageModel
from lib.redis_tools import RedisTools

class MessageServer(object):
	def __init__(self,application):
		self._app = application
		self._client_map = {}
		self._user_map = {}
		self._users = UserModel()
		self._devices = DeviceModel()
		self._tokens = TokenModel()
		self._messages = MessageModel()
		self._redis = RedisTools()

	def add_client(self,conn):
		self._client_map[conn] = {}

	def remove_client(self,conn):
		user_id = self._client_map.pop(conn)
		if user_id:
			self._user_map.pop(user_id)

	def register(self,conn,message):
	#TODO:add user to database
		device = {
					"device_type":message.device_type,
					"device_token":message.device_token,
					"device_uuid":message.device_uuid,
					"system_version":message.system_version
				}
		user_id,token = self._devices.new_device(device)
		#TODO:check device type
		rep = login.Response()
		rep.err = login.Response.SUCCESS
		rep.user_id = str(user_id)
		rep.user_token = token
		conn.send(app.make_packet(rep))

	def login(self,conn,message):
		user_id = message.user_id
		user_token = message.user_token
		chk_res = self._token.check_token(user_id,user_token)
		if chk_res:
			self._user_map[user_id] = conn
			self._client_map[conn]["user_id"] = user_id
		rep = login.Result()
		rep.err = login.Result.SUCCESS if chk_res else login.Result.TOKEN_NOT_AVAILABLE
		rep.token = "test_token"
		conn.send(app.make_packet(rep))

	def on_chat(self,conn,message):
		to_id = message.to_user
		u_msg_id = message.message_id
		content = message.content
		message_id = self._messages.new_message({
			"msg_id":u_msg_id,
			"from_user":self._client_map[conn]["user_id"],
			"to_user":to_id,
			"content":content
			})
		self._redis.send_message(message_id)
		#TODO:give client send success message
		#need add chat.Response proto

	def send_message(self,message_id):
		message = self._message.get_message(message_id)
		to_user = message["to_user"]
		conn = self._user_map[to_user]
		if not conn:
			#FIXME:if other server hold this user,shouldn't push
			self._redis.push_message(message)
			return
		packet = chat.Receive()
		packet.message_id = message["msg_id"]
		packet.from_user = message["from_user"]
		packet.content = message["content"]
		conn.send(app.make_packet(packet))


app = ProtoRouter()
server = MessageServer(app)

@app.connected()
def on_connection(conn):
	log.debug("new connection")
	server.add_client(conn)

@app.route(login.Register)
def on_register(conn,message):
	server.register(conn,message)

@app.route(login.Login)
def on_login(conn,message):
	server.login(conn,message)

@app.route(chat.Send)
def on_chat(conn,message):
	server.on_chat(conn,message)

@app.closed()
def on_close(conn):
	server.remove_client(conn)

if __name__ == "__main__":
	app.run(24842)
