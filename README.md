
Pre requisite:

Allow xserver for docker on local connection
```bash
sudo xhost +local:docker
```

To run:

```bash
docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -v ./Checker.py:/app/Checker.py iit Checker.py
```
