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


      Docker Daemon (dockerd)
      -----------------------------
    
        A background service that:
        
          - Builds, runs, and manages containers
          
          - Handles images, volumes, networks

              **Example: When you run:**

                      docker run nginx
