
# import libraries
from bs4 import BeautifulSoup
from requests import get
from urllib.parse import  urljoin


 
def get_content(storyBody):
    content=''
    for i in storyBody.find_all(['script','figure','style']):
        i.decompose()
    for i in storyBody.find_all(attrs={'class':'with-extracted-share-icons'}):
        i.decompose()
    if storyBody != None:
        content = storyBody.text
    return content

def get_headline (soup):
    headline=''
    headline_txt=soup.find('h1', attrs={'class': 'story-body__h1' }) or soup.find('h1', attrs={ 'class': 'story-headline'})
    if headline_txt != None:
        headline=headline_txt.text
    return headline

def get_summary(article):
    summary=''
    summ = article.find('p', attrs={'class': 'media__summary'})               # article's summary
    if summ!= None:
       summary=summ.text
    return summary

def get_authors(body):
    authors=[]
    authors_txt = body.find('span', attrs={'class': 'byline__name'})           # get the authors of the article
    if authors_txt!= None:
        authors_txt = body.find('span', attrs={'class': 'byline__name'}).text  
        names = authors_txt.split('By ')
        if '' in names:
            names.remove('')
            authors = names
    return authors

def get_keywords(soup):
     keywords=[]
     tag=soup.find('ul', attrs={'class': 'tags-list'})
     if tag != None:
         tags=tag.find_all('li')
         for i in tags:
             keyword=i.text
             keywords.append(keyword)
     return keywords

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
        url =  article.find('a', attrs={'class': 'media__link'})   # url of an article from href attribute
        if url !=None:
            self.url= url.get('href')
            self.url =urljoin(link , self.url  ) 
            self.summary = get_summary(article)                                   
            soup=getHTMLPage(self.url)
            if soup!=None:
                body = soup.find('div', attrs={'class': 'story-body'})
                if body != None:
                    self.content= get_content(body)
                    if self.content!='':
                        self.headline= get_headline(soup)            # get the headline of the article
                        self.authors = get_authors(body)
                        self.keywords = get_keywords(soup)
                    
                        
