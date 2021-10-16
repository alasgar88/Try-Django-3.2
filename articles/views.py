from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from articles.admin import ArticleAdmin
from .models import Article
from .forms import ArticleForm


def search_view(request):

    query_dict = request.GET.get("q")
    print(query_dict)

    article_list = Article.objects.filter(content__contains=query_dict)

    context = {
        "object_list": article_list
    }
    return render(request, 'articles/search.html', context=context)


@login_required
def create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        article_object = form.save()
        # to avoid  sending Post method again and  saving dublicate object after refresh page
        context['form'] = ArithmeticError()
        # This variant is for forms.Form type
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # article_object = Article(title=title, content=content)
        # article_object.save()
        context['title'] = article_object.title  # =title
        context['content'] = article_object.content  # =content
        context['created'] = True
        context['object'] = article_object
    return render(request, 'articles/create.html', context=context)


def detail_view(request, id):

    object = get_object_or_404(Article, id=id)

    context = {
        "object": object
    }
    return render(request, 'articles/detail.html', context=context)
