from flask import Flask,render_template,url_for,request
from database import accountDataBase

app=Flask(__name__)
db=accountDataBase()

@app.route('/Search',methods=['GET','POST'])
def index():
    if request.method=='POST':
        if request.form['website']!='':
            password=db.password(request.form['website'])
            return render_template('index.html',accountInfo=password)

    return render_template('index.html')

@app.route('/Add',methods=['GET','POST'])
def accountAdd():
    if request.method=='POST':
        errcount=0
        sendhtml=[]
        if len(request.form["username"])<4:
            errcount+=1
            sendhtml.append('username is to short')
        if request.form["website"].find(".com")==-1:
            errcount+=1
            sendhtml.append("website doesn't look legal")
        if errcount!=0:
            return render_template('addAccount.html',sendhtml=sendhtml)
        else:
            db.insert(request.form["website"],request.form["username"],request.form["email"],request.form["password"])
            return render_template('sucess.html')
    return render_template('addAccount.html')
    
@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')



if __name__=="__main__":
    app.run(debug=True)
