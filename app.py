from flask import Flask, abort, render_template, request, redirect, url_for, session, g
import json
import datetime
from ast import literal_eval as to_list
import sqlite3 as sql
import razorpay
from internal.Key import *
from internal import price

client = razorpay.Client(
    auth=(MID, MKEY))

nepaltour = ['Dhangadi', 'Nepalgunj', 'Butwal']



app = Flask(__name__)
app.secret_key=Secret_Key



@app.route("/")
def index():
    session.pop("id",None)
    session.pop("From",None)
    session.pop("To",None)
    session.pop("Date",None)
    session.pop("Payment",None)
    session.pop("Payment",None)
    return render_template("index.html")


# @app.route("/checking", methods=["POST", "GET"])
# def check():
#     if request.method == "POST":
#         result = request.form
#         From = result["From"]
#         To = result["To"]
#         Date = result["Date"]
#     else:
#         From = "Maharashtra"
#         To = "Dhangadi"
#         Now = datetime.datetime.now()
#         Date = Now.strftime("%Y-%m-%d")

#     Price = price.x[f'{From}To{To}']
#     result = {
#         'From': From,
#         'To': To,
#         'Date': Date,
#         'Price': Price
#     }
#     if To in nepaltour:
#         Place = To
#     else:
#         Place = f'{From}{To}'
#     conn = sql.connect("database.db")
#     conn.row_factory = sql.Row
#     cur = conn.cursor()
#     info = cur.execute(f"SELECT * FROM {Place} WHERE Date='{Date}'").fetchone()
#     if info == None or info == []:
#         result = json.dumps(result)
#         return render_template("booking.html", result=result)

#     result['Lower'] = info['Lower']
#     result['Upper'] = info['Upper']

#     result = json.dumps(result)
#     return render_template("booking.html", result=result)

    # TESTING
@app.route("/checking", methods=["POST", "GET"])
def check():
    if request.method=="GET" and 'id' not in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        result = request.form
        From = result["From"]
        To = result["To"]
        Date = result["Date"]
        session['id'] = 1
        session['From'] = From
        session["To"] = To
        session["Date"] = Date

    else:
        From = session["From"]
        To = session["To"]
        Date = session["Date"]

    Price = price.x[f'{From}To{To}']
    result = {
        'From': From,
        'To': To,
        'Date': Date,
        'Price': Price
    }
    if To in nepaltour:
        Place = To
    else:
        Place = f'{From}{To}'
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    info = cur.execute(f"SELECT * FROM {Place} WHERE Date='{Date}'").fetchone()
    if info == None or info == []:
        result = json.dumps(result)
        lower=list(range(0,30))
        upper=list(range(0,30))
        conn.execute(f"INSERT INTO {Place} (Date,Lower,Upper) VALUES(?,?,?)",(f'{Date}',f'{lower}',f'{upper}'))
        conn.commit()
        return render_template("booking.html", result=result)

    result['Lower'] = to_list(info['Lower'])
    result['Upper'] = to_list(info['Upper'])

    result = json.dumps(result)
    return render_template("booking.html", result=result)


# From = None
# To = None
# Result = {}


# @app.route("/detailform", methods=["POST", "GET"])
# def detailform():
#     global From, To, Result
#     if request.method == "POST" and request.args.get("action") != 'PaymentProcess':
#         From = request.form["From"]
#         To = request.form["To"]
#         Lseat = request.form["LSeat"]
#         Useat = request.form["USeat"]
#         Date = request.form["Date"]
#         print(From, To, Lseat, Useat, Date)
#         return render_template("detailform.html", result=Result)

#     # print(request.method)

#     if From == None and To == None:
#         return redirect(url_for("index"))

#     Info = {}
#     if request.args.get("action") == "PaymentProcess":
#         Price = price.x[f'{From}To{To}']*100
#         data = {"amount": Price, "currency": "INR",
#                 "receipt": "order_rcptid_11"}
#         payment = client.order.create(data=data)
#         Info["Name"] = request.form["Name"]
#         Info["Mobile"] = request.form["Mobile"]
#         Info["Email"] = request.form["Email"]
#     else:
#         print("Else InCounter")
#         print(From, To)
#         return render_template("detailform.html", result=Result)

#     Result["Data"] = payment
#     Result["Info"] = Info
#     return render_template("detailform.html", result=Result)


                                            #TESTING


Lseat=None
Useat=None
@app.route("/detailform", methods=["POST", "GET"])
def detailform():
    global Lseat,Useat
    Info={}
    result={}
    if "id" not in session:
        return redirect(url_for("index"))

    if request.method == "POST" and request.args.get("action") != 'PaymentProcess':
        try:
            Lseat = to_list(request.form["LSeat"])
            Useat = to_list(request.form["USeat"])
        except:
            return redirect(url_for("check"))
        
        session["Lseat"]=Lseat
        session["Useat"]=Useat

        # print(Lseat,Useat)
        # return render_template("detailform.html", result=Info)

    # print(request.method)

    if 'id' not in session:
        return redirect(url_for("index"))

    if Lseat==None or Useat==None or (Lseat==0 or Useat==0):
        return redirect(url_for("index"))

    if "Payment" not in session and request.args.get("action") == "PaymentProcess":
        Price = price.x[f'{session["From"]}To{session["To"]}']*100*(len(Lseat)+len(Useat))
        data = {"amount": Price, "currency": "INR",
                "receipt": "order_rcptid_11"}
        payment = client.order.create(data=data)
        #Make Some Variable To Show In DetailFrom HTML   
        # Result["Data"] = payment
        session["Payment"]=payment
        # print(payment)
        # # Result["Info"] = Info
        # return render_template("detailform.html", result=Result)
    # print(session["Payment"],session["id"])


    Info["From"] = session["From"]
    Info["Date"] = session["Date"]
    Info["To"] = session["To"]
    Price = price.x[f'{session["From"]}To{session["To"]}']
    Info["Price"] = Price
    Info["Seat"]= len(Lseat)+len(Useat)

    if 'Payment' in session:
        result["Data"]=session["Payment"]
        result["KEY"]=MID

    result["Info"]=Info
    return render_template("detailform.html", result=result)


@app.route("/success", methods=["POST","GET"])
def verifyPayment():
    param_dict={
        'razorpay_order_id':request.form["razorpay_order_id"],
        'razorpay_payment_id':request.form["razorpay_payment_id"],
        'razorpay_signature':request.form["razorpay_signature"]
    }
    try:
        client.utility.verify_payment_signature(param_dict)
        # print("Ok")
        conn=sql.connect("database.db")
        if session["To"] in nepaltour:
            Place=session["To"]
        else:
            Place=f'{session["To"]}{session["From"]}'
        Date=session["Date"]
        conn.row_factory=sql.Row
        cur=conn.cursor()
        info=cur.execute(f"SELECT Lower,Upper FROM {Place} WHERE Date='{Date}'").fetchone()
        Lower=to_list(info["Lower"])
        Upper=to_list(info["Upper"])

        for i in session["Lseat"]:
            Lower.pop(Lower.index(i))


        for i in session["Useat"]:
            Upper.pop(Upper.index(i))

        # conn.execute(f"INSERT INTO {Place} (Date,Lower,Upper) VALUES(?,?,?)",(f'{Date}',f'{Lower}',f'{Upper}'))
        conn.execute(f"UPDATE {Place} SET Lower='{Lower}',Upper='{Upper}' WHERE Date='{Date}'")
        conn.commit()
    except:
        return "Payment Not Success Full"

    return redirect(url_for("index"))

    


if "__main__" == __name__:
    app.run(debug=True)
