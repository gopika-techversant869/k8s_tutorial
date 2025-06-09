How to Handle Multiple containers:
----------------------------------

If you need to deploy two containers at the same network , without docker compose you should following this:

First you refer the day_05

Here I created the two applications app_1 and app_2. So the app_2 is depend on app_1

Create the docker files for each 

Then build the images for each app 

Create  a local netword then run the container like following

    docker network create my-network

    docker run -d --name flask_app1_container --network my-network -p 5000:5000 flask-app1

    docker run -d --name flask_app2_container --network my-network -p 5001:5001 flask-app2



