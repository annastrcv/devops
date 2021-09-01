#Best practices
1) .dockerignore file
2) I used lightweight base image with python
3) Used COPY command inside the Dockerfile rather than ADD
4) Didn't use `apt-get update` inside the Dockerfile