import sqlalchemy

from . import bp
from flask import request, make_response, Response
from Config import db
from app.run.models import TBRunRecords
from app.user.models import TBUserInfo
from datetime import datetime


def get_time():
	nowTime = datetime.now()
	return nowTime


@bp.route('/start', methods=['POST'])
def run():
	username = request.json.get('username')
	# start_time = request.json.get('startTime')
	start_time = get_time()
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is not None:
		if user.p_is_running == 1:
			data = {
				'code': 100,
				'msg': 'User is running',
			}
			response = make_response(data)
			return response
		try:
			user_id = user.p_id
			runOldRec = TBRunRecords.query.filter_by(p_user_id=user_id).order_by(sqlalchemy.desc(TBRunRecords.p_id)).first()
			# print(runOldRec is None)
			if runOldRec and runOldRec.p_is_finish == 0:
				data = {
					"code": 100,
					"msg": "User is running",
				}
				response = make_response(data)
				return response
			user.p_is_running = 1
			newRun = TBRunRecords(user_id, None, None, None, start_time, None, 0)
			db.session.add(newRun)
			runRec = TBRunRecords.query.filter_by(p_user_id=user_id, p_start_time=start_time, p_is_finish=0).first()
			# print(runRec.p_id)
			data = {
				'code': 200,
				'msg': 'Start running',
				'runId': runRec.p_id,
			}
			response = make_response(data)
			return response
		except Exception as e:
			print(e)
			db.session.rollback()
			user.p_is_running = 0

			data = {
				'code': 100,
				'msg': 'Start running failed',
			}
			response = make_response(data)
			return response
		finally:
			db.session.commit()
	else:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response = make_response(data)
		return response


@bp.route('/end', methods=['POST'])
def end():
	username = request.json.get('username')
	# end_time = request.json.get('endTime')
	end_time = get_time()
	meters = request.json.get('meters')
	calories = request.json.get('calories')
	p_id = request.json.get('runId')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is not None:
		runRec = TBRunRecords.query.filter_by(p_id=p_id).first()
		if runRec is None:
			data = {
				"code": 100,
				"msg": "Run not found",
			}
			response = make_response(data)
			return response
		if runRec.p_is_finish == 1:
			data = {
				"code": 100,
				"msg": "User is not running",
			}
			response = make_response(data)
			return response
		runRec.p_is_finish = 1
		duration = (end_time - runRec.p_start_time).seconds
		# print(duration)
		# print(end_time)
		# print(runRec.p_start_time)

		if duration < 60:
			data = {
				"code": 100,
				"msg": "Duration is too short",
			}
			user.p_is_running = 0
			response = make_response(data)
			return response
		if runRec is not None:
			user.p_is_running = 0
			runRec.p_meters = meters
			runRec.p_calories = calories
			runRec.p_end_time = end_time
			runRec.time = duration
			db.session.commit()
			data = {
				'code': 200,
				'msg': 'End running',
				'duration': runRec.p_time,
				'startTime': runRec.p_start_time,
				'endTime': runRec.p_end_time,
			}
			response = make_response(data)
			return response
		else:
			data = {
				'code': 100,
				'msg': 'Serve error',
			}
			response = make_response(data)
			return response


@bp.route('/history', methods=['POST'])
def history():
	username = request.json.get('username')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is not None:
		runRecs = TBRunRecords.query.filter_by(p_user_id=user.p_id).all()
		data = {
			'code': 200,
			'msg': 'Get history',
			'history': [],
		}
		for runRec in runRecs:
			data['history'].append({
				'runId': runRec.p_id,
				'startTime': runRec.p_start_time,
				'endTime': runRec.p_end_time,
				'duration': runRec.p_time,
				'meters': runRec.p_meters,
				'calories': runRec.p_calories,
			})
		response = make_response(data)
		return response
	else:
		data = {
			'code': 100,
			'msg': 'User not found',
		}
		response: Response = make_response(data)
		return response


@bp.route('/query/isRunning', methods=['POST'])
def isRunning():
	username = request.json.get('username')
	user = TBUserInfo.query.filter_by(p_username=username).first()
	if user is not None:
		if user.p_is_running == 1:
			runRec = TBRunRecords.query.filter_by(p_user_id=user.p_id).first()
			if runRec is not None:
				data = {
					'code': 200,
					'msg': 'Is running',
					'isRunning': True,
					'runId': runRec.p_id,
					'startTime': runRec.p_start_time,
				}
				response = make_response(data)
				return response
			else:
				data = {
					'code': 200,
					'msg': 'Serve error',
					'isRunning': False,
				}
				response = make_response(data)
				return response
		else:
			data = {
				'code': 200,
				'msg': 'Is not running',
				'isRunning': False,
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



