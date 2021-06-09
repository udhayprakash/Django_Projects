Step 1: Installing basic modules 
    pip install -U pip setuptools pipenv 

Step 2: creating virtualenvironment & 
    installing modules
    
    pipenv install django~=2.2
    pipenv install ipylint --dev

Step 3: Activating virtual environment
    pipenv shell 
    
    Verification of installation
        python --version 
        django-admin --version 

Django Project 

Step 4: create django project 
    django-admin startproject locallibrary

    create an application 
        Method 1: 
            django-admin startapp catalog 

        Method 2:
            cd locallibrary
            python manage.py startapp catalog
    
    Register the application, into the project 
        Add 'catalog' in settings.py/INSTALLED_APPS

Step 5: creating a MySQL database and adding in settings.py 
    DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # }
        'default': {
            'AUTOCOMMIT': True,
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'locallibrary',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4'
            }
        }
    }

    python manage.py makemigrations
    python manage.py showmigrations
    python manage.py migrate 
    python manage.py showmigrations
    

    admin user 
        username: admin 
        password: admin123#

Step 5:
    After creating db tables in models, 
    register in admin.py to see them in admin page 

            a1 a2 a3 a4 a5
            2  3   1 4  a
                1    d
                1    d
                2    a
                2    
                2

            (('a', 'alive'), ('d', 'dead'))
            CharField()

            DB Normalization - dividing db tables, columnwise
            Db Sharding      - dividing db tables, row wise
                            - 

Step 6: 



Browser  --> project server  --> web server(Apache/ Guni) --> app server(django) <>
                                   static - images, js, 
                                   

    CRUD 
        C - create  
        R - retrieve   
                All           -> ListView
                single record -> DetailView
        U - update 
        D - delete 


    generic.ListView
        - generically "the_model_name_list"
        - For model 'Book', -> book_list
            - /application_name/the_model_name_list.html
            - catalog/book_list.html


{% %}
{# #}
{{ value | filter}}

''.join(values)
['a', 'b', 'c'] -> 'abc'


Step 7: 

        accounts/ login/ [name='login']
        accounts/ logout/ [name='logout']
        accounts/ password_change/ [name='password_change']
        accounts/ password_change/done/ [name='password_change_done']
        accounts/ password_reset/ [name='password_reset']
        accounts/ password_reset/done/ [name='password_reset_done']
        accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
        accounts/ reset/done/ [name='password_reset_complete']


        # Add Django site authentication urls (for login, logout, password management)

        urlpatterns += [
            path('accounts/', include('django.contrib.auth.urls')),
        ]