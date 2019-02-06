# Item-Catalog

## Project Overview
This project focuses mainly on CRUD(Create, Retrieve, Update, Delete) operations performed on database using python. In python, we use Flask
framework to build a web application and SQlAlchemy database to perform
CRUD operations.

### Required Software for the Project:
* **Virtual Box (https://www.virtualbox.org/)**
* **Vagrant (https://www.vagrantup.com/)**
* **Python (https://www.python.org/)**

### Technologies Used
* **HTML**
* **CSS**
* **Python** 
* **Flask (Python web development framework)**
* **SQLAlchemy database**
* **Udacity Vagrant File (https://github.com/udacity/fullstack-nanodegree-vm)**

To install 'Flask' and 'SQLAlchemy' database use the following commands:

`$ pip3 install Flask`

`$ pip3 install sqlalchemy`

### API's used
* **Google OAuth2 API (For Authentication and Authorization Purpose.)**

Firstly install Virtual Box, Vagrant and Python.
Open your project folder and add and intialize the vagrant box by using the following commands:

`$ vagrant box add ubuntu/trusty64`

`$ vagrant init ubuntu/trusty64`

Now use the following command to bring up the virtual machine:

`$ vagrant up`

Connect to the virtual machine by using the following command:

`$ vagrant ssh`

Now a terminal opens and following is displayed:

**vagrant@vagrant-ubuntu-trusty-64:~$**

Navigate to vagrant directory and create the following files:
* **database_setup.py**
* **list_of_games.py**
* **final_project.py**

### database_setup.py
This file contains configuration related to databases like tables 
and their columns. By running this file, a database and their corresponding tables and columns will be created and a file **'pcgames.db'** is generated.

Use the following command to run the file

`$ python3 database_setup.py` 

### list_of_games.py
We will be using this to create and dump dummy values into the database.
By running this file dummy values are dumped into 'pcgames.db' file which
is our database file.

Use the following command to run the file

`$ python3 list_of_games.py`

### final_project.py
This file contains the code related to database CRUD operations and 
code for authorizing and authenticating a user. The user will be able to
login and add, edit, update, delete his own items. But he cannot modify
the items added by another user. 

For authentication and authorization purpose we will be 'Google OAuth2 API' service provided by Google.

Use the following command to run the file

`$ python3 final_project.py`

To see the ouput, open your browser and goto the following URL:

`http://localhost:7000`

### This project requires an internet connection as styles and images used are from different sources of internet.
