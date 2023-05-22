from Config import db
from sqlalchemy.dialects.mysql import LONGTEXT


class TBActivities(db.Model):
	p_id = db.Column(db.Integer, primary_key=True)
	p_name = db.Column(db.String(255))
	p_content = db.Column(LONGTEXT)
	p_start_time = db.Column(db.TIMESTAMP)
	p_end_time = db.Column(db.TIMESTAMP)
	p_brief = db.Column(LONGTEXT)

	def __init__(self, p_name, p_content, p_start_time, p_end_time, p_brief):
		self.p_name = p_name
		self.p_content = p_content
		self.p_start_time = p_start_time
		self.p_end_time = p_end_time
		self.p_brief = p_brief

	def __repr__(self):
		return '<TBActivate %r>' % self.p_name

