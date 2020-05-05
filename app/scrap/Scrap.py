# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:38:42 2020

@author: NOUHAILA
"""

# import libraries
from bs4 import BeautifulSoup
from requests import get


# get html page    
def getHTMLPage(link):
    print('link',link)
    page=get(link)
    #page = urllib.request.urlopen(link).read()                         # query the website and return the html to the variable 'page'
    soup = BeautifulSoup(page.text, 'html.parser')                       # parse the html using beautiful soup and store in variable 'soup'
    return soup

class ScrapPage(object):
    def __init__(self,link):
        self.link=link      # page's url to crawl ex: www.bbc.com
              
    # find all articles in page 
    def Articles(self):
        soup=getHTMLPage(self.link)
        articles = soup.find_all('div', attrs={'class': 'media__content'})
        return articles
      
class ScrapArticles(object):
    
    def __init__(self):
        self.summary=''
        self.url=''       # url of article
        self.headline=''
        self.authors=[]
        self.content=''
        self.keywords=[]
    
    # get the composants of the article
    def run(self,article,link): 
        self.url =  article.find('a', attrs={'class': 'media__link'}).get('href')   # url of an article from href attribute
        if "https://www" not in self.url:
            self.url = link + self.url                                      
        summ = article.find('p', attrs={'class': 'media__summary'})               # article's summary
        if summ!= None:
             self.summary=summ.text
        soup=getHTMLPage(self.url)
        if soup!=None:
            body = soup.find('div', attrs={'class': 'story-body'})
            if body != None:
                content=body.find('div', attrs={'property': 'articleBody'})       # get the content of the article
                if content != None:
                    for i in content.find_all(['script','figure','div']):            # Clean the content from superflu
                        i.decompose()
                    self.content=content.text
                if self.content!='':
                    title=body.find('h1', attrs={'class': 'story-body__h1'})
                    if title != None:
                        self.headline= title .text            # get the headline of the article
                    authors_txt = body.find('span', attrs={'class': 'byline__name'})           # get the authors of the article
                    if authors_txt!= None:
                        authors_txt = body.find('span', attrs={'class': 'byline__name'}).text  
                        names = authors_txt.split('By ')
                        names.remove('')
                        self.authors = names
                
                    tag=soup.find('ul', attrs={'class': 'tags-list'})
                    if tag != None:
                        tags=tag.find_all('li')
                        for i in tags:
                            keyword=i.text
                            self.keywords.append(keyword)
                            
#if content is empty , no need to get other fields , to handle error later for article that don't have property=articleBody in their html




'''link='https://www.bbc.com'       
a=ScrapPage(link)        
articles=a.Articles()    
for article in articles[0:4]:
    b=ScrapArticles()
    b.run(article,link)
    print(b.headline)
    print(b.authors)
    print(b.content)
    print(b.url)
    print(b.summary)
    print(b.keywords)'''

