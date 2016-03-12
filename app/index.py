from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.http import JsonResponse
from newspaper import Article
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from django.views.decorators.csrf import csrf_exempt
from api import LanguageTranslation, Api


def index(request):
    context = {}
    return render(request, 'app/index.html', context)


def result(request):
    url = ""
    try:
      url = request.POST['url']
    except KeyError:
      url = ""

    if url == "":
        raise Http404("No url given!")

    article = Article(url)
    article.download()
    article.parse()
    text = article.text
    source = TextBlob(text)
    if source.detect_language() == 'fr':
        source = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

    translated = LanguageTranslation().translate(text)
    context = {'title': article.title,
        'author': (" % ").join(article.authors), 'text': text,
        'transtxt': translated, 'nouns': source.noun_phrases,
               'transnouns': TextBlob(translated).noun_phrases}
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
