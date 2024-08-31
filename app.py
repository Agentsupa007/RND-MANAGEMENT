from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__,template_folder='template')

DATABASE = 'RND.db'

con = sqlite3.connect('RND.db', check_same_thread=False)
c=con.cursor()

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/checkin',methods=['GET','POST'])
def checkin():
    if request.method =='POST':
        c_id=request.form["c_id"] 
        room_type = request.form['room']
        days=request.form['days']
        c_id="cid"+c_id
        q1="create table {}(AMENITIES varchar(50),PRICE integer)".format(c_id)
        q2="insert into {}(AMENITIES,PRICE) VALUES('ROOM BILL',0)".format(c_id)
        c.execute(q1)
        c.execute(q2)
        con.commit()

        if room_type=="1":
            q1="UPDATE {} SET PRICE=1500*{} WHERE AMENITIES='ROOM BILL'".format(c_id,days)
            c.execute(q1)
            con.commit()
        elif room_type=="2":
            q1="UPDATE {} SET PRICE=2000*{} WHERE AMENITIES='ROOM BILL'".format(c_id,days)
            c.execute(q1)
            con.commit()
        else:
            q1="UPDATE {} SET PRICE=2500*{} WHERE AMENITIES='ROOM BILL'".format(c_id,days)
            c.execute(q1)
            con.commit()
    return render_template("checkin.html")


@app.route('/checkout',methods=['GET','POST'])
def checkout():
    total="YOUR TOTAL IS : "
    if request.method =='POST':
        c_id=request.form["c_id"]
        c_id="cid"+c_id
        a=request.form["ans"]
        total=bill(c_id)
        if a=='y':
            q2="drop table {}".format(c_id)
            c.execute(q2)
            con.commit()
    
    return render_template("checkout.html",value=total)

@app.route('/laundry',methods=['GET','POST'])
def laundry():
    if request.method =='POST':
        c_id=request.form["c_id"]
        c_id="cid"+c_id
        q2="insert into {}(AMENITIES,PRICE) values('LAUNDRY BILL',0)".format(c_id)
        c.execute(q2)
        con.commit()
        cloth_type=request.form['cloth']
        if cloth_type=="1":
            q3="update {} set PRICE=PRICE+15 WHERE AMENITIES='LAUNDRY BILL'".format(c_id)
            c.execute(q3)
            con.commit()
        if cloth_type=="2":
            q3="update {} set PRICE=PRICE+25 WHERE AMENITIES='LAUNDRY BILL'".format(c_id)
            c.execute(q3)
            con.commit()
        if cloth_type=="3":
            q3="update {} set PRICE=PRICE+10 WHERE AMENITIES='LAUNDRY BILL'".format(c_id)
            c.execute(q3)
            con.commit()
    return render_template("laundry.html")

@app.route('/spa',methods=['GET','POST'])
def spa():
    if request.method =='POST':
        c_id=request.form["c_id"]
        c_id="cid"+c_id
        q2="insert into {}(AMENITIES,PRICE) values('SPA BILL',0)".format(c_id)
        c.execute(q2)
        con.commit()
        spa_type=request.form['spa']
        if spa_type=="1":
            q3="update {} set PRICE=PRICE+1500 WHERE AMENITIES='SPA BILL'".format(c_id)
            c.execute(q3)
            con.commit()
        if spa_type=="2":
            q3="update {} set PRICE=PRICE+1500 WHERE AMENITIES='SPA BILL'".format(c_id)
            c.execute(q3)
            con.commit()
        if spa_type=="3":
            q3="update {} set PRICE=PRICE+2500 WHERE AMENITIES='SPA BILL'".format(c_id)
            c.execute(q3)
            con.commit()
    return render_template("spa.html")

@app.route('/restaurant',methods=['GET','POST'])
def restaurant():
    if request.method =='POST':
        c_id=request.form["c_id"]
        c_id="cid"+c_id
        q3="insert into {}(AMENITIES,PRICE) VALUES('RESTAURANT BILL',0)".format(c_id)
        c.execute(q3)
        con.commit()
        order=request.form['restaurant']
        if order=="1":
            q2="UPDATE {} SET PRICE=PRICE+20 WHERE AMENITIES='RESTAURANT BILL'".format(c_id)
            c.execute(q2)
            con.commit()
        elif order=="2":
            q2="UPDATE {} SET PRICE=PRICE+30 WHERE AMENITIES='RESTAURANT BILL'".format(c_id)
            c.execute(q2)
            con.commit()
        elif order=="3":
            q2="UPDATE {} SET PRICE=PRICE+35 WHERE AMENITIES='RESTAURANT BILL'".format(c_id)
            c.execute(q2)
            con.commit()
        elif order=="4":
            q2="UPDATE {} SET PRICE=PRICE+30 WHERE AMENITIES='RESTAURANT BILL'".format(c_id)
            c.execute(q2)
            con.commit()
        elif order=="5":
            q2="UPDATE {} SET PRICE=PRICE+40 WHERE AMENITIES='RESTAURANT BILL'".format(c_id)
            c.execute(q2)
            con.commit()
        elif order=="6":
            q2="UPDATE {} SET PRICE=PRICE+60 WHERE AMENITIES='RESTAURANT BILL'".format(c_id)
            c.execute(q2)
            con.commit()
    return render_template("restaurant.html")

def bill(c_id):
    c_id=c_id
    q1="SELECT SUM(PRICE) FROM {}".format(c_id)
    c.execute(q1)
    data=c.fetchall()
    data=data[0][0]
    return(data)

if __name__=="__main__":
    app.run(debug=True)