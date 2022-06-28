from flask import Blueprint,render_template,url_for,request
from werkzeug.utils import redirect
import testdb
from pybo import db
from pybo.models import Question,Answer
from datetime import datetime
from ..forms import AnswerForm


bp = Blueprint('answer',__name__,url_prefix='/answer')

@bp.route('/create/<int:question_id>' , methods=('POST',))
def create(question_id):
    form=AnswerForm()
    question = Question.query.get_or_404(question_id)

    if form.validate_on_submit():
        answer = Answer(content=form.content.data, create_date=datetime.now())
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail',question_id=question_id))

    return render_template('question/question_detail.html',question=question,form=form)
