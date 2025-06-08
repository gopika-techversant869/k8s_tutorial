How to containerize our application
---------------------------------
step 1: Add a Docer file in to your application

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
                      
                      # 3. Copy requirements file into the container
                      COPY requirements.txt .
                      
                      # 4. Install dependencies
                      RUN pip install --no-cache-dir -r requirements.txt
                      
                      # 5. Copy the rest of the application code
                      COPY . .
                      
                      # 6. Default command to run the app
                      CMD ["python", "app.py"]

In this Dockerfile, we start by using a minimal base image:
---------------------------------------------------------------------
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
