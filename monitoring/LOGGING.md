#Lab 7 report

##Prerequisites 
* Docekr
* GitHub

##Steps for the first setup
1) Clone the Loki repository
```
git clone https://github.com/grafana/loki.git
```
2) Go to `Production` directory inside `loki` and pull `docker-compose.yaml`
```
cd loki/production
docker-compose pull
```
3) By previous command we get the "docker-compose.yml" file with latest Loki, Promtail and Grafana images. 
4) Create config files in the folder `monitoring` for `Loki` and `Promtail`.

5) Change the `docker-compose.yml` according to your needs
* add your application to services
* mount new config files inside the images
* 
6) To run those images use the following command:
```
docker-compose up
```

7) To see the logs via Grafana dashboard go to ` http://localhost:3000/` and log in with `admin` username and `admin` password.

8) Inside Grafana add Loki `data source` with URL `http://loki:3100`
![img_1.png](img_1.png)

##Best Practices 

Using `json-file` as logging driver and tagging.



