import mysql.connector

# Create database connection
mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "root",
		database = "customerInfo",
		)

cursor = mydb.cursor()

# Create Customer database
cursor.execute("CREATE DATABASE customerInfo")

#Create tables
cursor.execute("""CREATE TABLE Senders (senderID int PRIMARY KEY NOT NULL , fname VARCHAR(50), 
	lname VARCHAR(50), phone VARCHAR(12) NOT NULL, addr VARCHAR(255), email VARCHAR(255),
	CHECK (senderID<99999 AND senderID>10000))""")

cursor.execute("""CREATE TABLE Receivers (senderID int, receiverID int PRIMARY KEY AUTO_INCREMENT,
	fname VARCHAR(50), lname VARCHAR(50), phone VARCHAR(12), addr VARCHAR(255), email VARCHAR(255),
	FOREIGN KEY(senderID) REFERENCES Senders(senderID))""")

cursor.execute("""CREATE TABLE Orders (
	senderID int, receiverID int, orderID VARCHAR(5) PRIMARY KEY, 
	price FLOAT, weight FLOAT, dateOrder DATE,
	FOREIGN KEY(senderID) REFERENCES Senders(senderID),
	FOREIGN KEY(receiverID) REFERENCES Receivers(receiverID)
	)""")

cursor.execute("""CREATE TABLE Items (
	orderID VARCHAR(5), 
	list VARCHAR(255),
	type VARCHAR(255),
	FOREIGN KEY(orderID) REFERENCES Orders(orderID)
	)""")

# Adding datas to database
senders = [(23143, "Lara", "Croft", "202-555-0157", "87 Beacon St", "lara@gmail.com"),
		(21745, "Camile", "Micheal", "202-555-0199", "853 Cobblestone Ave", "camile@gmail.com"),
		(34512, "Matt", "King", "775-555-0199", "68 Greenrose Ave", "mattking@gmail.com"),
		(65423, "Dan", "Howell", "410-555-0124", "68 Fawn Road", "howell@gmail.com"),
		(89045, "Sheldon", "Massey", "843-555-0164", "98 East Westport St", "shel123@gmail.com"),
		(43254, "Teresa", "Anderson", "843-555-0196", "54 Galvin St", "tanderson@gmail.com"),
		(37133, "Maria", "Micheal", "617-555-0174", "31 West Riverview", "michealm@gmail.com"),
		(72456, "Matt", "Hardy", "360-555-0169", "397 South Oak", "hardymatty@gmail.com"),
		(23475, "Margie", "Mandez", "775-555-0106", "4 Saxton St.", "mandezmar@gmail.com"),
		(23468, "Kim", "Dean", "410-555-0175", "7388 Newport Ave.", "kim@gmail.com")]

for data in senders:
	cursor.execute("INSERT INTO Senders VALUES(%s,%s,%s,%s,%s,%s)",
					(data[0],data[1],data[2],data[3],data[4],data[5]))

receivers = [(23143, "Hoa", "Nguyen", "0896-323-897", "1596 Hung Vuong Ave", "hoa@gmail.com"),
		(21745, "Phi", "Tran", "0519-215-567", "281 Han Hai Nguyen St", "tranphi@gmail.com"),
		(34512, "Tien", "Nguyen", "0139-884-725", "319 Ly Thuong Kiet St", "tienn@gmail.com"),
		(65423, "Hoang", "Dang", "0792-736-352", "878 Tran Cao Van", "hoangdang@gmail.com"),
		(23143, "Khoi", "Dao", "0168-836-519", "13 Hang Khoai St", "khoidaoo@gmail.com"),
		(72456, "Teo", "Pham", "0595-144-496", "69 Yen Vien", "teopham@gmail.com"),
		(89045, "Hai", "Mai", "0508-889-496", "51/16 Cao Thang St", "maii@gmail.com"),
		(43254, "Quan", "Ho", "0894-631-334", "18/5A Cong Hoa", "hoquan@gmail.com"),
		(37133, "Manh", "Phan", "0928-312-968", "6 Cua Dong St", "phanmanh@gmail.com"),
		(72456, "Long", "Phan", "0220-777-797", "12/1 Dong Den Str", "longg@gmail.com"),
		(72456, "An", "Nguyen", "0854-888-305", "58 Lo Duc", "ann@gmail.com"),
		(23475, "Tuan", "Huynh", "0358-790-495", "130 Phan Chu Trinh", "huynhtuan@gmail.com"),
		(23468, "Khoi", "Vu", "0212-249-533", "4 Nguyen Van Cu St", "khoivu@gmail.com"),
		(89045, "Yen", "Hung", "0730-819-156", "118 Cau Giay", "hungyen@gmail.com"),]

for data in receivers:
	cursor.execute("""INSERT INTO Receivers(senderID,fname,lname,phone,addr,email) 
		VALUES(%s,%s,%s,%s,%s,%s)""", (data[0],data[1],data[2],data[3],data[4],data[5]))

orders = [(23143, 1, "A3421", 53.00, 17.5, "2019-01-02"),
		(21745, 2, "A2437", 30.13, 10.0, "2020-11-12"),
		(34512, 3, "A4321", 105.75, 32.8, "2020-01-30"),
		(65423, 4, "A9623", 75.25, 25.4, "2021-01-19"),
		(23143, 5, "A5312", 512.12, 106.8, "2021-02-11"),
		(72456, 6, "A2516", 40.23, 11.8, "2021-04-05"),
		(89045, 7, "A3521", 53.75, 15.0, "2021-07-28"),
		(43254, 8, "A7243", 234.47, 65.0, "2021-08-15"),
		(37133, 9, "A6542", 123.23, 35.6, "2021-10-29"),
		(72456, 10, "A4522", 35.45, 10.5, "2022-01-25"),
		(72456, 11, "A5262", 90.12, 28.6, "2022-01-25"),
		(23475, 12, "A8372", 50.23, 10.3, "2022-05-01"),
		(23468, 13, "A5123", 67.12, 19.1, "2022-07-15"),
		(89045, 14, "A4067", 302.50, 31.6, "2022-10-29")]
for data in orders:
	cursor.execute("""INSERT INTO Orders VALUES(%s,%s,%s,%s,%s,%s)""", 
	(data[0],data[1],data[2],data[3],data[4],data[5]))

items = [("A3421", "Aspirin", "Medicines"),
		("A2437", "Books", "Books"),
		("A4321", "Candy, Chocolate", "Foods"),
		("A9623", "Dresses, T-shirts, Pants", "Clothes"),
		("A5312", "T-shirts, Chocolate, Aspirin", "Clothes, Foods, Medicines"),
		("A2516", "Macbooks, Aspirin", "Macs, Medicines"),
		("A3521", "Iphones, Ensure", "Iphone, Dairy"),
		("A7243", "Ensure, Chocolate, T-shirts, Pants", "Dairy, Foods, Clothes"),

		("A6542", "Aspirin, Books, Candy, Chocolates", "Books, Medicines, Foods"),


		("A4522", "Keyboards", "Electronic Devices"),
		("A5262", "S22 Ultra, Aspirin, Pants", "Phones, Medicines, Clothes"),
		("A8372", "Chocolate", "Foods"),
		("A5123", "Aspirin, Vitamins", "Medicines"),
		("A4067", "T-shirts, Cereal, Keyboards", "Clothes, Dairy, Electronic Devices")]
for data in items:
	cursor.execute("""INSERT INTO Items VALUES(%s,%s,%s)""", 
		(data[0],data[1],data[2]))

# Commit Changes
mydb.commit()
# Close connection
cursor.close()