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


      
   
