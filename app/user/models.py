from Config import db
from sqlalchemy.dialects.mysql import LONGTEXT


class TBUserInfo(db.Model):
	p_id = db.Column(db.Integer, primary_key=True)
	p_username = db.Column(db.String(255))
	p_password = db.Column(db.String(255))
	p_tel = db.Column(db.String(255))
	p_sid = db.Column(db.String(255))
	p_avatar = db.Column(LONGTEXT)
	p_resetcode = db.Column(db.String(255))
	p_age = db.Column(db.Integer)
	p_all_time = db.Column(db.Integer)
	p_all_meter = db.Column(db.Integer)
	p_all_calories = db.Column(db.Integer)
	p_count = db.Column(db.Integer)
	p_height = db.Column(db.Numeric(10, 2))
	p_weight = db.Column(db.Numeric(10, 2))
	p_is_running = db.Column(db.Integer)

	def __init__(self, username, password, tel, resetcode, sid='', avatar='', age=0, all_time=0, all_meter=0, all_calories=0, count=0, height=0, weight=0):
		self.p_username = username
		self.p_password = password
		self.p_tel = tel
		self.p_sid = sid
		self.p_avatar = avatar
		self.p_resetcode = resetcode
		self.p_age = age
		self.p_all_time = all_time
		self.p_all_meter = all_meter
		self.p_all_calories = all_calories
		self.p_count = count
		self.p_height = height
		self.p_weight = weight
		self.p_is_running = 0

	def check_password(self, password):
		return self.p_password == password

	def __repr__(self):
		return f'<TBUserInfo {self.p_username}>'
