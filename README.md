# HackMcGill Dev Team Coding Challenge

## Introduction

First, feel free to see the Live-Site Here --> http://104.248.117.23/

This web application was built to complete the development team challenge (check forked repository), for the HackMcGill Recruitment Process 2019.

The stack is:
- Python 3.7
- Django 2.1.4
- MongoDB 4.0 Community
- HTML/CSS
- Python Packages (Djongo)

The application was deployed to a droplet on DigitalOcean, on a VPS running Ubuntu 18.04

## Run Locally

Ensure you have the above dependencies installed.

Then clone the repository --> ``` git clone https://github.com/gaurav-karna/dev-challenge ```

Navigate into the repository: ``` cd dev-challenge/```

Ensure you have MongoDB running in the background, then make the required migrations: ```python3 manage.py makemigrations```, and then follow with ```python3 manage.py migrate```

Start the development server with ```python3 manage.py runserver```, and navigate to ```localhost:8000``` in your browser.

## Challenges

MongoDB is a new technology that I had to learn how to work with. Though I have had minimal NoSQL experience with Google Firebase, it was still a learning curve - albeit, still much easier to work with as opposed to PostgreSQL.

Deploying to DigitalOcean was done through their guide --> https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04#create-and-configure-a-new-django-project

I had some troubles configuring nginx properly, although it should be working properly now. I added a CNAME for hackmcgill.gkarna.com to point to the same resource of the IP address above - although it will take some time to propagate.


## Questions / Improvements

Feel free to open an issue, or contact me at gaurav.karna@mail.mcgill.ca
