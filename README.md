#### Adrien Leblanc

## Docker

### Dockerfile
Creating a dockerfrile using the image of python alpine3.16 as a base.
Defining the working directory and specifying the requirements saved in requirements.txt.
Indicating the langage and python script to use with CMD.

```d
FROM python:alpine3.16

WORKDIR /app

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3" , "getweather.py"]
```



### Build

the command docker build will create a container for each instruction. The finale result is a complet Docker image.
```d
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
 
 
 
 ### Test Run
 Test on a specific Latitude and Longitude using the API key toreturn the current weather for this location
 ```d
adrien@DESKTOP-OUBL135:/mnt/c/Users/adrie/TP1 docker$ docker run --env LAT="5.902785" --env LONG="102.754175" --env API_KEY="bca930721b6d03419b6cb5b0a6cf5b04" app_weather:0.0.1
[{'description': 'broken clouds', 'icon': '04d', 'id': 803, 'main': 'Clouds'}]
 ```
 
 ### Upload to Docker Hub
 ```d
adrien@DESKTOP-OUBL135:/mnt/c/Users/adrie/TP1 docker$ docker tag app_weather:0.0.1 adrienleblanc/weatherinfo:0.0.1                           
adrien@DESKTOP-OUBL135:/mnt/c/Users/adrie/TP1 docker$ docker push adrienleblanc/weatherinfo:0.0.1
The push refers to repository [docker.io/adrienleblanc/weatherinfo]
2bf89fb721c2: Pushed
ed92d852201a: Pushed
17abe6028379: Pushed
e06b65f6b0c2: Pushed
0347066a1a00: Mounted from library/python 
5bb1a595ed81: Mounted from library/python
27f7e4620f8d: Mounted from library/python
09c126bb3acd: Mounted from library/python
24302eb7d908: Mounted from library/python
0.0.1: digest: sha256:11214fda81650fe5863bcd2ad28f3d48e44542fce55f77cbdb4dd787f5aef5fd size: 2202
 ```
 ### Run test from Docker Hub
 Now running from the docker hub registry

 ```d
adrien@DESKTOP-OUBL135:/mnt/c/Users/adrie/Videos/Captures/EFREI/M1 app/Devops/TP1 docker$ docker run --env LAT="5.902785" --env LONG="102.754175" --env API_KEY="bca930721b6d03419b6cb5b0a6cf5b04" adrienleblanc/weatherinfo:0.0.1
[{'description': 'overcast clouds', 'icon': '04n', 'id': 804, 'main': 'Clouds'}]
 ```
### Bonus
O CVE using trivy :
```d
adrien@DESKTOP-OUBL135:/mnt/c/Users/adrie/Videos/Captures/EFREI/M1 app/Devops/TP1 docker$ trivy image adrienleblanc/weatherinfo:0.0.1
2022-06-03T14:15:14.194+0200    INFO    Need to update DB
2022-06-03T14:15:14.194+0200    INFO    Downloading DB...
28.10 MiB / 28.10 MiB [---------------------------------------------] 100.00% 22.77 MiB p/s 2s2022-06-03T14:15:16.870+0200    INFO    Detected OS: alpine
2022-06-03T14:15:16.870+0200    WARN    This OS version is not on the EOL list: alpine 3.16   
2022-06-03T14:15:16.870+0200    INFO    Detecting Alpine vulnerabilities...
2022-06-03T14:15:16.872+0200    INFO    Number of PL dependency files: 0
2022-06-03T14:15:16.872+0200    WARN    This OS version is no longer supported by the distribution: alpine 3.16.0
2022-06-03T14:15:16.872+0200    WARN    The vulnerability detection may be insufficient because security updates are not provided

adrienleblanc/weatherinfo:0.0.1 (alpine 3.16.0)
===============================================
Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)
 ```
 O lint errors using hadolint :
```d
adrien@DESKTOP-OUBL135:/mnt/c/Users/adrie/Videos/Captures/EFREI/M1 app/Devops/TP1 docker$ docker run --rm -i hadolint/hadolint < Dockerfile
Unable to find image 'hadolint/hadolint:latest' locally
latest: Pulling from hadolint/hadolint
6449f89468e7: Pull complete
Digest: sha256:93f0afd12c3be5d732227c0226dd8e7bb84f79319a773d7f8519e55f958ba415
Status: Downloaded newer image for hadolint/hadolint:latest
```
