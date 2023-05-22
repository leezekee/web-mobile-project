from . import bp
from flask import request, make_response
from app.activity.models import TBActivities


@bp.route('/query/all', methods=['GET'])
def query_all():
	activities = TBActivities.query.all()
	data = {
		'code': 200,
		'msg': 'success',
		'data': []
	}

	for activity in activities:
		data['data'].append({
			'p_id': activity.p_id,
			'p_name': activity.p_name,
			'p_start_time': activity.p_start_time,
			'p_end_time': activity.p_end_time,
			'p_brief': activity.p_brief
		})
	return make_response(data)


@bp.route('/query/<pid>', methods=['GET'])
def query_id(pid):
	activity = TBActivities.query.filter_by(p_id=pid).first()
	if activity is None:
		data = {
			'code': 100,
			'msg': 'Activity not found',
		}
		return make_response(data)
	data = {
		'code': 200,
		'msg': 'success',
		'data': []
	}

	data['data'].append({
		'p_id': activity.p_id,
		'p_name': activity.p_name,
		'p_start_time': activity.p_start_time,
		'p_end_time': activity.p_end_time,
		'p_brief': activity.p_brief,
		'p_content': activity.p_content
	})
	return make_response(data)
