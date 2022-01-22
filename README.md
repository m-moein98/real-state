# Shopping Card Project
this application was built to handle problems with saving and managing a real-state listing using FastAPI
the application is built in DDD methodology.
the dockerfile and Nginx conf to run the project are available in the project root.

# Technical Choices
the reason this app is build on FastAPI was the fact that it is fast to build the MVP and it's as scalable as it gets.
mongoDB is chosen as database because there is gonna be a lot database relations in the feutue and we don't our app to slow down becuase of using a relational SQL so we use the best available noSQL which is mongoDB.
in the feuture it is planned to switch to postgres as a replacement for sqlite to scale the project.

# Trade-off
this project was built without any tests and both integrated and unit tests are expected to be added to the project before sending project to production.
most of exception handling system is not done yet due to time limitations and this is also required in the project for feuture.
some enpoints might share other users data with someone who doesn't own the data and it's planned to be fixed in fruture.

# Cloud services
the logging and backup system are provided and managed in cloud side so you cannot see anything related to logging and backup system in the codes here.
this app is not connected to database through internet and the whole databse system in cloud is offline and only availabe to application privately.

# Host
this project is hosted in this address temporarily **[click here](https://ireen.moein98.ir/)**
### the servers are in debug mode on purpose

# About Me
I'm available at this email address: moein1475963.mmz@gmail.com
