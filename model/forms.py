from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search_creater=StringField('creater',validators=[DataRequired()])
    submit=SubmitField('搜索')