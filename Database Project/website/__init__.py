from flask import Flask
from flask_mysqldb import MySQL



mysql = MySQL()



def webapp():
	web = Flask(__name__)
	web.config["SECRET_KEY"] = "database"
	web.config["MYSQL_HOST"] = "localhost"
	web.config["MYSQL_USER"] = "root"
	web.config["MYSQL_PASSWORD"] = "root"
	web.config["MYSQL_DB"] = "customerInfo"
	mysql = MySQL(web)

	from .views import views
	from .auth import auth

	web.register_blueprint(views, url_prefix="/")
	web.register_blueprint(auth, url_prefix="/")

	

	return web


