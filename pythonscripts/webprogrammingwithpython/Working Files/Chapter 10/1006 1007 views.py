from django.http import HttpResponse
from films.models import Films
from django.template import Context, loader, RequestContext
from mysite.films.forms import AddForm
from django.shortcuts import render_to_response
import sqlite3 as db

def index(request):
   film_list = Films.objects.all()
   t = loader.get_template('films/index.html')
   c = Context({'film_list': film_list})
   return HttpResponse(t.render(c))

def add(request):
   form = AddForm(request.POST)
   write_to_database(request.POST)

   return render_to_response('add.html', {
      'form': form}, context_instance=
      RequestContext(request))

