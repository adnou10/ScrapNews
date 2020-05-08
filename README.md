# ScrapNews
===============
This is a web application for scraping news articles from "www.bbc.com" website.
[Soapbox](https://github.com/adhocteam/soapbox).

## Getting started
---------------

### Functionalities
---------------
 - Scrap News website
 - Store articles in MongoDb Atlas as a document of shape :
 [Soapbox]({
            'summary':<summary>,
            'authors':<authors>,
            'content':<content>,
            'url':<url>,           
            'headline':<headline>,
            'keywords':<keywords>
            }) 
 - Display the articles collection .
 - Provide search for articles by keyword .
 - Offers an API that provides access to the content in the mongo database.

### **Tools:**
---------------

The application was build using:

 - python 3.7 as the programming language
 - Flask as web developpement framework
 - beautifulsoup4 for the scrap

### Issues:
---------------
 
 - For now it only works on the "https://www.bbc.com/" website.
 - Don't scrap all articles
 

 [Soapbox](WHY?
 Because of the way I used bs4 in scraping was based on this url, I can say it lacks dynamicity)
 - Requires more tests

### Hosting:
 ---------------

 - heroku