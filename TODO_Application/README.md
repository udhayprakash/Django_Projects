## TODO Web Application
This tool is used to manage the TODO tasks of any individual.

### Application Details
This application will have to have the following features:
    
    - User able to create a new task
    - User able to edit an existing task
    - User able to archive tasks
    - User able to permanently delete tasks
    - Two separate tabs, one containing current tasks and the other archived tasks
    - Written and structured code as if its for a production setting
    - Ability to create a task and set a date for completion
    - Ability to search for a task based on its set completion date

Pending Features

    - Writing test-cases is strongly encouraged

A Task must have the following fields:
    
    - Title
    - Description
    - Target Date
    - Task Status

### Set-up Procedure
This project was created using Python 3.8 and Django 2.1.

__Step 1:__ Install python 3.8 and the python modules pipenv and Django

        pip install -U pipenv

__Step 2:__ Create virtual environment using pipenv and install modules
        
        pipenv start
        pipenv install django djangorestframwork
        pipenv install --dev pylint
        pipenv shell

__Step 3:__ Start the project 
        
        cd TodoProject 
        python manage.py runserver
        
__Step 4:__ open the link http://127.0.0.1:8000/ in browser


## Usage
Testing 
        
        python manage.py test 
