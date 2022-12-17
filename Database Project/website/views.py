from flask import Blueprint, render_template, request, flash
from flask_mysqldb import MySQL
from . import mysql


views = Blueprint("views", __name__)

@views.route('/index', methods = ["GET","POST"])
def index():
	if request.method == "POST":
		senderID = request.form['senderID']
		senderFname = request.form['senderFname']
		senderLname = request.form['senderLname']
		senderPhone = request.form['senderPhone']
		senderAddr = request.form['senderAddr']
		senderEmail = request.form['senderEmail']
		
		
		receiverFname = request.form['receiverFname']
		receiverLname = request.form['receiverLname']
		receiverPhone = request.form['receiverPhone']
		receiverAddr = request.form['receiverAddr']
		receiverEmail = request.form['receiverEmail']

		
		orderNum = request.form['orderNum']
		orderPay = request.form['orderPay']
		orderWeight = request.form['orderWeight']
		orderDate = request.form['orderDate']

		itemName = request.form['itemName']
		itemType = request.form['itemType']
				
		cursor = mysql.connection.cursor()	
		
		if request.form['insert'] == 'insert':
			try:
				cursor.execute("INSERT INTO customerinfo.Senders VALUES (%s,%s,%s,%s,%s,%s)",
					(senderID,senderFname,senderLname,senderPhone,senderAddr,senderEmail))
				
				cursor.execute("INSERT INTO customerinfo.Receivers(senderID,fname,lname,phone,addr,email) VALUES(%s,%s,%s,%s,%s,%s)", 
					(senderID,receiverFname,receiverLname,receiverPhone,receiverAddr,receiverEmail))
				
				cursor.execute("SELECT MAX(receiverID) FROM Receivers")
				receiverSID = cursor.fetchall()[0][0]
				cursor.execute("INSERT INTO customerinfo.Orders VALUES (%s,%s,%s,%s,%s,%s)",
					(senderID,receiverSID,orderNum,orderPay,orderWeight,orderDate))

				cursor.execute("INSERT INTO customerinfo.Items VALUES (%s,%s,%s)",
					(orderNum,itemName,itemType))
				mysql.connection.commit()
			except:
				return render_template("index.html")
		
		cursor.close()
	return render_template("index.html")

