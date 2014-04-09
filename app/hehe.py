import logging
import time
from logging.handlers import TimedRotatingFileHandler

def main():
    log = logging.getLogger()
    formatter = logging.Formatter("%(name)-12s %(asctime)s %(message)s")
    fileTimeHandler = TimedRotatingFileHandler("./log/me","S",1)

#    fileTimeHandler.suffix = "%Y%m%d_%H%M%S"
    fileTimeHandler.setFormatter(formatter)
    logging.basicConfig(level = logging.INFO)
    fileTimeHandler.setFormatter(formatter)
    log.addHandler(fileTimeHandler)

    for x in xrange(30):
#        log = logging.getLogger()
        log.error("aaaaaaaaa")
        log.info("vbbbbbbbbb")
        time.sleep(2)
	
	print "just for test pull request"
	print "the second time to test pull request"

if __name__ == '__main__':
    main()

