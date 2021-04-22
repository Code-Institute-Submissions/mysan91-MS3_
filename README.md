
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


## UX 

This site is mainly for personal use and not business.
Its for a user looking to get a good view and structure of tasks on the to do list. 

If you dont feel that you have a good structure and your want to have a system showing you all your tasks in different categorys this site is for your. 


### User Goals
*	As a user type, i want to be able to contact the site owner. 
*	As a user type, i want to be able to register and start an account. 
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


## Design Choices 

#### Home page
* A hero image 
* Hero text with a short about section
* Log in / register navbar 
* Footer with a contact form 
<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/home.JPG" style="width:200px">

##### Log in/ register page
<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/registrer.JPG" style="width:100px">
<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/signin.JPG" style="width:100px">

#### Add task 
<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/addtasks.JPG" style="width:200px">


#### Se all tasks 
<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/tasks.JPG" style="width:200px">

#### Manage Categorys 
<img src="https://raw.githubusercontent.com/mysan91/MS3/master/static/images/addcategory.JPG" style="width:200px">


### Styling 

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


### Technologies used 
Languages:

* HTML5
HTML was used for the main structure of the website.
* CSS3
CSS was used to style and change sizes. 

* Javascript
Was used on the dynamic functions on the site 

* Python3 
Used as Back-End programming language

* Pymongo 
Used as Python's API for MongoDB intergration.

* Flask rendering template, URIs Requests and the flash messages.

* BSON for accessing the data in MongoDB and to access IDs. 

* Werkzeug was user to hash password when registering to the site and encrypting on MongoDB.

Database:
* MongoDB was used to store all data for the website.

* Heroku
Used for hosting my full stack app.

Requests and flash messages.
* Jquery
JQuery was used for materialize features that needed javascript.
* Materialize CSS


Tools & Libraries:
*	Gitpod
* Github
*	Font-Awsome
*	Google Fonts
* Google Chrome



## Testing
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
The following steps i made to deploy the project on to the github page.
1. Log in to the github account. 
2. Pick the repositorie with the name Milestoneprojecttwo. 
3. After you click on the repositorie push the settings button. 
4. Scroll down to the Github pages under the source section. 
5. Click on the none bar and change it to Master.
6. Save the changes! 
7. The page then did refresh and the page is published at 

### Deploymen Mongo DB 

### Run the code locally
1. On the github page navigate to the main page of the repository you want to run. Check repository https://github.com/mysan91/MS3 
2. Above the list of files press on the code button with the downloadinglink.  
3. To clone the repository using HTTPS, under "Clone with HTTPS", click on the https link and the link will be copyed. If you want to clone the repository using SSH or Github Cli click on the link tap ob the respective tabs. 
4. After you have copy the link go to Git Bash and open. 
5. Change the current working directory to the location where you want to put the cloned directory. 
6. Type git clone and paste the repository URL.
7. Press enter to create the local clone. 

### Deployment Heroku 
1. Created a new application using the Heroku dashboard.
2. Go to settings tab, click on 'reveal config vars' and add config vars such as IP (0.0.0.0), PORT (5000), MongoDB Name, MongoDB URI URL with DB name and password.
3. Install Heroku via the console using npm install -g Heroku.
4. Push two new files (requirements.txt and Profile) to repository.
5. Now in In Heroku, you can Enable Automatic Deployment
6. Then deploy branch.
7. That can take a minute to build, once it's done, The message ‘Your app was successfully deployed.’ will be shown then Click ‘View’ to launch your new app: https://ms3taskmanager.herokuapp.com/




## Credits 
Hero image on homepage from Pexels.com
Codeinsitute mini project for information and how to structure the site 


