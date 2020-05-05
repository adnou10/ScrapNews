from flask import render_template, redirect, flash, url_for, Response
from app import app
from app.forms import URLForm
from app.models.article import Article



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
    articles=Article.objects.to_json()
    return Response(articles,mimetype="application/json",status=200)
    #form = URLForm()
    #return render_template('index.html', form=form)