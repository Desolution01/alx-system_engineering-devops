0x1A-application_server

Log in to web-01

if you have install pip skip, if you have not then install 

sudo apt install -y python3-pip

then install gunicorn

pip3 install gunicorn

you must have clone your AirBnB_clone_v2 repo into your server

in your AirBnB_clone_v2 directory run this code 

gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app

after this open another terminal

login your web-01 again 

then run this code 

curl 127.0.0.1:5000/airbnb-onepage/

you should have this message if everything goes well

Hello HBNB!ubuntu@229-web-01:~$





task 2

Log in to web-01

if you have not install nginx from previous task then install

sudo apt install -y nginx

we have to create nginx configuration file 

sudo vi /etc/nginx/sites-available/airbnb-onepage

input your configuration inside

this is a sample

# Configures Nginx to serve the /number_odd_or_even/ route on AirBnB_clone_v2.

server {
    # Listen on port 80
    listen      80 default_server;
    listen      [::]:80 default_server ipv6only=on;

    # Use server IP as domain name
    server_name 54.237.80.101;

    # Customize HTTP response header
    add_header  X-Served-By 210276-web-01;

    # Serve /airbnb-onepage/ route on AirBnB_clone_v2
    location = /airbnb-onepage/ {
        proxy_pass http://127.0.0.1:5000/airbnb-onepage/;
    }

    # 404 error page
    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}


change the server_name to your web-01 ip
chnage the  X-Served-By to your web-01 id

then run this code to change your configuration to a symbolic link

sudo ln -s /etc/nginx/sites-available/airbnb-onepage /etc/nginx/sites-enabled/

there is a file name 'default' inside the /etc/nginx/sites-enabled/  that we stop your code from running

do this to see it

sudo ls /etc/nginx/sites-enabled/

you can either delete the file "default"

or update it into the new config "airbnb-onepage"

to delete 

sudo rm /etc/nginx/sites-enabled/default

to update vi into default

sudo vi /etc/nginx/sites-enabled/default

copy the content 

update it into the new config file

sudo vi /etc/nginx/sites-enabled/airbnb-onepage

after this then delete the default file 

sudo rm /etc/nginx/sites-enabled/default

the run the code to check your configuration

sudo nginx -t

it should be successful now

restart the nginx service 

sudo service nginx restart

run this code 

 gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app

open another terminal signin to your web-01 again 

can confirm your work 

run this code 

curl 127.0.0.1/airbnb-onepage/

you should get Hello HBNB

logout out of web-01 

and run this code 

curl YOUR_SERVER_IP/airbnb-onepage/

replace with your server ip

you should get the same message

copy the content of your ngnix config file 

create the 2-app_server-nginx_config file 

paste your nginx config inside and push to your github














task 3

Log in to web-01

cd into the AirBnB_clone_v2 directory

and run this code 

tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'

now lets create the nginx configuration file


sudo vi /etc/nginx/sites-available/airbnb-dynamic

paste the content of your ngnix configuration inside

this is a sample 

# Configures Nginx to serve the /number_odd_or_even/ route on AirBnB_clone_v2.

server {
    # Listen on port 80
    listen      80 default_server;
    listen      [::]:80 default_server ipv6only=on;

    # Use server IP as domain name
    server_name 54.237.80.101;

    # Customize HTTP response header
    add_header  X-Served-By 210276-web-01;

    # Serve /airbnb-onepage/ route on AirBnB_clone_v2
    location = /airbnb-onepage/ {
        proxy_pass http://127.0.0.1:5000/airbnb-onepage/;
    }

    # Serve /number_odd_or_even/ route on AirBnB_clone_v2
    location ~ /airbnb-dynamic/number_odd_or_even/(\d+)$ {
        proxy_pass http://127.0.0.1:5001/number_odd_or_even/$1;
    }

    # 404 error page
    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}


change the server_name to your web-01 ip
chnage the  X-Served-By to your web-01 id

then run this code to change your configuration to a symbolic link

sudo ln -s /etc/nginx/sites-available/airbnb-dynamic /etc/nginx/sites-enabled/

you need to remove the previous ngnix file

to delete 

sudo rm /etc/nginx/sites-enabled/airbnb-onepage

then run this code to check your configuration

sudo nginx -t

it should be successful now

restart the nginx service 

sudo service nginx restart

then test your code 

run the following code on your web server

curl 127.0.0.1:5001/number_odd_or_even/6

curl 127.0.0.1/airbnb-dynamic/number_odd_or_even/5

on both occation you should have an html tag saying 6 is even and for the other 5 is odd

logout of your server and run this on your local machine 

curl 35.231.193.217/airbnb-dynamic/number_odd_or_even/6
 your result should be same as above









task 4

*NOTE:* for this task your must have install all the necessary python packages

here are some

pip install gunicorn

pip install Flask

pip install flasgger

pip install flask_cors

pip install SQLAlchemy

pip install Werkzeug


check your Airbnb task for other


Log in to web-01

Clone AirBnB_clone_v3

git clone https://your_personal_token@github.com/your-username/AirBnB_clone_v3.git

input your details where necessary above

after clone cd into the AirBnB_clone_v3

cd AirBnB_clone_v3

in your task 4 there is a like to your AirBnB_clone_v3 

follow the link 

every necessary package you are support to install 

install them into your server for this task

then run this code 

tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'

or you run this 

gunicorn --bind 0.0.0.0:5002 api.v1.app:app

if you did not pass this stage without error 

that means there is a package you have not install

go back and fix it 

next we create our Nginx configuration file for the AirBnB clone v3 API

sudo vi /etc/nginx/sites-available/airbnb-api

paste the content of your ngnix file 

this is a sample

# Configures Nginx to serve the AirBnB_clone_v3 API.

server {
    # Listen on port 80
    listen      80 default_server;
    listen      [::]:80 default_server ipv6only=on;

    # Use server IP as domain name
    server_name 54.237.80.101;

    # Customize HTTP response header
    add_header  X-Served-By 210276-web-01;

    # Serve /airbnb-onepage/ route on AirBnB_clone_v2
    location = /airbnb-onepage/ {
        proxy_pass http://127.0.0.1:5000/airbnb-onepage/;
    }

    # Serve /number_odd_or_even/ route on AirBnB_clone_v2
    location ~ /airbnb-dynamic/number_odd_or_even/(\d+)$ {
        proxy_pass http://127.0.0.1:5001/number_odd_or_even/$1;
    }

    # Serve API on AirBnB_clone_v3
    location /api/v1/ {
        proxy_pass http://127.0.0.1:5002/api;
    }

    # 404 error page
    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}



change the server_name to your web-01 ip
chnage the  X-Served-By to your web-01 id

then run this code to change your configuration to a symbolic link

sudo ln -s /etc/nginx/sites-available/airbnb-api /etc/nginx/sites-enabled/


you need to remove the previous ngnix file

to delete 

sudo rm /etc/nginx/sites-enabled/airbnb-dynamic

then run this code to check your configuration

sudo nginx -t

it should be successful now

restart the nginx service 

sudo service nginx restart

then test your code 

run the following code on your web server on another terminal 



Create the 4-app_server-nginx_config file 

input the content of your ngnix into it

and push to your git hub 







task 5

Log in to web-01

Clone AirBnB_clone_v4

git clone https://your_personal_token@github.com/your-username/AirBnB_clone_v4.git

input your details where necessary above

after clone cd into the AirBnB_clone_v4

cd AirBnB_clone_v4

in your task 4 there is a like to your AirBnB_clone_v4 

follow the link 

every necessary package you are support to install 

sudo apt-get install -y python3-lxml

sudo pip3 install flask_cors 

sudo pip3 install flasgger

sudo pip3 uninstall -y jsonschema 

sudo pip3 install jsonschema==3.0.1

sudo pip3 install pathlib2

install them into your server for this task

in this directory

web_dynamic/static/scripts/2-hbnb.js

make you change the port to 5003

and in this directory too

web_dynamic/2-hbnb.py

then run this code 

cd ~/AirBnB_clone_v4

then run this code 

tmux new-session -d 'gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app'

or run this 

gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app

if you did not pass this stage without error 

that means there is a package you have not install

go back and fix it 

next we create our Nginx configuration file for the AirBnB clone v4


sudo vi /etc/nginx/sites-available/web_dynamic

paste the content of your ngnix file 

this is a sample


# Configures Nginx to serve the complete AirBnB_clone_v4 application.

server {
    # Listen on port 80.
    listen      80 default_server;
    listen      [::]:80 default_server ipv6only=on;

    # Use server IP as domain name
    server_name 54.237.80.101;

    # Customize HTTP response header
    add_header  X-Served-By 210276-web-01;

    # Serve /airbnb-onepage/ route on AirBnB_clone_v2
    location = /airbnb-onepage/ {
        proxy_pass http://127.0.0.1:5000/airbnb-onepage/;
    }

    # Serve /number_odd_or_even/ route on AirBnB_clone_v2
    location ~ /airbnb-dynamic/number_odd_or_even/(\d+)$ {
        proxy_pass http://127.0.0.1:5001/number_odd_or_even/$1;
    }

    # Serve AirBnB_clone_v3 API
    location /api {
        proxy_pass http://127.0.0.1:5002/api;
    }

    # Configure /2-hbnb route of AirBnB_clone_v4 as root location
    location / {
        proxy_pass http://127.0.0.1:5003/2-hbnb;
    }

    # Serve static content for AirBnB_clone_v4
    location /static {
        proxy_pass http://127.0.0.1:5003;
    }

    # 404 error page
    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}


change the server_name to your web-01 ip
chnage the  X-Served-By to your web-01 id

then run this code to change your configuration to a symbolic link

sudo ln -s /etc/nginx/sites-available/web_dynamic /etc/nginx/sites-enabled/


you need to remove the previous ngnix file

to delete 

sudo rm /etc/nginx/sites-enabled/airbnb-api

then run this code to check your configuration

sudo nginx -t

it should be successful now

restart the nginx service 

sudo service nginx restart

Create the 5-app_server-nginx_config file 

input the content of your ngnix into it

and push to your git hub






task 6

Log in to web-01


for this task we have to create a systemd service file

in the root directory of your server

run this code 

sudo mkdir /var/log/airbnb

sudo chown ubuntu:www-data /var/log/airbnb

sudo chmod 775 /var/log/airbnb

sudo vi /etc/systemd/system/gunicorn.service

paste this into it


[Unit]
Description=Gunicorn instance to serve Airbnb_clone_v4 content
After=network.target                                               
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/AirBnB_clone_v4
ExecStart=/home/ubuntu/.local/bin/gunicorn \
    --workers 3 \
    --bind 0.0.0.0:5003 \
    --error-logfile /var/log/airbnb/airbnb-error.log \
    --access-logfile /var/log/airbnb/airbnb-access.log \
    web_dynamic.2-hbnb:app

[Install]
WantedBy=multi-user.target



then run ths code too

sudo systemctl daemon-reload

sudo systemctl start gunicorn

sudo systemctl enable gunicorn

sudo systemctl status gunicorn 

after this last code you should see a green light

and messages showing that the service has started


Upload the gunicorn.service file to GitHub.







task 7

Log in to web-01

in the root directory of your server 

vi 4-reload_gunicorn_no_downtime

paste this 


#!/usr/bin/env bash
# Gracefully reloads Gunicorn.

pgrep gunicorn | xargs | cut -d ' ' -f 1 | xargs kill -HUP



make it executable


then run it 

./4-reload_gunicorn_no_downtime

reboot your server 

sudo reboot


create this file in the 0x1A-application_server directory for github 4-reload_gunicorn_no_downtime

make it executable 

then push to your github 

