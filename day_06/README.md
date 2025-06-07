Docker installation
---------------------
1. Update the apt package index and install prerequisites:

                    sudo apt-get update
                    sudo apt-get install \
                        ca-certificates \
                        curl \
                        gnupg
   
2. Add Docker’s official GPG key:

                    sudo install -m 0755 -d /etc/apt/keyrings
                    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
                    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

3. Set up the Docker repository:

                    echo \
                    "deb [arch=$(dpkg --print-architecture) \
                    signed-by=/etc/apt/keyrings/docker.gpg] \
                    https://download.docker.com/linux/ubuntu \
                    $(lsb_release -cs) stable" | \
                    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

4.  Install Docker Engine:

                    sudo apt-get update
                    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


6.  Verfify docker
   
                    docker info

          You get the all information about the docker 


7. Run Your first container

Go to your terminal and write this command

                    docker run hello-world

Step-by-step breakdown:
-----------------------------------------
1.Docker CLI (docker) sends a command to the Docker daemon (dockerd) saying:
    “Please run the container hello-world.”

2.Docker Daemon checks if the hello-world image exists locally on your system.

    If not found locally, it pulls the image from Docker Hub:Then you can see this:

        Unable to find image 'hello-world:latest' locally
        latest: Pulling from library/hello-world
        
3.Once pulled, Docker creates a container from the image.

4.Docker starts the container.

5.The container runs a small program that prints like this :

        docker run hello-world
        
                Unable to find image 'hello-world:latest' locally
                latest: Pulling from library/hello-world
                e6590344b1a5: Pull complete 
                Digest: sha256:0b6a027b5cf322f09f6706c754e086a232ec1ddba835c8a15c6cb74ef0d43c29
                Status: Downloaded newer image for hello-world:latest
                
                Hello from Docker!
                This message shows that your installation appears to be working correctly.
                
                To generate this message, Docker took the following steps:
                 1. The Docker client contacted the Docker daemon.
                 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
                    (amd64)
                 3. The Docker daemon created a new container from that image which runs the
                    executable that produces the output you are currently reading.
                 4. The Docker daemon streamed that output to the Docker client, which sent it
                    to your terminal.
                
                To try something more ambitious, you can run an Ubuntu container with:
                 $ docker run -it ubuntu bash
                
                Share images, automate workflows, and more with a free Docker ID:
                 https://hub.docker.com/
                
                For more examples and ideas, visit:
                 https://docs.docker.com/get-started/


Here I am not installed python or any external packages.

If you need to list the images:

        docker images

If you need to remove the container or image, you can use the following commands

            | Command      | What it Removes | What it Works On       | Typical Usage                                  |
        | ------------ | --------------- | ---------------------- | ---------------------------------------------- |
        | `docker rm`  | **Containers**  | Container IDs or names | Delete stopped or exited containers            |
        | `docker rmi` | **Images**      | Image names or IDs     | Delete images (only if no containers use them) |



      
   
