class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBConnection(metaclass=Singleton):

    def __init__(self, address=None, port=None, username=None, password=None):
        self.connection = self.connect(address, port, username, password)

    def connect(self, address, port, username, password):
        return 42

    def get_connection(self):
        return self.connection


a = DBConnection()
b = DBConnection()
print(a is b)
