#import modules
from flask import render_template, redirect, flash, url_for, Response
from app import app
from app.forms import URLForm
from app.models.article import Article


#Home page that shows the 'get url' form
@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():               # if "post"
        url=form.url.data                       # get url
        flash('URL entered {}'.format(url))
        return redirect(url_for('articles'),url=url)
    return render_template('index.html', form=form)

@app.route('/articles/<url>')#,methods=['GET','POST'])
def articles(url):
    return url
    #articles=Article.objects.to_json()
    #return Response(articles,mimetype="application/json",status=200)
    #form = URLForm()
    #return render_template('index.html', form=form)