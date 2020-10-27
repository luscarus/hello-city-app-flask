class Config(object):
	DEBUG = False
	TESTING = False

	SECRET_KEY = '1kvuyvuyjhb3jbgyvv7opkuyh1t'

	DB_NAME = 'production-db'
	DB_USERNAME = 'root'
	DB_PASSWORD = 'example'

	UPLOADS = '/home/username/app/app/static/images/uploads'

	SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
	pass


class DevelopmentConfig(Config):
	DEBUG = True

	DB_NAME = 'panterest_dev'
	DB_USERNAME = 'root'
	DB_PASSWORD = 'example'

