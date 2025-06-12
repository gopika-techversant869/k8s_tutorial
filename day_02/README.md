Docker Archetecture
---------------------
![image](https://github.com/user-attachments/assets/46d38e39-24fd-4027-aeb7-fbad84e9ee28)

Docker Components
------------------------

  1.Docker Engine
  ---------------------
  Docker Engine is the core part of Docker that makes everything work — creating, running, stopping containers, pulling images, etc.
  
  It has three parts:
  
      - Docker Daemon (dockerd)
      
      - Docker CLI (docker)
      
      - REST API

                  file:///home/gopika/Downloads/Untitled%20design.png

      Docker Daemon (dockerd)
      -----------------------------
    
        A background service that:
        
          - Builds, runs, and manages containers
          
          - Handles images, volumes, networks

              **Example: When you run:**

                        docker run nginx

                    **What happens:

                           - docker (CLI) sends request to dockerd
                            
                           - dockerd checks if nginx image exists locally
                            
                           - If not, it pulls the image from Docker Hub
                            
                           - Creates a container from the image
                            
                           - Starts the container**

        Docker CLI
        -----------------------------------------
          A command-line interface to interact with Docker

        Docker REST API
        ----------------------------
          - A RESTful HTTP API exposed by dockerd
          
          - Allows external tools to automate Docker actions
          
          - Used internally by the CLI and externally by tools like Portainer, Docker SDKs, etc.

          ![new drawio](https://github.com/user-attachments/assets/3115c944-815e-4d1d-ba84-be4fc7a8295b)

2.Docker Images
---------------------
A read-only template used to create containers.

  - Built from a Dockerfile.
  
  - Contains your app code, runtime (like Python/Node), libraries, and dependencies.
  
  - Example: python:3.10, nginx:latest, myapp:v1

3.Containers
-------------------------
A running instance of an image.

  - Lightweight, fast, isolated environment.
  
  - You can run, stop, restart, and delete containers.

4.Dockerfile
------------------------
A text file with instructions to build a Docker image.

  Defines:
  
    - Base image
    
    - Commands to install dependencies
    
    - Code copy

    - Ports to expose, etc.

5.Docker hub
------------------------
A cloud-based registry to store and share Docker images.

  - Like GitHub but for Docker images.

  - You can pull official images (ubuntu, nginx, etc.) or your own:

6.Docker Compose
-----------------------------
A tool to define and run multi-container applications.

  - Uses a docker-compose.yml file.
  
  - Great for apps with multiple services like web + database.
    
7. Docker Volume
   ----------------------------
  Used for persistent storage in Docker containers.

    - Keeps data even if the container is deleted.

8. Networks
   -------------------------------
  Let containers talk to each other securely.

    -  Default bridge network, or custom user-defined networks.

    -   Used in Compose or multi-container setups.
