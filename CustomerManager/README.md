## Customer Manager Web Application
### Application Details
This application will have to have the following features:
    
    - Displaying a list of customers
    - Creating a customer
    - Changing a customer
    - Deleting a customer

A customer must have the following fields:
    
    - Name
    - First name
    - Telephone number
    - Date of contact

### Set-up Procedure
This project was created using Python 3.8 and Django 2.2.

__Step 1:__ Install python 3.8 and the python modules pipenv and Django

        pip install -U pipenv

__Step 2:__ Create virtual environment using pipenv and install modules
        
        pipenv start
        pipenv install django djangorestframwork
        pipenv install --dev pylint
        pipenv shell

__Step 3:__ Start the project 
        
        cd CustomerManager 
        python manage.py runserver
        
__Step 4:__ open the link http://127.0.0.1:8000/ in browser


## Usage
Testing 
        
        python manage.py test 
        
-----------------------------------------------------------------------------------------------

In addition, following were done
    - Validation rules for field entry
    - Sorting on the customer list, based on their `name` field.

