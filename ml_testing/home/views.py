from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

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
    global bc
    b1 = Block(0, 0, "lol", 1, post_data['studentId'][0], post_data['firstname'][0],  post_data['lastname'][0], post_data['tuitionfee'][0], post_data['messfee'][0], post_data['hostelfee'][0], post_data['course'][0], "Initial")
    print(bc.get_block(0))
    bc.add_block(b1)
    print(bc.get_block(1))
    f = open("/Users/nmary/Documents/saved_chain_state.txt", "w")
    f.write(str(bc))
    f.close()
    return render(request, 'home2.html')


