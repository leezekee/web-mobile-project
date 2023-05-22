from Config import db
from sqlalchemy.dialects.mysql import DATETIME


class TBRunRecords(db.Model):
	p_id = db.Column(db.Integer, primary_key=True)
	p_user_id = db.Column(db.Integer)
	p_meters = db.Column(db.Integer)
	p_time = db.Column(db.Integer)
	p_calories = db.Column(db.Integer)
	p_start_time = db.Column(DATETIME(fsp=6))
	p_end_time = db.Column(DATETIME(fsp=6))
	p_is_finish = db.Column(db.Integer)

	def __init__(self, user_id, meters, time, calories, start_time, end_time, is_finish):
		self.p_user_id = user_id
		self.p_meters = meters
		self.p_time = time
		self.p_calories = calories
		self.p_start_time = start_time
		self.p_end_time = end_time
		self.p_is_finish = is_finish

	def __repr__(self):
		return '<TBRunRecords %r>' % self.p_id
