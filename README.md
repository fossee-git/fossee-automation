
Pre requisite:

Set docker image name
```bash
export IMAGE_NAME=<SET YOUR DOCKER IMAGE NAME>
```

Set docker image tag
```bash
export IMAGE_TAG=<SET YOUR DOCKER IMAGE TAG>
```

To build the docker image
```bash
docker build -t $IMAGE_NAME:$IMAGE_TAG .
```

Allow xserver for docker on local connection
```bash
sudo xhost +local:docker
```

To run:

```bash
docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -v $PWD/<FILE_NAME>:/app/main.py $IMAGE_NAME:$IMAGE_TAG main.py
```
