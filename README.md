# Django Sample App

Description:

The current `requirements.txt` file includes:

```
bcrypt==3.1.3
cffi==1.10.0
Django==1.10
pycparser==2.18
six==1.10.0

```

## Installation & Activation:

### 1. virtualenv 
Simply create and activiate a virtual environment to run this project. In the Terminal, run: 
`$ virtualenv djangoEnv` (to create)
`$ source djangoEnv/bin/activate` (to activate)

### 2. Install Requirements
Right there, you will find the *requirements.txt* file that has all the great debugging tools, django helpers and some other cool stuff. To install them, simply type:
`$ pip install -r requirements.txt`

### 3. Initialize the database
Migration, run:
`$ pyhon manage.py migrate`

### 4. Ready to activate the project? Go!
From the Terminal, run: 
`$ python manage.py runserver`
