Create docker image:
```bash
docker build --pull --rm -f "Dockerfile" -t htmlscreenshot:latest "."
```

Run docker image:
```bash
docker run --rm -it -d -p 80:80/tcp htmlscreenshot:latest
```

Check is runned:
```bash
docker ps
```

Stop running container:
```bash
docker stop {CONTAINER_ID}
```

