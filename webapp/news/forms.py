from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError

from webapp.news.models import News

class CommentForm(FlaskForm):
    news_id = HiddenField('ID новости', validators=[DataRequired()])
    comment_text = StringField('Комментарий', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Отправить', render_kw={'class': 'bnt bnt-primary'})

    def validate_news_id(self, news_id):
        if not News.query.get(news_id.data):
            raise ValidationError('Новость с таким id не существует')
