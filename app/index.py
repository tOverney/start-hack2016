import re
from random import shuffle
from uuid import uuid4

from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from newspaper import Article, ArticleException
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

from api import API
from api import LanguageTranslation
from api.base import ApiError
from news.search_related_news import SearchRelatedNews

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
    context = {}

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

    try:
        article = Article(url)
        article.download()
        article.parse()
    except ArticleException:
        return HttpResponseBadRequest()
    text = article.text
    source = TextBlob(text)
    if source.detect_language() == 'fr':
        source = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

    translated = LanguageTranslation().translate(text, dest_lang)
    keywords = selectKeywords(TextBlob(translated).noun_phrases, 4)

    market = languagesBing[dest_lang]

    relatedArticles = SearchRelatedNews().get(keywords, market)
    relatedArticles = [{'title': article.title,
                        'text': article.text,
                        'url': article.url,
                        'nouns': TextBlob(article.text).noun_phrases,
                        'image': article.top_img if article.top_img else '/app/static/images/defaultpaper.jpg',
                        } for article in relatedArticles]

    for a in relatedArticles:
        acc = []
        for noun in a['nouns']:
            if isinstance(noun, list):
                pass
                #shuffle(noun)
                #acc += noun[0]
            else:
                acc.append(noun)
        a['nouns'] = acc
        print(a['nouns'])
        for noun in a['nouns']:
            a['text'] = a['text'].replace(" " + noun + " ", " <b>" + noun + "</b> ")

    context = {'title': article.title,
               'author': (" % ").join(article.authors), 'text': text,
               'transtxt': translated, 'nouns': TextBlob(text).noun_phrases,
               'transnouns': TextBlob(translated).noun_phrases, 'related': relatedArticles}

    context['transnouns'] = [noun if ' ' not in noun
                             else noun.split(' ')
                             for noun in context['transnouns']]

    context['videos'] = SearchRelatedNews().getVideos(keywords, market)

    for noun in context['transnouns']:
        if isinstance(noun, list):
            shuffle(noun)

    if request.is_ajax():
        t = loader.select_template(["articles.html"])
        return HttpResponse(t.render(context))

    return render(request, 'app/decomposed.html', context)


@csrf_exempt
def concept_info(request):
    if 'concept' not in request.POST:
        return HttpResponseBadRequest('no "concept+ in request')

    concept = request.POST['concept']
    concept_en = API.language_translation.translate(concept, dest_lang='en')
    try:
        ret = API.text_insight.concepts(concept_en)
    except ApiError:
        return HttpResponseBadRequest("no such concept")
    return render(request, 'app/decomposed.html', ret.__dict__)


def contact(request):
    return render(request, 'app/contact.html', {})


def selectKeywords(words, nb):
    keys = []
    for i in range(0, 3):
        keys.append(words.pop(i))
    return keys

@csrf_exempt
def audio(request):
    if request.POST:
        text = request.POST['text']
        audiodata = API.text_to_speech.synthesize(text)

        uuid = str(uuid4())
        with open(uuid, 'wb') as out:
            out.write(audiodata)

        return HttpResponse(uuid)
    else:
        response = HttpResponse(content_type='audio/x-wav')
        uuid = request.GET['audio_id']

        with open(uuid, 'rb') as file:
            response.write(file.read())

        return response
