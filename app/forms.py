from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired, url
from flask_wtf.html5 import URLField
from wtforms.validators import url

class URLForm(FlaskForm):
    url = URLField('URL',validators=[url(),DataRequired()])
    submit = SubmitField('Scrap')