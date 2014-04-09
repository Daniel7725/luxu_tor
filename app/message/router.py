from packet import get_name
import codec
from receiver import TcpReceiver
from adapter import TornadoAdapter
import logging
log = logging.getLogger("router")
log.setLevel(logging.DEBUG)

class ProtoRouter(object):
	def __init__(self):
		self._functions = {}
		self._adapter = TornadoAdapter()

	def _register(self,msg_type,function):
		self._functions[get_name(msg_type)] = function

	def _get_function(self,message):
		return self._function.get(get_name(message))

	def connected(self,**options):
		def decorator(f):
			self._connection_cb = f
			return f
		return decorator

	def route(self,msg_type,**options):
		def decorator(f):
			self._register(msg_type,f,**options)
			return f
		return decorator

	def closed(self,**options):
		def decorator(f):
			self._closed_cb = f
			return f
		return decorator

	def run(self,port,debug=None):
		self.debug = debug
		self._adapter.set_connection_cb(slef._on_connection)
		self._adapter.set_message_cb(self._message_cb)
		self._adapter.set_close_cb(self._on_close)
		self._dadpter.run(port)

	def _on_connection(self,conn):
		log.debug("new connection")
		conn.set_context(TcpReceiver(lambda x:self._full_message(conn,x)))
		self._connection_cb(conn)

	def _full_message(self,conn,data):
		message = codec.parse(data)
		if message:
			fn = self._get_function(message)
			if fn:
				log.debug("get knowned meddage")
				fn(conn,message)
			else:
				log.debug("unknown message")

	def _message_cb(self,conn,data):
		receiver = conn.get_context()
		receiver.on_message(data)

	def _on_close(self,conn):
		self._close_cb(conn)

	def send(self,conn,message):
		data = self.make_packet(message)
		data = conn.get_context().pack(data)
		conn.send(data)
	
	def make_packet(self,message):
		return TcpReceiver.pack(codec.package(message))
