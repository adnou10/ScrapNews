#import modules
from flask import render_template, redirect, flash, url_for, Response,request
from app import app
from app.forms import URLForm
from app.models.article import Article
from app.scrap import Scrap as scr

#Home page that shows the 'get url' form
@app.route('/')
@app.route('/index')
def index():
    form = URLForm()
    return render_template('index.html', form=form)

@app.route('/articles',methods=['POST'])
def articles():
    if request.method == 'POST':
        url=request.form.get('url')
        page=scr.ScrapPage(url)            # Using our Scrap module to scrap the website
        articles=page.Articles()
        r=[]
        for article in articles[0:4]:
            b=scr.ScrapArticles()
            b.run(article,url)
            r.append(b.headline)
        return str(r)
    return redirect(url_for('index'))
    #articles=Article.objects.to_json()
    #return Response(articles,mimetype="application/json",status=200)
    #form = URLForm()
    #return render_template('index.html', form=form)