docker stop mycontainer
docker rm mycontainer
docker build -t myimage .
docker run -d --name mycontainer -p 80:80 --restart unless-stopped --privileged myimage
sleep  1
docker logs mycontainer