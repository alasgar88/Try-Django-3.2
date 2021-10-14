from django.http import HttpResponse
from articles.models import Article
import random
from django.template.loader import render_to_string


def home(request, *args, **kwargs):
    random_id = random.randint(1, 4)
    article_obj = Article.objects.get(id=random_id)

    object_list = Article.objects.all()
    context = {
        "object_list": object_list,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }

    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)
