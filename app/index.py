from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.http import JsonResponse
from newspaper import Article
from textblob import TextBlob
from api import LanguageTranslation

languages = {
    'en': "English",
    'fr': "French",
    'de': "German",
    'es': "Spanish",
    'it': "Italian",
    'ja': "Japanese",
    'pt': "Portugese",
}

def index(request):

    context = {'targets': languages}

    return render(request, 'app/index.html', context)



def result(request):
    (dest_lang, url) = ("", "")
    try:
        url = request.POST['url']
        dest_lang = request.POST['dest_lang']
    except KeyError:
        pass

    if url == "":
        raise Http404("No url given!")

    article = Article(url)
    article.download()
    article.parse()
    text = article.text
    translated = LanguageTranslation().translate(text, dest_lang)
    context = {'title': article.title,
        'author': (" % ").join(article.authors), 'text': text,
        'transtxt': translated, 'nouns': TextBlob(text).noun_phrases,
        'transnouns': TextBlob(translated).noun_phrases}
    #if request.is_ajax():
    #    return JsonResponse(context)
    return render(request, 'app/decomposed.html', context)
