#### Adrien Leblanc
# TP2 - API - Github Actions

## API Making with flask

Creation of an instance of flask and a route :

```python
from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods =['GET'])
```
Creation of a function with no parameters. latitude and longitude are fetched using the method request from flask instead and appid is given directly in order to test it.
```python
def get_coord_weather():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    appid = "***"
    #appid = os.environ.get('API_KEY')
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}")
    return str(response.json())
```
Definition of a port to run the app
```python
if __name__ == "__main__":
    app.run(port = 8081,debug=True)
    get_coord_weather()
```
### Testing the API

Running getweather-tp2.py
```ps
PS C:\Users\adrie\Videos\Captures\EFREI\M1 app\Devops\TP2 API\docker> & C:/Users/adrie/anaconda3/python.exe "c:/Users/adrie/Videos/Captures/EFREI/M1 app/Devops/TP2 API/docker/getweather-tp2.py"
 * Serving Flask app "getweather-tp2" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with watchdog (windowsapi)
 * Debugger is active!
 * Debugger PIN: 313-298-899
 * Running on http://127.0.0.1:8081/ (Press CTRL+C to quit)
```
In a terminal I run the command :

```ps
PS C:\Users\adrie\Videos\Captures\EFREI\M1 app\Devops\TP2 API> curl "http://localhost:8081/?lat=5.902785&lon=102.754175"
  

StatusCode        : 200
StatusDescription : OK
Content           : {'coord': {'lon': 102.7542, 'lat': 5.9028}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'base': 'stations', 'main':       
                    {'temp': 300.96, 'feels_like': 303.09, 'te...
RawContent        : HTTP/1.0 200 OK
                    Content-Length: 580
                    Content-Type: text/html; charset=utf-8
                    Date: Fri, 10 Jun 2022 08:01:15 GMT
                    Server: Werkzeug/2.0.3 Python/3.8.8
                    {'coord': {'lon': 102.7542, 'lat': 5.9028}, 'w...
Forms             : {}
Headers           : {[Content-Length, 580], [Content-Type, text/html; charset=utf-8], [Date, Fri, 10 Jun 2022 08:01:15 GMT], [Server, Werkzeug/2.0.3 Python/3.8.8]}8]}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 580
```

## docker

Build a docker image

```d
adrien@DESKTOP-OUBL135:/mnt/c/Users/adrie/Videos/Captures/EFREI/M1 app/Devops/TP2 API/docker$ docker build . -t app_weather:0.0.2
[+] Building 6.6s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                       0.0s 
 => => transferring dockerfile: 38B                                                                                                                        0.0s 
 => [internal] load .dockerignore                                                                                                                          0.1s 
 => => transferring context: 2B                                                                                                                            0.0s 
 => [internal] load metadata for docker.io/library/python:alpine3.16                                                                                       0.0s 
 => [1/5] FROM docker.io/library/python:alpine3.16                                                                                                         0.0s 
 => [internal] load build context                                                                                                                          0.2s 
 => => transferring context: 11.57MB                                                                                                                       0.2s 
 => CACHED [2/5] WORKDIR /app                                                                                                                              0.0s 
 => [3/5] COPY requirements.txt ./                                                                                                                         0.0s 
 => [4/5] RUN python -m pip install --no-cache-dir -r requirements.txt                                                                                     5.7s 
 => [5/5] COPY . .                                                                                                                                         0.1s 
 => exporting to image                                                                                                                                     0.3s 
 => => exporting layers                                                                                                                                    0.3s 
 => => writing image sha256:b166ea155850650c77f2e832e9e1bbddfb9505e479c4b5b8bdc4c9ea15f7f62d                                                               0.0s 
 => => naming to docker.io/library/app_weather:0.0.2      
```
#### Create a directory .github/workflows containing the file main.yaml
#### Steps are : check repository, log in docker using secret actions variables stored in github, specify dockerhub's registry, build and push the docker's image
#### Now everytime code is pushed on github, the action starts and push the new image on Dockerhub on the registry adrienleblanc/efrei-devops-tp2 with the tag "Main"

### hadolint
added hadolint verification with following steps :
```d
      - name: hadolint
        uses: hadolint/hadolint-action@v2.0.0
        with:
          dockerfile: dockerfile
```