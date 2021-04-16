from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from home.block import *
from home.Blockchain import *
from django.contrib import messages
from collections import Counter
import json

from django.conf import settings
# Create your views here.
from home.models import Student
bc = Blockchain()



def home(request):
    username = request.user.username

    if username == 'student_common_login':
      return render(request, 'home2.html')
    else:
          m= ""
          data = []

          for b in range(bc.get_length()):
              d = {}
              block = bc.get_block(b)
              d['student_id'] =block.student_id
              d['height'] = block.height
              d['timestamp'] = block.timestamp
              d['first_name'] = block.first_name
              d['last_name'] =block.last_name
              d['tuitionfee'] =block.tuition_fee
              d['messfee'] =block.mess_fee
              d['hostelfee'] =block.hostel_fee
              d['course'] = block.course
              d['status'] = block.status
              if (d['status'] != 0):
                data.append(d)
          k = [x['student_id'] for x in data]

          new_vals = []

          for i in Counter(k):
              all = [x for x in data if x['student_id'] == i]
              new_vals.append(max(all, key=lambda x: x['timestamp']))
          return  render(request,'home.html',{'data':new_vals})
def change_status(request):
    if request.method == "GET":
        id = request.GET['id']
        action = request.GET['action']
        if action == '1':
            temp  = bc.get_block(int(id))
            temp.status = "Approved"
            bc.add_block(temp)
        else:
            temp = bc.get_block(int(id))
            temp.status = "Rejected"
            bc.add_block(temp)

        print(bc)
        print(action)
        m = ""
        data = []

        for b in range(bc.get_length()):
            d = {}
            block = bc.get_block(b)
            d['student_id'] = block.student_id
            d['height'] = block.height
            d['timestamp'] = block.timestamp
            d['first_name'] = block.first_name
            d['last_name'] = block.last_name
            d['tuitionfee'] = block.tuition_fee
            d['messfee'] = block.mess_fee
            d['hostelfee'] = block.hostel_fee
            d['course'] = block.course
            d['status'] = block.status
            if (d['status'] != 0):
                data.append(d)
        k = [x['student_id'] for x in data]

        new_vals = []

        for i in Counter(k):
            all = [x for x in data if x['student_id'] == i]
            new_vals.append(max(all, key=lambda x: x['timestamp']))
        return render(request, 'home.html', {'data': new_vals})
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
    f = open("/Users/Dev/Documents/saved_chain_state.txt", "w")
    f.write(str(bc))
    f.close()
    messages.info(request, 'done')
    return render(request, 'home2.html')

def view(request):
    m= ""
    data = []

    for b in range(bc.get_length()):
        d = {}
        block = bc.get_block(b)
        d['student_id'] =block.student_id
        d['height'] = block.height
        d['timestamp'] = block.timestamp
        d['first_name'] = block.first_name
        d['last_name'] =block.last_name
        d['tuitionfee'] =block.tuition_fee
        d['messfee'] =block.mess_fee
        d['hostelfee'] =block.hostel_fee
        d['course'] = block.course
        d['status'] = block.status
        if (d['status'] != 0):
          data.append(d)
    k = [x['student_id'] for x in data]

    new_vals = []

    for i in Counter(k):
        all = [x for x in data if x['student_id'] == i]
        new_vals.append(max(all, key=lambda x: x['timestamp']))
    return  render(request,'view.html',{'data':new_vals})

def block(request):
    data =  str(bc)


    return  render(request,'block.html',{'data':data})


