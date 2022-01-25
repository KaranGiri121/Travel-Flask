from flask import Flask,render_template,request,redirect,url_for,session,g,abort
import json,datetime
from ast import literal_eval as to_list
import sqlite3 as sql


nepaltour=["Dhangadi","Nepalgunj","Butwal"]


class User:
    def __init__(self,id,username,password):
        self.id=id
        self.username=username
        self.password=password
    



users=[]
users.append(User(id=1,username='karan',password='karan@121'))



app= Flask(__name__)
app.secret_key="karangiri121@gmail.com"

@app.before_request
def before_request():
    g.user=None
    if "user_id" in session:
        user=[x for x in users if x.id==session['user_id']][0]
        g.user=user


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checking',methods=["POST","GET"])
def checking():
    if request.method == 'POST':
        result=request.form
        Date=result["Date"]
        From=result["From"]
        To=result["To"]
    else:
        From="Maharashtra"
        To="Dhangadi"
        Now=datetime.datetime.now()
        Date=Now.strftime("%Y-%m-%d")

    result={}
    result["Date"]=Date
    result["From"]=From
    result["To"]=To
    con=sql.connect("database.db")
    con.row_factory=sql.Row

    cur=con.cursor()
    if To in nepaltour:
        Place=To
    else:
        Place=f"{From}{To}"

    cur.execute(f"SELECT Lower,Upper FROM {Place} WHERE Date='{Date}'")
    x=cur.fetchone()
    if x==[] or x==None:
        print("Helloworld")
        print(result["From"])
        print(result["To"])
        return render_template("booking.html",result=result)
    else:
        result['Lower']=to_list(x["Lower"])
        result["Upper"]=to_list(x["Upper"])
        result["Date"]=[Date]
        result["From"]=[From]
        result["To"]=[To]
        result=json.dumps(result)

    return render_template('booking.html',result=result)


@app.route("/booking",methods=['POST'])
def booking():
    if(request.method=="POST"):
        data=request.form
        Date=data["Date"]
        From=data["From"]
        To=data["To"]
        Berth=data["Berth"]
        Side=data["Side"]
        SeatNo=data["SeatNo"]

    con=sql.connect("database.db")
    con.row_factory=sql.Row

    cur=con.cursor()

    if From in nepaltour:
        Place=f"{From}{To}"
    else:
        Place=To
    info=cur.execute(f"SELECT * FROM {Place} WHERE Date='{Date}'").fetchall()
    if info==[]:
        if Berth=='Lower':
            Lower="['"+Side+SeatNo+"']"
            Upper="[]"
        else:
            Upper="['"+Side+"_"+SeatNo+"']"
            Lower="[]"
        cur.execute(f"INSERT INTO {Place} (Date,Lower,Upper) VALUES(?,?,?)",(Date,Lower,Upper))
    else:
        if Berth=='Lower':
            temp=cur.execute(f"SELECT Lower FROM {Place} WHERE Date='{Date}'").fetchone()
            Lower=to_list(temp[0])
            temp=f'{Side}{SeatNo}'
            Lower.append(temp)
            cur.execute(f'UPDATE {Place} SET Lower="{Lower}" WHERE Date="{Date}"')
        if Berth=='Upper':
            temp=cur.execute(f"SELECT Upper FROM {Place} WHERE Date='{Date}'").fetchone()
            Upper=to_list(temp[0])
            temp=f'{Side}_{SeatNo}'
            Upper.append(temp)
            cur.execute(f'UPDATE {Place} SET Upper="{Upper}" WHERE Date="{Date}"')

    con.commit()

    return redirect(url_for("adminpanal"))
    
@app.route("/admin")
def adminpanal():
    if not g.user:
        return redirect(url_for("login"))

    return render_template("admin.html")



@app.route("/login",methods=['GET','POST'])
def login():
    session.pop("user_id",None)
    if request.method=="POST":
        username=request.form["Username"]
        password=request.form["Password"]
        user=[x for x in users if x.username==username]
        if not user:
            return redirect(url_for("login"))
        user=user[0]
        if user.password==password:
            session["user_id"]=user.id
            return redirect(url_for("index"))
        return redirect(url_for("login"))

    return render_template("login.html")

if '__main__'==__name__:
    app.run(debug=True,host='0.0.0.0')