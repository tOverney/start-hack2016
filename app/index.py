from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.http import JsonResponse
from newspaper import Article
from textblob import TextBlob
<<<<<<< Updated upstream
from api import LanguageTranslation
=======
from textblob_fr import PatternTagger, PatternAnalyzer
from django.views.decorators.csrf import csrf_exempt
from news.search_related_news import SearchRelatedNews
from api import LanguageTranslation, Api
>>>>>>> Stashed changes

languages = {
    'en': "English",
    'fr': "French",
    'de': "German",
    'es': "Spanish",
    'it': "Italian",
    'ja': "Japanese",
    'pt': "Portugese",
}

languagesBing = {
    'en': 'en-GB',
    'fr': 'fr-CH',
    'de': 'de-CH',
    'es': 'es-ES',
    'it': 'it-IT',
    'ja': 'ja-JP',
    'pt': 'pt-PT'
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
    keywords = selectKeywords(TextBlob(translated).noun_phrases, 4)
    print(keywords)

    market = languagesBing[dest_lang]
    
    relatedArticles = SearchRelatedNews().get(keywords, market)

    context = {'title': article.title,
        'author': (" % ").join(article.authors), 'text': text,
        'transtxt': translated, 'nouns': TextBlob(text).noun_phrases,
        'transnouns': TextBlob(translated).noun_phrases,
        'related': relatedArticles}

    if request.is_ajax():
        return JsonResponse(context)
    return render(request, 'app/decomposed.html', context)


@csrf_exempt
def concept_info(request):
    print(request.POST)
    concept = ""
    try:
        concept = request.POST['concept']
    except KeyError:
        concept = ""

    if concept == "":
        raise Http404("No concept!")

    api = Api()
    concept = api.text_insight.concepts(concept)
    if request.is_ajax():
        return JsonResponse({})
    return render(request, 'app/decomposed.html', concept)


def selectKeywords(words, nb):
    keys = []
    for i in range(0, 4):
        keys.append(words.pop(i))
    return keys
>>>>>>> Stashed changes
