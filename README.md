# NuMem_Components
CSCI3308_Project_Components

    - Describe repo organization/structure
    - Describe how to build/run/test/etc code
    - If using a Continuous Integration system, provide a link to the CI status page


The files are ordered by the application/usage each pertains to the website. For instance, There is a home file, and within that home file is a template file that has a sub-home file within it. This file specifically pertains to the html and css styling of the homepage and resource details. In the /training_site/home file is the python files also pertaining the home page and initial set up of the site including a models.py, views.py, and urls.py pages. These pages are essential to the site correctly linking and running. You will see another file name media which houses the images used in the database. Additionally, there is a folder only pertaining to the creation of users labeled 'acocunts'. All the neccessary code revolving around adding users to the site will be located within that file. 


Running and testing the code involves the usage of the web framework Django. In order to use Django, one must make sure that they have downlaoded the neccessary version of python, as well as django itself. Without these, this site will not load correctly. Furthermore, they will have to be able to run a local server, or host using a platform such as Heroku (see link below). In order to run a Django server on one's computer, they must use the command (or one similar depending on your OS system) 'python3 manage.py runserver'. This, if you have no errors, will hose the site on your local server. If there are any errors with the code, an error message will pop up in your terminal, as well as on the web browser when you try to run it. 

