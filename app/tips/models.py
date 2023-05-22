from Config import db
from sqlalchemy.dialects.mysql import LONGTEXT


class TBTips(db.Model):
	p_id = db.Column(db.Integer, primary_key=True)
	p_tips = db.Column(LONGTEXT)

	def __init__(self, tips):
		self.p_tips = tips

	def __repr__(self):
		return f'<TBTips {self.p_tips}>'