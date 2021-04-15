from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
import wikipedia
from nltk import ngrams




from home.block import *
from home.Blockchain import *


import json

from django.conf import settings
# Create your views here.

bc = Blockchain()



def home(request):
    username = request.user.username
    if username == 'student_common_login':
      return render(request, 'home2.html')
    else:
      return render(request, 'home.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    post_data = dict(request.POST.lists())
    post_data.pop('csrfmiddlewaretoken', None)
    print(post_data['firstname'][0])
    global bc
    b1 = Block(0, 0, "lol", 1, "neeuse", "neenu", "mary", "2000", "200", "1000", "Initial")
    b2 = Block(0, 0, "test", 1, "dinn", "divya", "test", "9000", "400", "1000", "Initial")

    print(bc.get_block(0))
    bc.add_block(b1)
    print(bc.get_block(1))
    bc.add_block(b2)
    print(bc.get_block(2))
    f = open("/Users/dev/Documents/dinak/mtech/blockchain/project_final/saved_chain_state.txt", "w")
    f.write(str(bc))
    f.close()
    return render(request, 'home2.html')


