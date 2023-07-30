from database import accountDataBase
lst=[]
nameList=['yabsera', 'James', 'Robert', 'John', 'Michael', 'David', 'William', 'Richard', 'Joseph', 'Thomas', 'Christopher', 'Charles', 'Daniel', 'Matthew', 'Anthony', 'Mark', 'Donald', 'Steven', 'Andrew', 'Paul']

for i in nameList:
    lst.append(len(i))


print(min(lst))

