# import sqlite3
# class MetaSingleton(type): # 메타클래스 생성
#     _instances = {}
#     def __call__(cls, *args, **kwargs): # __call__을 통해 싱글톤 생성
#         if cls not in cls._instances:
#             cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
# class Database(metaclass=MetaSingleton): # MetaSingleton의 도움으로 싱글톤 역할(단 한 개의 database 클래스 객체만 생성된다.) 
#     connection = None
#     def connect(self):
#          if self.connection is None:
#             self.connection = sqlite3.connect("db.sqlite3") 
#             self.cursorobj = self.connection.cursor()
#          return self.cursorobj
# db1 = Database().connect() 
# db2 = Database().connect()
# print ("Database Objects DB1", db1) 
# print ("Database Objects DB2", db2)
class HealthCheck:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance
    def __init__(self): 
        self._servers = []
    def addServer(self): 
        self._servers.append("Server 1") 
        self._servers.append("Server 2") 
        self._servers.append("Server 3") 
        self._servers.append("Server 4")
    def changeServer(self): 
        self._servers.pop() 
        self._servers.append("Server 5")
hc1 = HealthCheck() 
hc2 = HealthCheck()
hc1.addServer()
print("Schedule health check for servers (1)..") 
for i in range(4):
    print("Checking ", hc1._servers[i])
hc2.changeServer()
print("Schedule health check for servers (2)..") 
for i in range(4):
    print("Checking ", hc2._servers[i])