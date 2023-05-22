from . import bp
from flask import make_response
from app.tips.models import TBTips
from sqlalchemy.sql import func
import random


@bp.route('/get', methods=['GET'])
def get_tips():
	try:
		total = TBTips.query.count()
		random_index = random.randint(1, total)
		random_tip = TBTips.query.offset(random_index).first()
		data = {
			'tip': random_tip.tip,
			'msg': 'success',
			'code': 200
		}
		return make_response(data)
	except Exception as e:
		print(e)
		data = {
			'msg': 'no data',
			'code': 100,
			'tips': []
		}
		return make_response(data)



