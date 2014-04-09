pb = login_pb2.py chat_pb2.py

all:$(pb)

$(pb): %_pb2.py: %.proto
	protoc --cpp_out=../client --python_out=. $<

.PHONY: clean
clean:
	rm -f *_pb2.py
	rm -f ../client/*.pb.*
	rm -f *.pyc
