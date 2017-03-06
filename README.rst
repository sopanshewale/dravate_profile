Created by `Sopan Shewale <http://twitter.com/sopan_shewale>`_

========
Overview
========

Django has great User Management Apps included with it. But it's required to extend those by additional attributes to the Users. 
This application is developed to demonstrate the ability to extend exisiting User Management (rather User Profiles) App. 

This is docker enabled. You can start the docker image with **Docker Compose** tool. 

Features
========

   * Demonstrate the use of **Bootstrap** and **jQuery** 
   * Extended User Attributes - added **Phone** and **Address** 
   * Users can edit own profile
   * Users can change own passwords 

Running Docker Image
========

After cloning code into your working directory, you just need to run following command: 

    $ docker-compose up -d



This will start (This takes time for the first time - it's based on django image from Docker Repository) **dravate_profile**
image. 

You can connect to iamge via: 

    $ docker exec -it dravate_profile  bash


To create a  Super-User - you need to execute following commands afrer connecting to docker image via command line. 


#python manage.py createsuperuser 
Username (leave blank to use 'root'): demo 
Email address: demo@example.com
Password: 
Password (again): 
Superuser created successfully.


After that - you can visit

    http://localhost:9191
 

TODO
========
   * User Image upload 
   * Register on own (at this moment, admin user needs to create the new user) 

Collaboration or Consultancy
========

I can help you with consultacy work in **Django Framework** and other **Python** Projects. I can be contacted via `Sopan Shewale <http://twitter.com/sopan_shewale>`_


