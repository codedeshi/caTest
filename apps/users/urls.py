from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^registration$',views.registration,name='registration'),
	url(r'^login$',views.login, name='login'),
	url(r'^show$',views.show, name='show'),
	url(r'^logout$',views.logout, name='logout'),
]