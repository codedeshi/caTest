from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.

def index(request):
	return render(request,'users/index.html')
	
def show(request):
	if 'user' in request.session:
		return render(request,'users/show.html')
	else:
		return redirect('/')

def registration(request):
	reg = User.objects.register(request.POST)
	if len(reg['errors']) > 0:
		for message in reg['errors']:
			messages.add_message(request,messages.INFO,message)
		return redirect('/')
	else:
		request.session['user'] = {
			'name': reg['user'].name,
			'email': reg['user'].email,
			'auth_token': str(reg['user'].auth_Token),
			'id': reg['user'].id
		}
		return redirect('show')

def login(request):
	log = User.objects.login(request.POST)
	if log[0] == True:
		request.session['user'] = {
			'name': log[1].name,
			'email': log[1].email,
			'auth_token': log[1].auth_Token,
			'id': log[1].id
		}
		return redirect('show')
	else:
		messages.add_message(request,messages.INFO,log[1][0])
	return redirect('/')

def logout(request):
	del request.session['user']
	return redirect('/')