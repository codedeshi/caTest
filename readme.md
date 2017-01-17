# Api:

# Posting reviews:
http://127.0.0.1:8000/create.json 
User can post reviews at this route. Following data is required to be sent as the post body:
title 		: 	Title for the blog
sating		:	Rating between 1-5
summary	:	Summary text for the review
company	: 	Company for which the user wants to submit the review
Authentication token need to be sent as a header:
token		:	 Authentication token

# Retrieving Reviews:
http://127.0.0.1:8000/retrive.json
User can retrieve only their reviews by sending a GET request to this link with the authentication token in the header.

# Admin view:
http://127.0.0.1:8000/admin
I have used Django’s default admin view to provide admin access to all reviews, users and companies.  
Username	: admin
Password	:P@ssw0rd
Additional admin users can of course be created using python manage.py createsuperuser.

# Web UI: 
http://127.0.0.1:8000/
I have also made a full website where the users can register and login and interactively submit reviews and look at their reviews. 
Authentication token is automatically generated for each user and can be viewed by the use on their profile page.
