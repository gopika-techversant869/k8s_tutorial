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

      In this docker file we have to see we using the base image is slim.Becuase

          - python:3.10-slim is a smaller, minimal version of the full Python 3.10 official image.
          
          - It includes only the essential components to run Python.
          
          - This keeps your Docker image size smaller, faster to download and start.
          
          - It excludes many unnecessary packages and tools you don't need in production.
          
          - Good for most apps that don’t require heavy system dependencies.

          You can follow the other python base images also

        



                






