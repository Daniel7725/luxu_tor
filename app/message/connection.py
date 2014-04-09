class Connection(object):
	def __init__(self,functions):
		self._send = functions["send"]
		self._close = functions["close"]
		self._is_closed = functions["is_closed"]

	def send(self,data,callback = None):
		return self._send(data,callback)

	def close(self):
		return self._close()

	def is_closed(self):
		return self._is_closed()

	def set_context(self,context):
		self._context = context

	def get_context(self):
		return self._context
