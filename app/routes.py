#import modules
from flask import render_template, redirect, flash, url_for, Response,request
from app import app
from app.forms import URLForm
from app.models.article import Article
from app.scrap import Scrap as scr
from app.scrap import tojson as tjs

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
        for article in articles[0:5]:
            b=scr.ScrapArticles()
            b.run(article,url)
            content=b.content
            if content!='':
                headline=b.headline
                authors=b.authors
                url_art=b.url
                summary=b.summary
                keywords=b.keywords
                json=tjs.ToJson(authors,content,url_art,headline,keywords,summary)
                article = Article(**json).save()
                r.append([article.id,article.content])
        arts=Article.objects
        return  render_template('articles.html',arts=arts)   #display articles in db
    return redirect(url_for('index'))

# To see article's detail 
@app.route("/disp/<id>") 
def display(id):
    art=Article.objects.get(id=id)
    return render_template('article.html',art=art)
    #return render_template('display.html',arh=arh,cont=arc)
    