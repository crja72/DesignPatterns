def Singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@Singleton
class DBConnection:
    def __init__(self, address=None, port=None, username=None, password=None):
        self.connection = self.connect(address, port, username, password)

    def connect(self, address, port, username, password):
        return 42

    def get_connection(self):
        return self.connection


a = DBConnection()
b = DBConnection()
print(a is b)
