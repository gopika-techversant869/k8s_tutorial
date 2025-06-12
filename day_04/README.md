How to containerize our application
---------------------------------
step 1: Add a Docer file in to your application
----------------------------------------------------------

Follow the official Docker Documentation:

https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/

A Dockerfile is a plain text file with instructions that Docker uses to build a custom image of your application. It tells Docker things like:

      - What base image to use
      
      - What files to copy
      
      - What packages to install
      
      - What command to run when the container starts


                      # 1. Base image with Python pre-installed
                      FROM python:3.10-slim
                      
                      # 2. Set the working directory in the container
                      WORKDIR /app
               Run with Port Mapping (for web apps)       
                      # 3. Copy requirements file into the container
                      COPY requirements.txt .
                      
                      # 4. Install dependencies
                      RUN pip install --no-cache-dir -r requirements.txt
                      
                      # 5. Copy the rest of the application code
                      COPY . .
                      
                      # 6. Default command to run the app
                      CMD ["python", "appRun with Port Mapping (for web apps).py"]day_04day_04

In this Dockerfile, we start by using a minimal base image:
---------------------------------------------------------------------
List of base images : https://hub.docker.com/_/python  (you can refer this)

🔹 Base Image: python:3.10-slim
                  - It's a lighter version of the full Python 3.10 image.
                  
                  - It contains only the core Python runtime and minimal system libraries.
                  
                  - This results in smaller image size, faster builds, and better performance.
                  
                  - Ideal for production use where we don’t need extra development tools or compilers.
                  
                  - You can also use other variants like python:3.10, python:3.10-alpine, etc., based on your needs.

🔹 WORKDIR /app
                  - This creates the /app folder (if it doesn't exist) in the container.
                  
                  - It also sets it as the current working directory for all following instructions.
                  
                  - So all file paths after this are relative to /app.
            docker build -t your-image-name .RUN pip install --no-cache-dir -r requirements.txt


                                    /
                                    ├── app/
                                    │   ├── requirements.txt
                                    │   ├── app.py
                                    │   └── (your app files)
                                    ├── bin/
                                    ├── lib/
                                    ├── usr/
                                    └── ... (system folders)

🔹 COPY requirements.txt .
                  - Copies requirements.txt from your host machine into the /app folder in the container.
                  
                  - The . means “copy to the current directory,” which is /app.
                  

🔹 RUN pip install --no-cache-dir -r requirements.txt
                  -  Installs Python dependencies listed in requirements.txt.
                  
                  -   --no-cache-dir avoids caching downloaded packages, keeping the image smaller.
                  
                  - Note: These dependencies are installed system-wide in the container (not just /app).

🔹 COPY . .
                  - The first . = your current directory on your local machine (project folder).
                  
                  - The second . = current directory inside the container, which is /app.
                  
                  - This copies all your app files into /app in the container.
                  
                  -  Warning: This will also copy unwanted files unless you use a .dockerignore.

🔹 CMD ["python", "app.py"]

                  - This is the default command that runs when the container starts.
                  
                  - It runs python app.py inside the /app directory.



Then we build the docker Image
------------------------------------------
For building the image we can use :

            docker build      # Command to build a Docker image
            -t myapp:latest   # -t stands for "tag"; gives your image a name and optional version
                  .           # The dot means: "build using the Dockerfile in the current directory"

List images:
------------------
If you need to list the images :
            
            docker images

How to convert this image to a container
-----------------------------------------

We can run our container in serveral ways:

1) Basic Run - docker run image-name
2) Run with name - docker run --name mycontainer image-name (Gives the container a custom name for easy reference later (instead of random IDs)
3) Detached Mode (Run in Background) - docker run -d --name mycontainer image-name (Runs the container in the background (doesn’t show logs in the terminal)
4)Run with Port Mapping (for web apps) - docker run -p 8000:8000 image-name  (Maps port 8000 on your host to port 8000 inside the container)

How to get the status of the container:
---------------------------------------
docker ps           - Running containers
docker ps -a        - All containers (including stopped ones)


Its looks like
----------------------------------------

![image](https://github.com/user-attachments/assets/b64b2f1f-03b3-4e81-8cb3-aaf7e622e7a9)

How to debug the containers
--------------------------------------

We can log the container use:
      docker logs container_id or container name
      
If you want to "go inside" the running container to inspect or debug things:
      docker exec -it <container-name> /bin/bash

Once inside, you can:

            - Check files (ls, cat)
            
            - View logs (tail, less)
            
            - Run Python commands (python)
            
            - Inspect installed packages, etc.


How to stop tyhe container:

      docker stop container name


Note:
------
You can try this with docker_test_app 
            
            


