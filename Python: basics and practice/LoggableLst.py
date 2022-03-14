import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(Loggable, list):
    def append(self, elem):
        super(LoggableList, self).append(elem)
        return self.log(elem)
