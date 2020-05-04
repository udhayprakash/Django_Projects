Step 1: create virtual env and activate it 

    python -m pip install -U virtualenv
    virtualenv .venv
    .venv/script/activate 

Step 2: create requirements.txt and README.md files 
    
Step 3: Added modules in requirements.txt and install them.
    pip install -r requirements.txt

Step 4: Verifying the installations
        (.venv) ~python --version
        Python 3.8.2

        (.venv) ~python -m django --version
        3.0

Step 5: Start the Django Project 

        django-admin startproject mysite

    mysite/                 ====> Project directory 
        manage.py           ====> main file in project 
        mysite/
            __init__.py     ====> empty file for python packaging
            settings.py     ====>  Settings/configuration for this Django project
            urls.py         ====> routing the paths 
            asgi.py         ====> An entry-point for ASGI-compatible web servers to serve your project. 
            wsgi.py         ====> An entry-point for WSGI-compatible web servers to serve your project. 

Step 6: Start the development server 
        cd mysite
        python manage.py runserver 
        python manage.py runserver 8000
        python manage.py runserver 0:8000
        python manage.py runserver 0.0.0.0:8000
        python manage.py runserver 127.0.0.1:8000

        127.0.0.1 --> Loop back address - to hit the local server

Step 7: create an application with name 'polls'

        python manage.py startapp polls

        polls/
            __init__.py
            admin.py         =====> manages what to show in admin page for this app
            apps.py          =====> application config file
            migrations/      ====> Audit of all database changes 
                __init__.py
            models.py        =====> database tables and columns related
            tests.py         ====> units tests for views and APIs
            views.py         ===> Business object
Step 8: create polls/urls.py, Add routing to polls.views 
        Correspondingly add routing in project/urls.py to route to polls/urls.py

Step 9: In Settings.py, settings for sqlite database will come by default. 
    If we are interested in working with any other database, apart from sqlite, 
    we need to create the database first  and add its corresponding settings 
    in settings.py under DATABASES section.

Step 10: MOdifiy the time zone as per your business logic. It is UTC by default.
        TIME_ZONE = 'CST'

Step 11: In INSTALLED_APPS, we get by default, 
    django.contrib.admin        – The admin site. You’ll use it shortly.
    django.contrib.auth         – An authentication system.
    django.contrib.contenttypes – A framework for content types.
    django.contrib.sessions     – A session framework.
    django.contrib.messages     – A messaging framework.
    django.contrib.staticfiles  – A framework for managing static files.

Step 12: To migrations to get the default django tables
    python manage.py migrate

Step 13: Register the 'polls' applications, in settings.py
     INSTALLED_APPS += [    'polls.apps.PollsConfig',]

    Add db tables in polls/models.py

    To create the db migrations, 
        python manage.py makemigrations

    To see the status of db migrations, at project level, 
        python manage.py showmigrations

    To see the db commands corresponding to the migration changes, 
        python manage.py sqlmigrate  polls 0001
        

    To apply the changes to db, 
        python manage.py migrate


Step 14:To open the db shell, 
            python manage.py shell 
         

                from polls.models import Question, Choice
                Question.objects.all()

                from django.utils import timezone
                q = Question(question_text="What's new?", pub_date=timezone.now())
                q.save()
                
                Question.objects.all()


            In ORM, use .get() if you are sure that there is only one record. Else use .filter()
                Question.objects.filter(pub_date__year=current_year)


Django Execution Flow 

    http://127.0.0.1:8000/polls/

    Broswer <-> Project/Urls.py <-> polls/urls.py <-> polls/views.py 


    views 
        - function-based views 
        - class-based views 

step 15 : create html file under the location 
                polls/templates/polls/index.html

step 16: Jinja templating/Django Templating Language(DTL) in html 

            {% %} - expression tag 
            {{}} - processing tag 


step 17: Add a post form 
            CSRF - Cross Site Request Forgery 
            
            netflix.com 
                - Authentication (access credentials) - login 
                - AUthorization (level of access determination)
            
            pages 
                - page 1 - acess granted
                - page 2 - no permission given 
                - page 3 - no permission given

            django will sent a unique token everytime {csrf} tag is present. 
            It is be unique for each page, per each logged user

            public key - private key 

            django - db (private key)
                   - webpage (public key)

            MIDDLEWARE -     'django.middleware.csrf.CsrfViewMiddleware',

step 18: 
        converting function - based views to class based generic views
        - With class based views, with minimal code all will be done

Step 19:  Install ipython and go to shell to see the ipython interactive django shell 
            pip install ipython
            python manage.py shell 


        testing 
            - unittest 
            - pytest 
            - nosetest
            

-----------------
Opening shell in Jupyter notebook (https://davit.tech/django-jupyter-notebook/)
    pip install django jupyter ipython django-extensions

    Add 'django-extensions' in settings.py/INSTALLED_APPS

    python manage.py shell_plus --notebook

    