#### Adrien Leblanc

## Installation de Docker

## Docker

### Dockerfile
Création d'un dockerfile en important l'image de python alpine3.16 comme base.

### Build image

```ps
adrien@DESKTOP-OUBL135:/mnt/c/Users/adrie/TP1 docker$ docker build . -t app_weather:0.0.1
[+] Building 0.9s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                0.0s 
 => => transferring dockerfile: 38B                                                                                                                                                                 0.0s 
 => [internal] load .dockerignore                                                                                                                                                                   0.0s 
 => => transferring context: 2B                                                                                                                                                                     0.0s 
 => [internal] load metadata for docker.io/library/python:alpine3.16                                                                                                                                0.7s 
 => [internal] load build context                                                                                                                                                                   0.0s 
 => => transferring context: 565B                                                                                                                                                                   0.0s 
 => [1/5] FROM docker.io/library/python:alpine3.16@sha256:f04a62c5f08dffec45b3d33a41c61112394669f17aca2b2dc260f7a993fa373b                                                                          0.0s 
 => CACHED [2/5] WORKDIR /app                                                                                                                                                                       0.0s 
 => CACHED [3/5] COPY requirements.txt ./                                                                                                                                                           0.0s 
 => CACHED [4/5] RUN python -m pip install --no-cache-dir -r requirements.txt                                                                                                                       0.0s 
 => [5/5] COPY . .                                                                                                                                                                                  0.0s 
 => exporting to image                                                                                                                                                                              0.0s 
 => => exporting layers                                                                                                                                                                             0.0s 
 => => writing image sha256:11214fda81650fe5863bcd2ad28f3d48e44542fce55f77cbdb4dd787f5aef5fd                                                                                                        0.0s 
 => => naming to docker.io/library/app_weather:0.0.1    
 ```
 
