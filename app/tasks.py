from app.models.article import Article
from app.scrap import Scrap as scr
from app.scrap import tojson as tjs
import time
from rq import get_current_job

'''def _set_task_progress(progress):
    job = get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()'''
        
    
#--------------------------------------------------- Background job --------------------------------------------------
def scrap_and_save(url):
    #try:
        #_set_task_progress(0)
        data = []
        page=scr.ScrapPage(url)            # Using our Scrap module to scrap the website
        articles=page.Articles()
        n=len(articles)
        i=0
        for article in articles:
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
                print(json['headline'])
                data.append(json)
                #time.sleep(5)
                i += 1
        return data
    