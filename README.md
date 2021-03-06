[![CI to Docker Hub](https://github.com/annastrcv/devops/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/annastrcv/devops/actions/workflows/main.yml)

# DevOps labs

Repository for labs in the course of DevOps, Innopolis University

## Description

This repository contains tasks from the labs of DevOps course

## Getting Started

### Dependencies

* Docker
* Python
* MacOS 10.15.7

### Installation

* The program is wrapped in Docker and stored here: https://hub.docker.com/repository/docker/annastrcv/msc_time

### Executing program

* After downloading an image from the Docker Hub use the following commands to make this image run:

```
docker run --rm -p 5000:5000 msc_time
```
where `msc_time` is the name of the image

or run
```
docker-compose up
```
out of the main folder `devops`

## Help

For now this progra deosn't contain any helper info, stay tuned!


## Version History

* Labs 1 & 2 [commit](https://github.com/annastrcv/devops/commit/494f3f882192fd7bc723f249739fe5333a84c0f4) 
* Lab 3 [commit](https://github.com/annastrcv/devops/commit/60706549dcb8c6e6efa280e0a3c8b5971785d15f) 
* Lab 4 [commit](https://github.com/annastrcv/devops/commit/1ee217120d2a165350527c2e0726ea1131dac746)
* Lab 5 [commit](https://github.com/annastrcv/devops/commit/872bf387c182b8bce5f24ee6b86fbc8bd8f659ed) 
* Lab 6 [commit](https://github.com/annastrcv/devops/commit/102548586fb45f072bee304d882e2ce25a6080a0) 
* Lab 7 [commit](https://github.com/annastrcv/devops/commit/a4ad96ee24604ca43cc93892de062fedbde98012)
* Lab 8 [commit](https://github.com/annastrcv/devops/commit/d113455b9672821e71548d79c49135ad6213af9d)
* Lab 9 [commit](https://github.com/annastrcv/devops/commit/e9659be58f9b825aec44d3b6a034fb6939471cee)
* Lab 10 [commit](https://github.com/annastrcv/devops/commit/25c905a201dc0be90525741493d58f2d6b4217c6#diff-17c132990e8e8523ccd403287b6ae761c1cd57f764df278bce7ed310bbddd7f1)
* Lab 11 [commit](https://github.com/annastrcv/devops/commit/1ad534adeaf6aab879c3f4a7f20cdfb8c16e158e)
* Lab 12 [commit](https://github.com/annastrcv/devops/commit/a23d8663890ea67cf39b8d2c24631645bd7f5ebd)
* Lab 13 [commit](https://github.com/annastrcv/devops/commit/974cd3e41116d2b494f356fac8cf035f7c8d3fe4)
* Lab 14 [commit]()

## Improvements based on the feedback

* Docker file improvement
  * [commit](https://github.com/annastrcv/devops/commit/7317baa1e3810d460ad7a82b99763c23952cfd96)
* Fixed repo structure
  * [initial fix](https://github.com/annastrcv/devops/commit/b763e1ed9df2cf11b5f4995505f71b09cf8ef0a5),
  [fixed github actions](https://github.com/annastrcv/devops/commit/b763e1ed9df2cf11b5f4995505f71b09cf8ef0a5)


## Acknowledgments

* [awesome-readme](https://github.com/matiassingers/awesome-readme)

