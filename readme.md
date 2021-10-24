# HTML to screenshot

Docker conainer to generate a JPG screenshot from an HTML page

## Quick start guide

Run a docker container:
```bash
docker run --rm -it -d -p 8080:80/tcp arbeleon/htmlscreenshot:1.0.0
```

Generate a screenshot
```
curl -X POST \
  http://localhost:8080/image \
  -d '<html>
    This is a web page!
   </html>' \
  --output screenshot.jpg
```

## Build a docker image

Build a docker image:
```bash
docker build --pull --rm -f "Dockerfile" -t htmlscreenshot:latest "."
```

## Docker repository

[Docker Hub arbeleon/htmlscreenshot](https://hub.docker.com/repository/docker/arbeleon/htmlscreenshot)



