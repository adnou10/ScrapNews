# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:10:22 2020

@author: NOUHAILA
"""

# import libraries
from bs4 import BeautifulSoup
import urllib.request

class ScrapArticle(object):
    
    def __init__(self,url):
        self._url=url
        self.headline=''
        self.authors=[]
        self.content=''

    #get the article's story
    def story(self):
        page = urllib.request.urlopen(self._url)                         # query the website and return the html to the variable 'page'
        soup = BeautifulSoup(page, 'html.parser')                       # parse the html using beautiful soup and store in variable 'soup'
        div = soup.find('div', attrs={'class': 'story-body'})              # get the story's body
        return div
    
    # get the composants of the article
    def run(self):
        
        body=self.story()
        self.headline= body.find('h1', attrs={'class': 'story-body__h1'}).text            # get the headline of the article

        authors_txt = body.find('span', attrs={'class': 'byline__name'}).text             # get the authors of the article
        print(authors_txt)
        names = authors_txt.split('By ')
        print(names)
        names.remove('')
        print (names)
        self.authors = names
    
        content=body.find('div', attrs={'property': 'articleBody'})                  # get the content of the article
        for i in content.find_all(['script','figure','div']):                        # Clean the content from superflu
               i.decompose()
        self.content=content.text
    
    
    
    
    
    
    
    
    
    
"""a=ScrapArticle("https://www.bbc.com/news/health-52530828")  
a.run()  
a.headline
a.authors
a.content"""