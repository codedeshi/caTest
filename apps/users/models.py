from __future__ import unicode_literals
from django.db import models
import uuid, bcrypt, random
# Create your models here.
class UserManager(models.Manager):
	def register(self, post_data):
		errors = []
		user = User.objects.filter(email = post_data['email']).count()
		if len(post_data['name']) == 0:
			errors.append('Name cannot be blank')
		if len(post_data['email']) == 0:
			errors.append('Email cannot be blank')
		if user>0:
			errors.append('Email already registered')
		if post_data['password'] != post_data['confirm']:
			errors.append('Password and Confirm Password should match')
		if errors:
			return {'errors':errors}
		else:
			hashed_pw = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
			new_user = self.create(name=post_data['name'],email=post_data['email'], password=hashed_pw)
			return {'errors':errors, 'user':new_user}
		pass
	def login(self, post_data):
		try:
			user = User.objects.get(email=post_data['email'])
			password = post_data['password'].encode()
			if bcrypt.hashpw(password, user.password.encode())==user.password.encode():
				return (True,user)
		except:
			pass
		return (False, ["Email/password don't match."])	

	
class User(models.Model):
	name = models.CharField(max_length=45)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=100)
	auth_Token = models.CharField(max_length=100,default=uuid.uuid4 )	
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

	def __str__(self):
		return self.name