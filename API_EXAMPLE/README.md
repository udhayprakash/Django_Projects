
    django-admin startproject api_example
    cd api_example
    python manage.py migrate
    python manage.py createsuperuser --user admin --email admin@domain.com
    password: Test123#
    python manage.py startapp languages 

    In INSTALLED_APPS, 
    add 'rest_framwork'
    add languages