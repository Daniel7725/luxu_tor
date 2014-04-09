import struct

k_header_len = 4
k_min_msg_len = 2

class TcpReceiver(object):
	def __init__(self,msg_callback):
		self._buffer = ''
		self.msg_callback = msg_callback

	def on_message(self,data):
		self._buffer += data
		while len(self._buffer) >= k_header_len + k_min_msg_len:
			length = struct.unpack('>i',buffer(self._buffer,0,k_header_len))[0]
			if len(self._buffer) >= length + k_header_len:
				message = buffer(self._buffer,k_header_len,length)
				self.msg_callback(message)
				self._buffer = self._buffer[k_header_len+length:]
			else:
				break
	
	@staticmethod
	def pack(self,message):
		data = struct.pack('>i',len(message)) + message
		return data
