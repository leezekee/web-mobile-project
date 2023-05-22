from app.activity.models import TBActivities
from app.tips.models import TBTips
from . import bp
from flask import request, make_response
from Config import db


@bp.route('/activity/add', methods=['POST'])
def add_activity():
	p_name = request.json.get('p_name')
	p_content = request.json.get('p_content')
	p_start_time = request.json.get('p_start_time')
	p_end_time = request.json.get('p_end_time')
	p_brief = request.json.get('p_brief')
	activity = TBActivities(p_name, p_content, p_start_time, p_end_time, p_brief)
	db.session.add(activity)
	db.session.commit()
	arec = TBActivities.query.filter_by(p_name=p_name).first()
	return make_response({'code': 200, 'msg': 'success', 'id': arec.p_id})


@bp.route('/activity/delete', methods=['POST'])
def delete_activity():
	p_id = request.json.get('p_id')
	activity = TBActivities.query.filter_by(p_id=p_id).first()
	db.session.delete(activity)
	db.session.commit()
	return make_response({'code': 200, 'msg': 'success'})


@bp.route('/activity/update/content', methods=['POST'])
def update_activity_content():
	p_id = request.json.get('id')
	p_content = request.json.get('content')
	activity = TBActivities.query.filter_by(p_id=p_id).first()
	if activity:
		activity.p_content = p_content
		db.session.commit()
		return make_response({'code': 200, 'msg': 'success'})
	else:
		return make_response({'code': 404, 'msg': 'not found'})


@bp.route('/activity/update/brief', methods=['POST'])
def update_activity_brief():
	p_id = request.json.get('id')
	p_brief = request.json.get('brief')
	activity = TBActivities.query.filter_by(p_id=p_id).first()
	if activity:
		activity.p_brief = p_brief
		db.session.commit()
		return make_response({'code': 200, 'msg': 'success'})
	else:
		return make_response({'code': 404, 'msg': 'not found'})


@bp.route('/activity/update/time', methods=['POST'])
def update_activity_time():
	p_id = request.json.get('id')
	p_start_time = request.json.get('startTime')
	p_end_time = request.json.get('endTime')
	activity = TBActivities.query.filter_by(p_id=p_id).first()
	if activity:
		activity.p_start_time = p_start_time
		activity.p_end_time = p_end_time
		db.session.commit()
		return make_response({'code': 200, 'msg': 'success'})
	else:
		return make_response({'code': 404, 'msg': 'not found'})


@bp.route('/activity/update/name', methods=['POST'])
def update_activity_name():
	p_id = request.json.get('id')
	p_name = request.json.get('name')
	activity = TBActivities.query.filter_by(p_id=p_id).first()
	if activity:
		activity.p_name = p_name
		db.session.commit()
		return make_response({'code': 200, 'msg': 'success'})
	else:
		return make_response({'code': 404, 'msg': 'not found'})


@bp.route('/tips/add', methods=['POST'])
def add_tips():
	tip = request.json.get('tip')
	tips = TBTips(tip)
	db.session.add(tips)
	db.session.commit()
	tiprec = TBTips.query.filter_by(tip=tip).first()
	return make_response({'code': 200, 'msg': 'success', 'id': tiprec.id})


@bp.route('/tips/delete', methods=['POST'])
def delete_tips():
	pid = request.json.get('id')
	tips = TBTips.query.filter_by(id=pid).first()
	db.session.delete(tips)
	db.session.commit()
	return make_response({'code': 200, 'msg': 'success'})
