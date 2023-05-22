from Config import create_app, db
from dotenv import load_dotenv
import os
from gevent import pywsgi


load_dotenv('.flaskenv')

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.route('/')
def hello():
	return 'Hello World!'


if __name__ == '__main__':
	# with app.app_context():
	# 	db.drop_all()
	# 	db.create_all()
	app.run(host='127.0.0.1', port=8090)
	# server = pywsgi.WSGIServer(('127.0.0.1', 8090), app)
	# server.serve_forever()
