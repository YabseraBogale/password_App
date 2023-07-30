import sqlite3
import random
class accountDataBase():
    def __init__(self) -> None:
        self.connect=sqlite3.connect('Account.db',check_same_thread=False)
        self.pointer=self.connect.cursor()
    def insert(self,website,username,email,password)-> str:
        self.data=(website,username,email,password)
        self.pointer.execute(
            "insert into Account(website,username,email,password) values(?,?,?,?)",
            self.data
        )
        self.connect.commit()
        return "Sucessful"
    def password(self,password):
        self.pointer.execute("select * from Account where website=(?)",(password,))
        self.data=self.pointer.fetchall()
        return self.data
    def seeAllInfo(self):
        self.pointer.execute("select * from Account;")
        self.data=self.pointer.fetchall()
        return self.data
    def randomName(self) -> str:
        self.nameList=['yabsera', 'James', 'Robert', 'John', 'Michael', 'David', 'William', 'Richard', 'Joseph', 'Thomas', 'Christopher', 'Charles', 'Daniel', 'Matthew', 'Anthony', 'Mark', 'Donald', 'Steven', 'Andrew', 'Paul']
        self.number=random.randint(2,3)
        if self.number==2:
            return self.nameList[random.randint(0,len(self.nameList)-1)] + self.nameList[random.randint(0,len(self.nameList)-1)]
        self.symbol=['_','@','$','!']
        return self.nameList[random.randint(0,len(self.nameList)-1)] + self.symbol[random.randint(0,len(self.symbol)-1)] + self.nameList[random.randint(0,len(self.nameList)-1)] + self.symbol[random.randint(0,len(self.symbol)-1)] + self.nameList[random.randint(0,len(self.nameList)-1)]
    def generatePassword(self,length=15):
        self.password=""
        while length>=0:
            self.password+=chr(random.randint(33,126))
            length-=1
        return self.password
