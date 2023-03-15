# rpicontainer - Docker COntainer for Raspberry Pi with GPIO

# Set Up Headless Pi
## SD Card
 - Rasperry Pi Imager -> Install Raspbian onto SD Card
    - Set hostname to something reasonable (rpizax)
    - Set user and password
    - Set Wifi SSID and Password

## Run Config
    sudo raspi-config
- Interface ... Turn on i2C, SPI if needed


### install git
    sudo apt update
    sudo apt install git

### Run docker install script
    curl -sSL https://get.docker.com | sh
    sudo usermod -aG docker $USER
    # When you do a reboot, you can just type docker ---.
    # Alternatively, to make it work in your current session, just type
    newgrp docker

### Check if docker is installed correctly
    sudo docker run hello-world

### prepare for project, clone this repo, point to new repo.
    git clone https://github.com/djoha/rpicontainer.git
    mv rpicontainer newrepo
    git remote set-url origin https://github.com/user/newrepo.git

# Editor
## Open VS COde
Make sure Remote-SSH Extension is installed

 - Crtl+Shift+P
 - Remote-SSH: Connect To Host
 - user@hostname
 - Choose OS (Linux)
 - Enter Password

## Click "Open Folder"... navigate to repo.
Note the project structure

    .
    ├── app
    │   ├── __init__.py
    │   └── main.py
    ├── Dockerfile
    ├── relaunch.sh
    └── requirements.txt

# Run the Container
## Run the steps listed below
    ./relaunch.sh

## Build the Image: First time takes a while
    sudo docker build -t myimage .

## Run the container.  Make sure port matches Dockerfile
    sudo docker run -d --name mycontainer -p 80:80 --restart unless-stopped --privileged myimage

## Stop
    sudo docker stop mycontainer

## Remove
    sudo docker rm mycontainer

## Check Logs for Trouble Shooting:
    tail -f /var/log/syslog
    sudo docker logs mycontainer

## Check docs page:
    http://hostname/docs

