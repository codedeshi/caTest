from __future__ import unicode_literals
from django.db import models
from ..users.models import User
# Create your models here.
class ReviewManager(models.Manager):
	def getData(self, post_data):
		pass

	def postData(self,post_data,token,ip):
		errors =[]
		if len(post_data['title'])==0:
			errors.append('Title cannot be blank')
		if len(post_data['title'])>64:
			errors.append('Title cannot be more than 64 Characters')
		if len(post_data['company'])==0:
			errors.append('Company cannot be blank')
		if len(post_data['summary'])==0:
			errors.append('Summary cannot be blank')
		if len(post_data['summary'])>10000:
			errors.append('Summary cannot be more than 10000 characters')
		if errors:
			return {'errors':errors}

		else:
			try:
				user = User.objects.get(auth_Token=token)
			except:
				return {'errors':'unauthorized user'}
				
			try:
				company = Company.objects.get(company_name=post_data['company'])
			except:
				company = Company.objects.create(company_name=post_data['company'])
			
			review = self.create(
				title = post_data['title'],
				company = company,
				user = user,
				rating = post_data['rating'],
				summary = post_data['summary'],
				ip = ip
			)
			return {'errors':errors, 'review':review}


class Company(models.Model):
	company_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.company_name

class Review(models.Model):
	title = models.CharField(max_length=64)
	rating = models.IntegerField(blank=False)
	summary = models.TextField(max_length=10000)
	ip = models.GenericIPAddressField()
	company = models.ForeignKey(Company)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = ReviewManager()

	def __str__(self):
		return self.title