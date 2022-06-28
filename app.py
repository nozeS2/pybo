from pybo.models import Question,Answer
from datetime import datetime
from pybo import db

q = Question(subject='질문 1입니다.', content='질문1에 대한 내용입니다.',create_date=datetime.now())
db.session.add(q)
db.session.commit()