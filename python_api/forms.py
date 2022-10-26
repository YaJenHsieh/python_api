from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length


class SearchForm(FlaskForm):
	searched = StringField('Search',validators=[DataRequired()])
	submit = SubmitField('Submit')

class EditNewsForm(FlaskForm):
	edit_news_title = TextAreaField('Edit News Title',validators=[DataRequired(),Length(min=1)]) 
	edit_news_content = TextAreaField('Edit News',validators=[DataRequired(),Length(min=1)]) 
	submit = SubmitField('Submit')

class AddNewsForm(FlaskForm):
	add_news_title = TextAreaField('Add News Title',validators=[DataRequired(),Length(min=1)])
	add_news_content = TextAreaField('Add News',validators=[DataRequired(),Length(min=1)])
	add_news_url = TextAreaField('Add News Url',validators=[DataRequired(),Length(min=1)]) 
	submit = SubmitField('Submit')


