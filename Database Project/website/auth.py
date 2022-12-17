from flask import Blueprint, render_template, request, flash
from flask_mysqldb import MySQL
from . import mysql

auth = Blueprint("auth", __name__)

@auth.route('/update', methods = ["GET"])
def updatepage():
	return render_template("update.html")

@auth.route('/update', methods = ["POST"])
def update():
	boolean = True

	senderID = request.form['senderID']
	newSFname = request.form['newSFname']
	newSLname = request.form['newSLname']
	newSPhone = request.form['newSPhone']
	newSAddr = request.form['newSAddr']
	newSEmail = request.form['newSEmail']

	receiverID = request.form['receiverID']
	newRFname = request.form['newRFname']
	newRLname = request.form['newRLname']
	newRPhone = request.form['newRPhone']
	newRAddr = request.form['newRAddr']
	newREmail = request.form['newREmail']

	orderRID = request.form['orderRID']
	orderID = request.form['orderID']
	newPrice = request.form['newPrice']
	newWeight = request.form['newWeight']
	newDate = request.form['newDate']

	itemOID = request.form['itemOID']
	newItems = request.form['newItems']
	newType = request.form['newType']

	cursor = mysql.connection.cursor()

	customerInfo = ''
	receiversInfo = ''
	ordersInfo = ''
	itemsInfo = ''
	
	if request.form['update'] == 'update':
		try:
			cursor.execute("SELECT * FROM customerinfo.Senders WHERE senderID=%s",[senderID])
			datas = cursor.fetchall()[0]
			for data in datas:
				customerInfo += str(data) + ' || '
			
			cursor.execute("SELECT * FROM customerinfo.Receivers WHERE senderID=%s",[senderID])
			datas = cursor.fetchall()
			for item in datas:
				for data in item:
					receiversInfo += str(data) + ' || '
				receiversInfo += '<br>'

			cursor.execute("SELECT * FROM customerinfo.Orders WHERE senderID=%s",[senderID])
			datas = cursor.fetchall()
			for item in datas:
				for data in item:
					ordersInfo += str(data) + ' || '
				ordersInfo += '<br>'

			cursor.execute("""SELECT * FROM customerinfo.Items WHERE orderID = ANY
					(SELECT orderID FROM customerinfo.Orders WHERE senderID=%s)""",[senderID])
			datas = cursor.fetchall()
			for item in datas:
				for data in item:
					itemsInfo += str(data) + ' || '
				itemsInfo += '<br>'
			boolean = True
		except:	
			boolean = False
	
		
	if request.form['update'] == 'updateS':
		if senderID != '':
			if newSFname != '':
				cursor.execute("UPDATE customerinfo.Senders SET fname=%s WHERE senderID=%s",[newSFname,senderID])
			if newSLname != '':
				cursor.execute("UPDATE customerinfo.Senders SET lname=%s WHERE senderID=%s",[newSLname,senderID])
			if newSPhone != '':
				cursor.execute("UPDATE customerinfo.Senders SET phone=%s WHERE senderID=%s",[newSPhone,senderID])
			if newSAddr != '':
				cursor.execute("UPDATE customerinfo.Senders SET addr=%s WHERE senderID=%s",[newSAddr,senderID])
			if newSEmail != '':
				cursor.execute("UPDATE customerinfo.Senders SET email=%s WHERE senderID=%s",[newSEmail,senderID])
		
			
	if request.form['update'] == 'updateR':
		if newRFname != '':
			cursor.execute("UPDATE customerinfo.Receivers SET fname=%s WHERE receiverID=%s",[newRFname,receiverID])
		if newRLname != '':
			cursor.execute("UPDATE customerinfo.Receivers SET lname=%s WHERE receiverID=%s",[newRLname,receiverID])
		if newRPhone != '':
			cursor.execute("UPDATE customerinfo.Receivers SET phone=%s WHERE receiverID=%s",[newRPhone,receiverID])
		if newRAddr != '':
			cursor.execute("UPDATE customerinfo.Receivers SET addr=%s WHERE receiverID=%s",[newRAddr,receiverID])
		if newREmail != '':
			cursor.execute("UPDATE customerinfo.Receivers SET email=%s WHERE receiverID=%s",[newREmail,receiverID])
			

	if request.form['update'] == 'addR':
		cursor.execute("INSERT INTO Receivers(senderID,fname,lname,phone,addr,email) VALUES(%s,%s,%s,%s,%s,%s)",
			(senderID,newRFname,newRLname,newRPhone,newRAddr,newREmail))
	
	if request.form['update'] == 'updateO':
		if orderID != '':
			if newPrice != '':
				cursor.execute("UPDATE customerinfo.Orders SET price=%s WHERE orderID=%s", [newPrice,orderID])
			if newWeight != '':
				cursor.execute("UPDATE customerinfo.Orders SET weight=%s WHERE orderID=%s", [newWeight,orderID])
			if newDate != '':
				cursor.execute("UPDATE customerinfo.Orders SET dateOrder=%s WHERE orderID=%s", [newDate,orderID])

	if request.form['update'] == 'addO':
		if orderRID != '':
			cursor.execute("INSERT INTO customerinfo.Orders VALUES(%s,%s,%s,%s,%s,%s)",
				(senderID,orderRID,orderID,newPrice,newWeight,newDate))

	if request.form['update'] == 'updateI':
		if itemOID != '':
			if newItems != '':
				cursor.execute("UPDATE customerinfo.Items SET list=%s WHERE orderID=%s", [newItems,itemOID])
			if newType != '':
				cursor.execute("UPDATE customerinfo.Items SET type=%s WHERE orderID=%s", [newType,itemOID])
	
	if request.form['update'] == 'addI':
		if itemOID != '':
			cursor.execute("INSERT INTO customerinfo.Items VALUES(%s,%s,%s)",
				(itemOID,newItems,newType))

	mysql.connection.commit()
	cursor.close()
	return render_template("update.html", boolean=True, customer=customerInfo, receivers=receiversInfo, orders=ordersInfo, items=itemsInfo)


@auth.route('/search', methods = ["GET","POST"])
def search():
	if request.method == "POST":
		senderID = request.form['senderID']
		senderFname = request.form['senderFname']
		senderLname = request.form['senderLname']
		senderPhone = request.form['senderPhone']
		senderAddr = request.form['senderAddr']
		senderEmail = request.form['senderEmail']
		
		receiverSID = request.form['receiverSID']
		receiverID = request.form['receiverID']
		receiverFname = request.form['receiverFname']
		receiverLname = request.form['receiverLname']
		receiverPhone = request.form['receiverPhone']
		receiverAddr = request.form['receiverAddr']
		receiverEmail = request.form['receiverEmail']

		orderSID = request.form['orderSID']
		orderRID = request.form['orderRID']
		orderID = request.form['orderID']
		orderPay = request.form['orderPay']
		orderWeight = request.form['orderWeight']
		orderDate = request.form['orderDate']

		itemOID = request.form['itemOID']
		itemName = request.form['itemName']
		itemType = request.form['itemType']

		cursor = mysql.connection.cursor()

		customerInfo = ''
		
		if request.form['search'] == 'searchS':
			if senderID!='' or senderFname!='' or senderLname!='' or senderPhone!='' or senderAddr!='' or senderEmail!='':
				cursor.execute("SELECT * FROM customerinfo.Senders WHERE senderID=%s OR fname=%s OR lname=%s OR phone=%s OR addr=%s OR email=%s",
					[senderID,senderFname,senderLname,senderPhone,senderAddr,senderEmail])
				datas = cursor.fetchall()
				for item in datas:
					for data in item:
						customerInfo += str(data) + ' || '
					customerInfo += '<br>'
				return render_template("search.html",boolean=True,cus=True,customer=customerInfo)
			else:
				cus = True
				boolean = True
				cursor.execute("SELECT * FROM customerinfo.Senders")
				datas = cursor.fetchall()
				for item in datas:
					for data in item:
						customerInfo += str(data) + ' || '
					customerInfo += '<br>'
				return render_template("search.html",boolean=True,cus=True,customer=customerInfo)

		if request.form['search'] == 'searchR':
			if receiverSID!='' or receiverID!='' or receiverFname!='' or receiverLname!='' or receiverPhone!='' or receiverAddr!='' or receiverEmail!='':
				cursor.execute("SELECT * FROM customerinfo.Receivers WHERE senderID=%s OR receiverID=%s OR fname=%s OR lname=%s OR phone=%s OR addr=%s OR email=%s",
					[receiverSID,receiverID,receiverFname,receiverLname,receiverPhone,receiverAddr,receiverEmail])
				datas = cursor.fetchall()
				for item in datas:
					for data in item:
						customerInfo += str(data) + ' || '
					customerInfo += '<br>'
				return render_template("search.html",boolean=True,cus=True,customer=customerInfo)
			else:

				cursor.execute("SELECT * FROM customerinfo.Receivers")
				datas = cursor.fetchall()
				for item in datas:
					for data in item:
						customerInfo += str(data) + ' || '
					customerInfo += '<br>'
				return render_template("search.html",boolean=True,cus=True,customer=customerInfo)


		if request.form['search'] == 'searchO':
			if orderSID!='' or orderRID!='' or orderID!='' or orderPay!='' or orderWeight!='':
				if orderDate=='':
					cursor.execute("SELECT * FROM customerinfo.Orders WHERE senderID=%s OR receiverID=%s OR orderID=%s OR price=%s OR weight=%s",
						[orderSID,orderRID,orderID,orderPay,orderWeight])
				if orderDate!='':
					cursor.execute("SELECT * FROM customerinfo.Orders WHERE senderID=%s OR receiverID=%s OR orderID=%s OR price=%s OR weight=%s OR dateOrder=%s",
						[orderSID,orderRID,orderID,orderPay,orderWeight,orderDate])
				datas = cursor.fetchall()
				for item in datas:
					for data in item:
						customerInfo += str(data) + ' || '
					customerInfo += '<br>'
				return render_template("search.html",boolean=True,cus=True,customer=customerInfo)
			else:
				cursor.execute("SELECT * FROM customerinfo.Receivers")
				datas = cursor.fetchall()
				for item in datas:
					for data in item:
						customerInfo += str(data) + ' || '
					customerInfo += '<br>'
				return render_template("search.html",boolean=True,cus=True,customer=customerInfo)

		if request.form['search'] == 'searchI':
			if itemOID!='' or itemName!='' or itemType!='':
				cursor.execute("SELECT * FROM customerinfo.Items WHERE orderID=%s OR list=%s OR type=%s",
						[itemOID,itemName,itemType])
				datas = cursor.fetchall()
				for item in datas:
					for data in item:
						customerInfo += str(data) + ' || '
					customerInfo += '<br>'
				return render_template("search.html",boolean=True,cus=True,customer=customerInfo)
			else:
				cursor.execute("SELECT * FROM customerinfo.Items")
				datas = cursor.fetchall()
				for item in datas:
					for data in item:
						customerInfo += str(data) + ' || '
					customerInfo += '<br>'
				return render_template("search.html",boolean=True,cus=True,customer=customerInfo)

	return render_template("search.html")



@auth.route('/delete', methods = ["GET","POST"])
def delete():
	if request.method == "POST":
		senderID = request.form['senderID']

		receiverSID = request.form['receiverSID']
		receiverID = request.form['receiverID']
		
		orderID = request.form['orderID']

		itemOID = request.form['itemOID']
		
		cursor = mysql.connection.cursor()

		
		if request.form['delete'] == 'deleteS':
			if senderID!='':
				cursor.execute("""DELETE FROM customerinfo.Items WHERE orderID = ANY(
					SELECT orderID FROM customerinfo.Orders WHERE senderID=%s)""", [senderID])
				cursor.execute("DELETE FROM customerinfo.Orders WHERE senderID=%s",[senderID])
				cursor.execute("DELETE FROM customerinfo.Receivers WHERE senderID=%s",[senderID])
				cursor.execute("DELETE FROM customerinfo.Senders WHERE senderID=%s",[senderID])
		
		if request.form['delete'] == 'deleteR':
			if receiverSID!='' and receiverID!='':
				cursor.execute("""DELETE FROM customerinfo.Items WHERE orderID = ANY(
					SELECT orderID FROM customerinfo.Orders WHERE receiverID=%s)""", [receiverID])
				cursor.execute("DELETE FROM customerinfo.Orders WHERE receiverID=%s",[receiverID])
				cursor.execute("DELETE FROM customerinfo.Receivers WHERE receiverID=%s",[receiverID])


		if request.form['delete'] == 'deleteO':
			if orderID!='':
				cursor.execute("""DELETE FROM customerinfo.Items WHERE orderID = ANY(
					SELECT orderID FROM customerinfo.Orders WHERE orderID=%s)""", [orderID])
				cursor.execute("DELETE FROM customerinfo.Orders WHERE orderID=%s",[orderID])

		if request.form['delete'] == 'deleteI':
			if itemOID!='':
				cursor.execute("DELETE FROM customerinfo.Items WHERE orderID=%s",[itemOID])
		
		mysql.connection.commit()
		cursor.close()
	return render_template("delete.html")

