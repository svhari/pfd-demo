# python-flask-docker rel_1.1
Basic Python Flask app in Docker which prints  the deployment time in addition to the hostname and IP of the container

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/svhari/python-flask-docker.git

$ docker build -t python-flask-docker .
```

### Run the container
Create a container from the image.
```
$ docker run --name pfd -d -p 8080:8080 python-flask-docker
```

Now visit http://localhost:8080
```
 The hostname of the container is 699a0911921d and its IP is 172.17.0.2. 
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pfd
172.17.0.2
$ docker inspect -f '{{ .Config.Hostname }}' pfd  699a0911921d
```


