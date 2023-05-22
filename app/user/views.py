from flask import request, make_response
from app.user.models import TBUserInfo
from Config import db
from . import bp

# from flask import Blueprint
#
# bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/', methods=['GET', 'POST'])
def test():
	return {'msg': 'success'}


@bp.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is not None:
		if user.check_password(password):
			data = {
				'code': 200,
				'msg': 'Success',
			}
			response = make_response(data)
			return response
		else:
			data = {
				'code': 100,
				'msg': 'Wrong Password',
			}
			response = make_response(data)
			return response
	else:
		data = {
			'code': 100,
			'msg': 'User not found, please register first',
		}
		response = make_response(data)
		return response


@bp.route('/register', methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	tel = request.json.get('tel')
	resetcode = request.json.get('resetcode')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is not None:
		data = {
			'code': 100,
			'msg': 'User already exists',
		}
		response = make_response(data)
		return response
	else:
		newUser = TBUserInfo(username, password, tel, resetcode)
		db.session.add(newUser)
		db.session.commit()
		data = {
			'code': 200,
			'msg': 'Success',
		}
		response = make_response(data)
		return response


@bp.route('/reset', methods=['POST'])
def reset():
	username = request.json.get('username')
	password = request.json.get('password')
	resetcode = request.json.get('resetcode')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is not None:
		if user.p_resetcode == resetcode:
			user.p_password = password
			db.session.commit()

			data = {
				'code': 200,
				'msg': 'Success',
			}
			response = make_response(data)
			return response
		else:
			data = {
				'code': 100,
				'msg': 'Wrong reset code',
			}
			response = make_response(data)
			return response
	else:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response = make_response(data)
		return response


@bp.route('/update/password', methods=['POST'])
def update_password():
	username = request.json.get('username')
	password = request.json.get('password')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is None:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response = make_response(data)
		return response
	user.p_password = password
	db.session.commit()
	data = {
		'code': 200,
		'msg': 'Success',
	}
	response = make_response(data)
	return response


@bp.route('/update/avatar', methods=['POST'])
def update_avatar():
	username = request.json.get('username')
	avatar = request.json.get('avatar')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is None:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response = make_response(data)
		return response
	user.p_avatar = avatar
	db.session.commit()
	data = {
		'code': 200,
		'msg': 'Success',
	}
	response = make_response(data)
	return response


@bp.route('/update/resetcode', methods=['POST'])
def update_resetcode():
	username = request.json.get('username')
	resetcode = request.json.get('resetcode')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is None:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response = make_response(data)
		return response
	user.p_resetcode = resetcode
	db.session.commit()
	data = {
		'code': 200,
		'msg': 'Success',
	}
	response = make_response(data)
	return response


@bp.route('/update/tel', methods=['POST'])
def update_tel():
	username = request.json.get('username')
	tel = request.json.get('tel')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is None:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response = make_response(data)
		return response
	user.p_tel = tel
	db.session.commit()
	data = {
		'code': 200,
		'msg': 'Success',
	}
	response = make_response(data)
	return response


@bp.route('/update/sid', methods=['POST'])
def update_sid():
	username = request.json.get('username')
	sid = request.json.get('sid')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is None:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response = make_response(data)
		return response
	user.p_sid = sid
	db.session.commit()
	data = {
		'code': 200,
		'msg': 'Success',
	}
	response = make_response(data)
	return response


@bp.route('/update/height', methods=['POST'])
def update_height():
	username = request.json.get('username')
	height = request.json.get('height')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is None:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response = make_response(data)
		return response
	user.p_height = height
	db.session.commit()
	data = {
		'code': 200,
		'msg': 'Success',
	}
	response = make_response(data)
	return response


@bp.route('/update/weight', methods=['POST'])
def update_weight():
	username = request.json.get('username')
	weight = request.json.get('weight')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is None:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response = make_response(data)
		return response
	user.p_weight = weight
	db.session.commit()
	data = {
		'code': 200,
		'msg': 'Success',
	}
	response = make_response(data)
	return response


@bp.route('/update/age', methods=['POST'])
def update_age():
	username = request.json.get('username')
	age = request.json.get('age')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is None:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response = make_response(data)
		return response
	user.p_age = age
	db.session.commit()
	data = {
		'code': 200,
		'msg': 'Success',
	}
	response = make_response(data)
	return response


@bp.route('/update/basicinfo', methods=['POST'])
def update_basicinfo():
	username = request.json.get('username')
	weight = request.json.get('weight')
	height = request.json.get('height')
	age = request.json.get('age')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is None:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response = make_response(data)
		return response
	user.p_weight = weight
	user.p_height = height
	user.p_age = age
	db.session.commit()
	data = {
		'code': 200,
		'msg': 'Success',
	}
	response = make_response(data)
	return response


@bp.route('/query/<username>', methods=['GET'])
def query_username(username):
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is not None:
		data = {
			'code': 200,
			'msg': 'Success',
			'username': user.p_username,
			'avatar': user.p_avatar,
			'tel': user.p_tel,
			'sid': user.p_sid,
			'height': user.p_height,
			'weight': user.p_weight,
			'age': user.p_age,
			'all_meter': user.p_all_meter,
			'all_calories': user.p_all_calories,
			'all_time': user.p_all_time,
		}
		response = make_response(data)
		return response
	else:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response = make_response(data)
		return response



