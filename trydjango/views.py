from django.http import HttpResponse
from articles.models import Article
import random


def home(request):
    random_id = random.randint(1, 4)
    article_obj = Article.objects.get(id=random_id)

    HTML_STRING = f"""
        <h1>{article_obj.title} ({article_obj.id})!</h1>
        """

    P_STRING = f"""
        <p>{article_obj.content}</p>
    """

    HTML_STRING = HTML_STRING + P_STRING

    return HttpResponse(HTML_STRING)
