.PHONY: all
all: libmessage.a

objects = message.o

libmessage.a: $(objects)
	ar -crv libmessage.a $(objects)

$(objects): %.o: %.cc
	g++ -c $< -o $@


.PHONY: clean
clean:
	rm -f $(objects)
	rm -f libmessage.a
