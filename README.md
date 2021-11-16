# YogaMembership
A Form for storing details of User into the database 

To run locally, do the usual:

1. First Clone the Repository.

2. Install all the necessary files,libraries from requirements.txt
    pip install -r requirements.txt

3. After installing this you can use the cmd in terminal  
    python manage.py runserver
  to run the webapp on localhost
 
4. To access the database you can create a user by using

python manage.py createsuperuser

or A prexisting superuser also exists 
with Username: admin  
     Password:12345@user
     
5. To access the admin panel just type http://127.0.0.1:8000/admin after starting the server.

6. Also to create a new databse you should apply cmd
    python manage.py makemigrations
    python manage.py migrate
    
Can refer to,Detailed explanation for how to run a cloned repository from github - https://alicecampkin.medium.com/setting-up-a-forked-django-project-53d5939b7e9e
