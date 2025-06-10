How to Handle Multiple containers:
----------------------------------

If you need to deploy two containers at the same network , without docker compose you should following this:

First you refer the day_05

In this example, we deploy two Flask applications: app_1 and app_2.

            app_1 runs a simple service.
            
            app_2 depends on app_1 and makes HTTP requests to it.


App structure:
----------------------

day_05/
├── app_1/
│   ├── app.py
│   └── Dockerfile
├── app_2/
│   ├── app2.py
│   └── Dockerfile

Build docker Images 
------------------------------

docker build -t flask-app1 .
docker build -t flask-app2 .

Create docker network
----------------------------------

    docker network create my-network

Run the Containers
----------------------------------------
Run both containers on the same network:

    syntaxc:   docker run -d --name <container_name> --network <network_name> -p <host>:<container> <image_name>

    docker run -d --name flask_app1_container --network my-network -p 5000:5000 flask-app1

    docker run -d --name flask_app2_container --network my-network -p 5001:5001 flask-app2

Test it
-------------------------------
Open your browser at:

        http://localhost:5000/ → shows "Welcome to the Docker Test App!"
        
        http://localhost:5001/ → calls the first app internally and shows:
        

- Both containers are on the same Docker network my-network.

- The second app calls the first app by container name: flask_app1_container.

- Docker’s built-in DNS resolves that name to the correct container IP.

- Ports 5000 and 5001 are mapped to the host for easy browser access.


But here we have some limitations 
-------------------------------------------
1. Manual networking and setup

           - Here we need to setup the same network for each container
2.Harder to manage dependencies
            - If app2 depends on app1, you have to make sure app1 runs first, manually.
            - No built-in depends_on like Docker Compose provides.
            
3.No central configuration

4.Scaling is hard 
            - Want to run 3 instances of a container? You’d have to script it manually.

When manual is okay
--------------------------
           - For very simple setups
            
           - For learning purposes
            
           - When you only need 1 or 2 containers temporarily


If we have more conatiners we need a solution. So that the solution is Docker compose



   


