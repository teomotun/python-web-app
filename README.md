# python-web-app
Python app for CI CD




## Running Locally
#### Clone the repo 
```sh
git clone https://github.com/teomotun/python-web-app.git
cd python-web-app
```


#### Setup virtual env and install requirements
```sh    
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```


#### 
```sh
python3 src/app.py 
curl http://127.0.0.1:5000/ 
export PYTHONPATH=src
pytest
```

## Running as a container
#### Build Steps
```
echo "Cleanup images and container if they exist"
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker rmi $IMAGE_NAME
IMAGE_NAME="python-web-app-image"
CONTAINER_NAME="python-web-app-container"
echo "Check current working directory"
pwd
echo "Build docker image and run container"
docker build -t $IMAGE_NAME .
docker run -dit -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME
echo "Copy result.xml into Jenkins container"
rm -rf reports; mkdir reports
docker cp $CONTAINER_NAME:/code/reports/result.xml reports/
cat reports/result.xml


### If not post-build action
echo "Cleanup"
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker rmi $IMAGE_NAME
```


## On Kenkins CentOS Instance
```
#### Install docker
sudo yum install -y yum-utils -y
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo -y
sudo yum install docker-ce docker-ce-cli containerd.io -y
sudo systemctl start docker
sudo systemctl enable docker

#### check what groups jenkins is part of on jenkins server
sudo groups jenkins
#### Add the jenkins user to docker group
sudo usermod -aG docker jenkins 
#### reboot server so all permissions will be in place
sudo reboot
```
