# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:38:42 2020

@author: NOUHAILA
"""

# import libraries
from bs4 import BeautifulSoup
import urllib.request


# get html page    
def getHTMLPage(link):
    page = urllib.request.urlopen(link)                         # query the website and return the html to the variable 'page'
    soup = BeautifulSoup(page, 'html.parser')                       # parse the html using beautiful soup and store in variable 'soup'
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
        self.url = link + article.find('a', attrs={'class': 'media__link'}).get('href')   # url of an article from href attribute
        summ = article.find('p', attrs={'class': 'media__summary'})               # article's summary
        if summ!= None:
             self.summary=summ.text
        soup=getHTMLPage(self.url)
        body = soup.find('div', attrs={'class': 'story-body'})
        self.headline= body.find('h1', attrs={'class': 'story-body__h1'}).text            # get the headline of the article
        authors_txt = body.find('span', attrs={'class': 'byline__name'})           # get the authors of the article
        if authors_txt!= None:
            authors_txt = body.find('span', attrs={'class': 'byline__name'}).text  
            names = authors_txt.split('By ')
            names.remove('')
            self.authors = names
        content=body.find('div', attrs={'property': 'articleBody'})                  # get the content of the article
        for i in content.find_all(['script','figure','div']):                        # Clean the content from superflu
               i.decompose()
        self.content=content.text
        tags=soup.find('ul', attrs={'class': 'tags-list'}).find_all('li')
        for i in tags:
            keyword=i.text
            self.keywords.append(keyword)

        




"""link='https://www.bbc.com'       
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
    print(b.keywords)
"""
