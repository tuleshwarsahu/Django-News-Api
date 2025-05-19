import requests
from .models import Articles

def get_news_from_api(url):
    try:
        data = requests.get(url)
        data = data.json()
        print(data)
        if data.get('articles'):
            for article in data.get('articles'):
                source = article.get('source').get('name')
                author = article.get('author')
                title = article.get('title')
                description = article.get('description')
                url = article.get('url')
                url_to_image = article.get('urlToImage')
                published_at = article.get('publishedAt')
                content = article.get('content')
                
                Articles.objects.create(
                    source=source,
                    author=author,  
                    title=title,
                    description=description,
                    url=url,
                    url_to_image=url_to_image,
                    published_at=published_at,
                    content=content
                )
        
    except Exception as e:
        print(e)
        data = None