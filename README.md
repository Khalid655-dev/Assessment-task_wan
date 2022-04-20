# Assessment-task_wan
# RESTful Application

### Scenario
You have been given a real world challenge to generate reports on registration of cars. Let’s
suppose a small startup wants to build this app which would help the end user to search and view
the reports generated. Let’s suppose you got the opportunity to join this startup as a backend
Intern. You must provide clear and complete documentation about how to run your program. You
should be able to handle different routes in your app. The following features Restful APIs
implementation is given to you as a first task to implement.


- Table of Content
[ToC]

### Requirements

#### Functional Requirements
Following are the functions which the application will be able to perform.
* **User signup /signin**
User shall be able to sign up with his/her credentials for the first time and then can login to use the app features.
* **Periodic Sync of Dataset:**
Using the URL provided above, make automated calls once a
day to retrieve and store data into a local relational database. You only need to maintain a
data set for the last 10 years i.e. 2012-2022. This operation should be performed as a
background task. Keep in mind that discovered data should only update & not overwrite
the current data stored. 
* **Search car based on year, model and make**
User shall be search specific car details based on year, make and model
* **Schema Validation**
The APIs should be able to properly validate input/output schemas.

#### Non-functional Requirements
Following are the non-functional requirements;
* **Security**
User password will be encrypted before storing in the database which cannot be understood if retrieved the data from database.
* **Performance**
The application should perform well and provide responsive messages on each operation.

### Detail Design and Architecture
The application include PostgreSQL database for development phase.
 
### Environment setup

#### **Step-1** Cloning repository

```
# clone porject
git clone https://github.com/Khalid655-dev/Assessment-task_wan.git

```
#### **Step-2** Python-vitual environment and dependencies installation

```
# create app-env python-virtual environment
python3 -m venv app-env

# to install the required packages
pip install -r requirements
```

#### **Step-3** Activate python-virtual environment (app-env)
```
# activate app-env
source app-env/bin/activate
```

#### **Run application
```

#run application
 pyhton app.py

```


Congratulations! 
