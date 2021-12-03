# python-web-app
Python app for CI CD





## Clone the repo 
```sh
git clone https://github.com/teomotun/python-web-app.git
cd python-web-app
```





## Setup virtual env and install requirements
```sh    
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```






## 
```sh
python3 src/app.py 
curl http://127.0.0.1:5000/ 
export PYTHONPATH=src
pytest
```



## Build Steps
```
IMAGE_NAME="python-web-app-image"
CONTAINER_NAME="python-web-app-container"
echo "Check current working directory"
pwd
echo "Build docker image and run container"
docker build -t $IMAGE_NAME .
docker run -d --name $CONTAINER_NAME $IMAGE_NAME
echo "Copy result.xml into Jenkins container"
rm -rf reports; mkdir reports
docker cp $CONTAINER_NAME:/python-test-calculator/reports/result.xml reports/
echo "Cleanup"

### If not post-build action
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker rmi $IMAGE_NAME
```
