from flask import Flask


app = Flask(__name__)


if app.config["ENV"] == "production":
	app.config.from_object("config.ProductionConfig")

else:
	app.config.from_object("config.DevelopmentConfig")


from hello_city import views

