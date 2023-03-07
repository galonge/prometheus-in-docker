# prom_python_app with prometheus
Basic Python Flask app in Docker instrumented with prometheus which prints the hostname and IP of the container

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone <this-repo>
$ docker build -t prom_python_app .
```

### Run the container
Create a container from the image.
```
$ docker container run --name prom_python_app -d -p 8000:8000 prom_python_app
```

Now visit http://localhost:8000
```
 # The hostname of the container is [container-hostname] and the ip is [container-ip]
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' prom_python_app

[container-ip]

$ docker inspect -f '{{ .Config.Hostname }}' my-container
[container-hostname]

```


