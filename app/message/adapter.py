from connection import Connection
import logging
log = logging.getLogger("adapter")
log.setLevel(logging.DEBUG)

class Adapter(object):
	def __init__(self):
		self._connection_cb = self._def_conn_cb
		self._message_cb = self._def_msg_cb
		self._close_cb = self._def_close_cb

	def set_connection_cb(self,cb):
		self._connection_cb = cb

	def set_message_cb(self,cb):
		self._message_cb = cb

	def set_close_cb(self,cb):
		self._close_cb = cb

	def _def_conn_cb(self,conn):
		pass

	def _def_msg_cb(self,conn,data):
		pass

	def _def_close_cb(self,conn):
		pass

	def run(self,port):
		pass

from tornado.tcpserver import TCPServer
import tornado.ioloop
class TornadoAdapter(Adapter):

	class AdapterServer(TCPServer):
		def __init__(self,callbacks):
			self._connection_cb = callbacks["connect"]
			self._message_cb = callbacks["message"]
			self._close_cb = callbacks["close"]
			super(TornadoAdapter.AdapterServer,self).__init__()
		def handle_stream(self,stream,address):
			self._connection_cb(stream,address)
			stream.set_close_callback(self._close_cb)
			stream.read_until_close(None,streaming_callback = lambda x:self._message_cb(stream,x))
			stream.set_close_callback(lambda : self._close_cb(stream))

	def __init__(self):
		self.connection_map = {}
		super(TornadoAdapter,self).__init__()

	def on_connection(self,stream,data):
		conn = Connection(dict(
				send = stream.write,
				close = stream.close,
				is_closed = stream.closed))
		self.connection_map[stream] = conn
		log.debug("new connection")
		self._connection_cb(conn)
	
	def on_message(self,stream,data):
		self._message_cb(self.connection_map[stream],data)

	def on_close(self,stream):
		self._close_cb(self.connection_map[stream])
		self.connection_map.pop(stream)

	def run(self,port):
		server = TornadoAdapter.AdapterServer(dict(
				connect = self.on_connection,
				message = self.on_message,
				close = self.on_close))
		server.listen(port)
		tornado.ioloop.IOLoop.instance().start()
