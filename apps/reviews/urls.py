from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^show$', views.show, name='reviewShow'),
	url(r'^createForm$', views.createForm, name='createReview'),
	url(r'^create.json$', views.create, name="create.json"),
	url(r'^retrive.json$', views.getData, name="retrive.json"),
]