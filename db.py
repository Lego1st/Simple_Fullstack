import MySQLdb

class Database:
    def __init__(self):
        """ 
            Create connection and start a cursor 
        """
        self.db = MySQLdb.connect("localhost","root","123456","testdb" )
        self.cursor = self.db.cursor()    

    def exe(self, sql):
        """
            MySQL command execution
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def insertUser(self, name, age):
        self.exe("insert into user(name,age) values ('{}', {})".format(name, age))     
        
    def deleteUser(self, age):
        self.exe("delete from user where age > '%d'" % (age))

    def getName(self):
        sql = "select * from user"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.db.close()