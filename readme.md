# HTML to screenshot

Docker conainer to generate a JPG screenshot from an HTML page

## Quick start guide

Build a docker image:
```bash
docker build --pull --rm -f "Dockerfile" -t htmlscreenshot:latest "."
```

Run a docker container:
```bash
docker run --rm -it -d -p 8080:80/tcp htmlscreenshot:latest
```

Generate a screenshot
```
curl -X POST \
  http://localhost:8080/image \
  -H 'Postman-Token: cc2238c5-2e53-4fdd-876c-add36a82e63e' \
  -H 'cache-control: no-cache' \
  -d '<html>
This is a web page!
</html>'
```



