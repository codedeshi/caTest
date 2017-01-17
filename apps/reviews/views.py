from django.shortcuts import render, redirect
from .models import Review
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers

def show(request):
	if 'user' in request.session:
		userReviews = Review.objects.filter(user__auth_Token=request.session['user']['auth_token'])
		return render(request,"reviews/show.html",{'reviews':userReviews})
	else:
		return redirect('/')

def getData(request):
	token = request.META.get('HTTP_TOKEN')
	data = Review.objects.filter(user__auth_Token=token)
	response = []
	for i in data:
		response.append({
			'title': i.title,
			'company':i.company.company_name,
			'ratng': i.rating,
			'summary': i.summary,
			'user': i.user.name,
			'submitted_date': i.created_at,
			'ip': i.ip
		})
	return JsonResponse(response, safe=False) 

def createForm(request):
	review = create(request)
	if 'errors' in review:
		for message in review['errors']:
			messages.add_message(request,messages.INFO,message)
		return redirect("reviewShow")
	else:
		return redirect("reviewShow")

@csrf_exempt
def create(request):
	token = None;
	if 'user' in request.session:
		token = request.session['user']['auth_token']
	if token == None:
		token = request.META.get('HTTP_TOKEN')
	review = Review.objects.postData(request.POST, token, get_client_ip(request))
	if len(review['errors']) > 0:
		return JsonResponse({'errors': review['errors']})
	else:
		response = {
			'id': review["review"].id,
			'title': review["review"].title,
			'ratng': review["review"].rating,
			'summary': review["review"].summary
		}
		return JsonResponse(response, safe=False)

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
			ip = x_forwarded_for.split(',')[-1].strip()
	else:
			ip = request.META.get('REMOTE_ADDR')
	return ip