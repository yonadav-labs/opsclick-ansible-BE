# Setting up the servers
Just use docker and docker-compose

```bash
$ git clone https://github.com/xyklex/django-mongoengine.git
$ docker build -t opsclick-api-deploy:latest -t opsclick-api-deploy:0.1 .
$ docker-compose up -d
```

And the app will be ready to accept requests


# API endpoints:

## For the cloud:
- `localhost:8000/digitalocean/regions [GET]`
- `localhost:8000/digitalocean/sizes [GET]`
- `localhost:8000/digitalocean/images [GET]` (can receive parameters in the url like '?type=distribution' or '?type=application' just like the digitalocean API)

The requests to this endpoints must contain in the header and digitalocean 'access-key' key 
```json
{"access-key": "71b1eac1e0c4a233c917276cf2f6bd5cda4dd3433c07bdcb9924cc98bd917886"}
```

## For services: 
The idea is that the register of the available services depend from the modules that will be in app_dir/services/mysql, and will be registered automatically when the api start or reload, with that in mind we can retrieve the services and clouds we can setup

- `localhost:8000/service  [GET]` (retrieve all the services registered) 
- `localhost:8000/service/<service_name> [GET,POST]` (create a service in the database)

## For setup:
- `localhost:8000/setup [POST]` 

The json to setup a service in a digitalocean cloud look like the next:
```json
{
	"service":"mysql",
	"cloud":"digitalocean",
	"options":{
		"droplets":["uno"],
		"state": "absent",
		"size": "512mb",
		"image": "ubuntu-14-04-x64",
		"region": "sgp1",
		"access_key":"71b1eac1e0c4a233c917276cf2f6bd5cda4dd3433c07bdcb9924cc98bd917886"
	}
}
```
With the header =>  `Content-Type': 'application/json`

The `state` key can have two values, `absent` will delete any droplet in the `droplets` value, and `present` will create the droplets in the `droplets` value with the information in json.
