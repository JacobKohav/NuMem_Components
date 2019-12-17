# NuMem_Components
CSCI3308_Project_Components

This site's components are stored in a folder called `training_site`.
Within this folder are a number of folders and files used by Django.
Three of these folders "home", "users" and "training_site" are Django 'apps'.
Additionally there is a "fourth app" `django_quiz` which is a 3rd party Django app that we've integrated for the quiz functionality. That app is installed by adding its git url to our `requirements.txt`
Below is a brief list of some of the files involved.
* `training_site` - this folder contains files relevant to the entire Django project.
	* `settings.py` - contains the global settings for the Django project
	* `urls.py` - manages the routing of urls to the other Django apps (eg. '/' just leads to the hompage.)
	* `wsgi.py` - this file is called by the actual web server (in our case `gunicorn`) to get information about the web application.
* `home` - this app contains files pertinent to the homepage.
	* `models.py` - the home app's model file is where we implemented the ResourceLink model for linking to external sites.
* `users` - this app handles user registrations and logins.

## Deployment:
This app has been deployed on heroku.

See the [heroku_dev](https://github.com/JacobKohav/NuMem_Components/tree/heroku_dev) branch for heroku specific files.

Heroku acts as an upstream repository, where after any push Heroko will attempt to run your application based on a `Procfile`
Heroku detects that your application is python based if there is a `requirements.txt`.
It will automatically install any requirements from this file.
Because Django is python based, other than installing these requirements there is nothing to build, everything is done at runtime.
