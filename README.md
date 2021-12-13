# rpicontainer

# Headless Pi:
- SDCardFormatter -> Quick Format the SD Card
- Rasperry Pi Imager -> Install Raspbian onto SD Card
- In "boot" directort, 
  - add a file called SSH
  - Add "ip=192.168.x.x" to the end of the line in cmdline.txt


# Run Config
sudo raspi-config
# WiFi region, ssid, passphrase
# Interface ... Turn on i2C, SPI


# install python
sudo apt update
sudo apt install python3

# install git
sudo apt install git

# Run docker install script
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker $USER
# When you do a reboot, you can just type docker ---.
# Alternatively, to make it work in your current session, just type
newgrp docker

# Check if docker is installed correctly

sudo docker run hello-world

mkdir myproject

# Open VS COde
Crtl+Shift+P
Remote-SSH: Connect To Host
pi@10.54.40.59
Choose OS
Enter Password (raspberry)

# Click "Open Folder"... navigate to project folder

# Build the Image: First time takes a while
sudo docker build -t myimage .

# Run the container.
sudo docker run -d --name mycontainer -p 80:80 --restart unless-stopped myimage

# Stop
sudo docker stop mycontainer

# Remove
sudo docker rm mycontainer



