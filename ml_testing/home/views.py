from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
import wikipedia
from nltk import ngrams


import json

from django.conf import settings
# Create your views here.

content = ""
bigrams_list  = []
trigrams_list  = []
quadrigrams_list = []
model_ted = ''
def home(request):
    username = request.user.username
    if username == 'student_common_login':
      return render(request, 'home2.html')
    else:
      return render(request, 'home.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
