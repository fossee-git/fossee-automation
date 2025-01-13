
Pre requisite:

To build the docker image
```bash
docker build -t <IMAGE_NAME:TAG> .
```

Allow xserver for docker on local connection
```bash
sudo xhost +local:docker
```

To run:

```bash
docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -v $PWD/<FILE_NAME>:/app/main.py <IMAGE_NAME:TAG> main.py
```
