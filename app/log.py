#coding:utf-8
import logging
import logging.config
import time

def main():
	logging.config.fileConfig("./config/logger.conf")
	logger = logging.getLogger("root")

	for i in xrange(30):
#		logger = logging.getLogger("root")
		logger.debug('This is debug message'+str(i))
		logger.info("This is info message"+str(i))
		logger.warning("This is warning message"+str(i))
		time.sleep(2)

if __name__ == '__main__':
	main()
