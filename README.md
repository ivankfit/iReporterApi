# iReporterApi
[![Build Status](https://travis-ci.com/ivankfit/iReporterApi.svg?branch=starter)](https://travis-ci.com/ivankfit/iReporterApi)
[![Coverage Status](https://coveralls.io/repos/github/ivankfit/iReporterApi/badge.svg?branch=develop)](https://coveralls.io/github/ivankfit/iReporterApi?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
# Description
### This Project helps people to report corruption related incidents and also call for goverrnment intervention incase of emergencies in the communities.

## Features
1. A user can create an account
2. A user can login
3. A user can upload an image
4. A user can upload a vedio
5. A user can create a red flag record
6. A user can create an intervetion
7. A user can edit their red flags or intervetion
8. A user can add geolocation
9. A user can change their geolocation
10. Admin can chage the status of a record

# Installation

install python3

Create a virtual environment for the project.

``
`
virtualenv "name of the virtual environment"
```
Then Activate the venv using:
```
source "name of the virtual environment / Scripts/Activate
```

* 
Navigate to the application directory:

```
cd iReporterApi
```

*
 Create a virtual environment to install the
application in. 
You could install virtualenv and virtualenvwrapper.

Within your virtual environment,
 install the application package dependencies with:

 `pip install - r requirements.txt`

To deploy on Heroku
  install gunicorn and add it in requirements.txt by running pip freeze > requirements.txt


* 
Run the application with:

```
python run.py
```
* 
for tests and coverage run in terminal using:

```
pytest --cov
```

# 
URL endpoints

| URL Endpoint | HTTP Methods | Output |
| -------- | ------------- | --------- |
|'api/v1/redflags' | 'POST' | Creates a new Redflag|
|api/v1/redflags/'<int: id >' | 'GET' | gets aredflag|
|'api/v1/users'| `GET` | Retrieve all users |
|'api/v1/users' | 'POST' | Creates a new User |
|'api/v1/redflags/'<int:id>' | 'PUT' | Updates a redflagd|
|'api/v1/redflags/<int:id>/comment' | 'PATCH' | Update a comment record in a red flag |
|'api/v1/redflags/<int:id>/location' | 'PATCH' | Update a location record in a red flag |
|`api/v1/redflags/<int:id>` | `DELETE` | Delete a Redflags |


# Example New User body
```
Example body
{
    "firstname": "tweheyo",
    "lastname": "ivan",
    "othernames": "kfit",
    "email": "tweheyoivan@gmail.com",
    "phone_number": "788777777",
    "username": "van",
    "registered": "dateandtime",
    "is_admin": "true"

}
```

# Example New RedFlag Body
```
{
    "comment": "Asked for abribe",
    "created_by": 1,
    "created_on": "Thu, 17 Jan 2019 10:13:51 GMT",
    "id": 3,

    "location": "mbarara",
    "status": "draft",
    "type": "redflag"
}
```
# Deployement
[Heroku Deployement](https://iwillreport.herokuapp.com/)

# Author
[Ivan Kfit](https://github.com/ivankfit)


## My useful links
1. Heroku link https://iwillreport.herokuapp.com/
2. Pivatal Tracker Board link https://www.pivotaltracker.com/n/projects/2228054




