from flask import render_template,redirect,flash,url_for
from app import app
from app.forms import URLForm



@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        flash('URL entered {}'.format(
            form.url.data))
        return redirect(url_for('articles'))
    return render_template('index.html', form=form)

@app.route('/articles')#,methods=['GET','POST'])
def articles():
    form = URLForm()
    return render_template('index.html', form=form)