# We define a function to structure our data as a json model
def ToJson(authors,content,url,headline,keywords,summary):
    json={
            'summary':summary,
            'authors':authors,
            'content':content,
            'url':url,           
            'headline':headline,
            'keywords':keywords
            }
    return json