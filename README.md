
<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/tasks.JPG" style="width:550px">



# Personal task manager 

## About 
The project is a tool to get structure in your life and plan your activities. 
So i decided to do a personal task manager were your can structure your activities. 

## Creating 
After making the mini project i wanted to do my own way of a task manager and add a different structure to it. 

I wanted to build something that is suitabele for my life and what i need to get a good structure and overview of my to do tasks. 

I started by watching the mini project structure again bit by bit to get a good understanding of how to build it and how i could connect the project to the database. 

First off i did almost the same ground coding as the mini project with a few different tasks input. And also a different type of structure of the different pages. 

The project is only a personal task manager and i only want the user to se its own tasks and not everyone elses tasks. 

## Preparation


## UX 

### Project goald 

* Making a full-stack site that uses HTML, CSS, JavaScript, Python+Flask and MongoDB.
* Creating a website that is easy to understand and work with.
* Creating a website were you can have a good structure and a bucketlist. 
* The user of the site can ute CRUD for the tasks and bucketlist.


### User Goals
*	As a user type, i want to be able to register and start an account. 
*	As a user i want to be able to visit the site on every device so that i can access the site on my mobile or tablet. 
*	As a user type, i want the site to be easely to navigate on. 
*	AS a user type, i want to be able to search for a task 
*	As a user type, i want to see how many tasks i have 
*	As a user type, i want to see how many tasks i have completed 
*	As a user type, i want to be able to add tasks
*	As a user type, i want to be able to edit and delete tasks
*	As a user type, i want to be able to see all the tasks that i have and also by category. 

 ### Site Owner Goals 
*	As the owner i want to build a site that is easy to understand and use
*	As the owner i want to build a site that looks appealing 
*	As the owner i want to build a site that is responsive and works on different screens.
* As the owner i want to build a site that have a good structure


 ### User Requirements 
*	Having a good structure. 
*	Easy to navigate 
*	Visually appealing. 
*	Footer with icons and locations and contact information.
*	Contact form
*	A about section 
*	Add/edit tasks 
* Responsive 
* Se completed tasks
* Se all the tasks that the user have


## Features 

### Design Choices 

#### Home page
* A attractive and simple layout that is easy to understand.
* Log in / register navbar 
<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/home.JPG" style="width:200px">

##### Log in/ register page
* People can create a new account on the web registration form. 
* People can login with their existing accounts.
* Users can easely log in or out. 
* Flash message If the username is not registered or if the password is incorrect an error message will appear.

<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/registrer.JPG" style="width:100px">
<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/signin.JPG" style="width:100px">

#### Add task 

* Form: The whole page is a form with different input types. The form used and all the input fields inside the form have been taken from Materialize.
* tasks and bucketlist items can be created, read, updated and deleted (CRUD) by the users.


<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/addtasks.JPG" style="width:200px">

#### Se all tasks 

* Delete button: This button is to the user and will allow the user to remove the task och bucketlist. 

* Edit button: This button is to the user and will allow the user to edit the tack or bucketlist item by redirecting the user to the "edit task or bucketlist" page.
* 
<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/tasks.JPG" style="width:200px">

#### Manage Categorys 

* User can see all categorys
* User can edit/delete categorys
<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/addcategory.JPG" style="width:200px">

#### Bucketlist


#### Add Bucketlist 

* Form: The whole page is a form with different input types. The form used and all the input fields inside the form have been taken from Materialize.


### Features that is implemented:

The website uses Materialize CSS on following:

* Navbar 
* Mobile Sidenav 
* Form (to register and log in)
* Hero image (on the home page)
* Users can login and register to add or edit tasks
* Users can delete a task
* Users can edit a task
* Users can pick both start and due date to a task 
* Site linked to Heroku
* Site linked to Mongodb database
* Login/register
* CRUD

### Features left to implement
* Posibility to sort all tasks in one category 
* Posibility to se att the completed tasks. 

### Technologies used 

#### Languages:

* HTML5
  * HTML was used for the main structure of the website.

* CSS3
  * CSS was used to style and change sizes. 

* Javascript
  * Was used on the dynamic functions on the site 

* Python3 
  * Used as Back-End programming language

#### Frameworks, libraies and other 

* Materialize 
  * Materialize is used to design the framework. 

* Pymongo 
  * Used as Python's API for MongoDB intergration.

* Flask
  * Rendering template, URIs Requests and the flash messages.

* BSON
  * for accessing the data in MongoDB and to access IDs. 

* Werkzeug
   * Werkzeug is used for the User to hash password when registering to the site and encrypting on MongoDB.

* MongoDB 
   * MongoDB is used to store all data for the website.

* Heroku
  * Used for hosting my full stack app.

* Jquery
  *  JQuery was used for materialize features that needed javascript.

* Gitpod 
  * The Gitpod is used to develop the project. 

* Git 
  * The Git was used for cersion control to commit and push to github. 

* Github
  * The Github is used to develop the project.   



## Testing

* HTML: I have used https://validator.w3.org/ in order to validate the HTML code.

* CSS: I have used https://jigsaw.w3.org/css-validator/ in order to validate the CSS code.

* JavaScript: I have used https://jshint.com/ in order to check the JavaScript code.


#### User story Testing 
* User want to be able so register to the page. 
  * The user can navigate to the Register page and type in a new username and a password. 

* User want to log in on the page
  * After register to the page the user can click on log in in type in the username and password and will be logged in. 
  The User will then be loggen in and get to the profile page. New items will be shown in the navbar such as Tasks,Profile, New task, Manage task and log out. 

* User want to see the tasks 
    * The user can now click on the task item in the navbar to get to the tasks site and see all the tasks that the user have.

* User want to edit or mark a task as done.
  * The user can easely edit and mark the task as done in the tasks meny, Under each tasks the two buttons edit and done shows. 
    The done button takes away the task. And the edit button takes you to an other site were your can make changes to your current task. 

* User want to make a new task
  * The user can click on New task, And start adding category, task name and task description, start date and due date. Then click on add task and the task will be added to the Tasks site. 

* User want to manage Categories 
  * User can click on the Manage Categories in the navbar to see all the categorys and be able to edit or delete a category. 

* User want to log out 
  * User can click on the log out item in the navbar. 

#### General testing 

* All links on the site works well and are being opened with success. 
* The page/linkes such as add task, manage categories and profile will will only be shown when the user is logged in. 
* Register with the user mysans with success. 
* Register with the user test1 and it worked with success, the new user was added to the database and was logged in. 
* Test to start a new task with the new user and it worked well. 
* Tested to delete a task and that also worked well. 
* Tested to manage categories and add a category and that worked well. 
* Tested to edit a category and that worked well. 
* Tested to delete a category and that worked well. 

#### Testing in different browsers

| Tested funcitons  | Sections tested |
| ------------- | ------------- |
| Responsiveness  | Login  |
| Content Cell  | Content Cell  |

##### Testing against the user stories 



##### Responsiv test
In this test i used the Google inspect tool 
The following devices were used: 

* Ipad 
  * When testing the responsivness for the Ipad, The navbar adjust and poped up at the right and the tasks also adjusted fine. 
  All the different sizes worked fine. 
* Iphone X
  * When testing the responsivness for the Iphone X, The navbar adjust and poped up at the right and the tasks also adjusted fine. 
  All the different sizes worked fine. 
* Iphone 6/7/8 
  * When testing the responsivness for the Iphone 6/7/8, The navbar adjust and poped up at the right and the tasks also adjusted fine. 
  All the different sizes worked fine. 
* Benq 24 inch screen 
  * When testing the responsivness for the BenQ, All of the sites and content adjust fine and worked well. 
 
## Deployment 

#### Requirements
* Python3
* Github account
* Heroku account
* MongoDB account

### Clone the project 

* Log in to GitHub and go to the repository you want to clone. 
* Click on the green button with the text Code.
* Click on “Open with GitHub Desktop” and follow the prompts in the GitHub Desktop Application

### Local deployment

1. I created a GitHub reposiroty using the Gitpod full template.
2. I installed Flask, Flask-pymongo and dnspython.
3. I created a env.py file with the enviroment variables: 
   * import os
   * os.environ.setdefault("IP", "0.0.0.0")
   * os.environ.setdefault("PORT", "5000")
   * os.environ.setdefault("SECRET_KEY", "SECRET_NUMBER")
   * os.environ.setdefault("MONGO_URI", "mongodb+srv://milestone3:Porsche997@milestone.3exkg.mongodb.net/Task_manager?retryWrites=true&w=majority")
   * os.environ.setdefault("MONGO_DBNAME", "Task_manager")

5. i added a gitignore and added: 
   * env.py
   * __pycache__/
  
6. in the app.py i imported env.py and i added: 
 <img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/app.JPG" style="width:250px">



8. Before deploying i added the below code to the end of the app.py file and changed the debug=true to debug=False.

     * if __name__ == "__main__":
      * app.run(host=os.environ.get("IP"),
       * port=int(os.environ.get("PORT")),
        * debug=True)



### Deploymen Mongo DB 

Mongo DB is used for tha database in this project 
Start by going to https://www.mongodb.com/ and creata a account. 
1. Start by creating a new Cluster. 
2. Then create database Task_manager. ANd add the collection name categories.
3. Then click on create collections. 
4. Users, Tasks, categories has already been created on step 3.
5. To insert documents to a collection click on the collection categories and then insert document.
6. The following string collections was used: 
  * category_name 
  * task_name
  * task_description
  * start_date
  * due_date
  * created_by 
  * username
  * password
  * Bucketlist_number
  * Bucketlist_description 

7. Go back to github and the repository.
8. Above the list of files click on the code button. 
9. To clone the repository using HTTPS, click HTTPS under "Clone".
10. Press Enter to create your local clone.
11. Create your own env.py file to store variables
  * Import os
  * os.environ.setdefault("IP", "enter value")
  * os.environ.setdefault("PORT", "enter value")
  * os.environ.setdefault("SECRET_KEY", "enter value")
  * os.environ.setdefault("MONGO_URI", "enter value")
  * os.environ.setdefault("MONGO_DBNAME", "enter value")

12. In mongoDB click on the overview button and connect.
13. Pick connect your application.
14. And pick python and version.
15. Copy the link and paste it in the ("MONGO_URI", "enter value")
16. Update the undername and password in the link.


### Deployment Heroku 
1. After loging into heroku I created a new application using the Heroku dashboard.
2. Select application milestone
3. I created requirements.txt and Procfile to the code before because that Heroku requires this to run the app:    
    * pip3 freeze -- local > requirements.txt

    * echo web: python app.py > Procfile
   
4. In the settings tab I clicked reveal config vars and entered the required environment variables, which in this case were:
 * IP (0.0.0.0)
 * PORT (5000)
 * MONGO_URI "mongodb+srv://milestone3:Porsche997@milestone.3exkg.mongodb.net/Task_manager?retryWrites=true&w=majority")
 * SECRET secret key for flask session 
 
5. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub
6. Confirm the linking of the heroku app to the correct GitHub repository in this case MS3 and click connect. 
7. In the heroku dashboard, click "Deploy".
8. In the Manual Deployment section of this page, made sure the master branch is selected and then click "Deploy Branch".
9. The site is now successfully deployed.
10. That can take a minute to build, once it's done, The message ‘Your app was successfully deployed.’ will be shown then Click ‘View’ to launch your new app: https://ms3taskmanager.herokuapp.com/




## Credits 
Hero image on homepage from Pexels.com
Codeinsitute mini project for information and how to structure the site 


