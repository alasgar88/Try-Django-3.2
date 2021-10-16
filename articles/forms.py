from django import forms
from django.core.exceptions import ValidationError

from articles.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title}is already taken")
        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError("This title is taken.")
    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title.lower().strip() == "1":
            raise forms.ValidationError("Title can not containe 1")

        if "office" in content.lower().strip():
            self.add_error(
                'content', 'Content cant not contain the word office')
        return cleaned_data
