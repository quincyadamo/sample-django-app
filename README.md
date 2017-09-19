# Django Sample App

Description:
This is an application that allows the logged user to add his travel plans and be able to join other users travel plans.
This includes normal authentication with server side validations. Once logged in a user can see travel plans that have either been created or joined by the user. A user has the ability to join other users' travel plans and newly added travel plan should appear on logged user's trip schedule table. (Note this was deployed to an EC2 instance).

![Example Image](https://s3.us-east-2.amazonaws.com/qadamo-images/travelbuddy.png "Example Image")

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
