from django.shortcuts import render, HttpResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.
import json
#@cache_page(600, key_prefix='index', cache='default')
def index(request):

    return HttpResponse(json.dumps({'msg': 'fucok'}))