# countries (flask restful api app)

Flask Restful API project for retrieving countries lists.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

This project creates a Restful api to deal with countries lists requests. Returning two types of lists, one for source countries and another for destination countries.

## Example

* source countries:

```
curl --header "Accept: application/json" http://localhost/v1/countries?target=source
[
    {
        "isoCode": "FR",
        "name": "France"
    },
    {
        "isoCode": "GB",
        "name": "United Kingdom"
    }
]
```

* destination countries:

```
curl --header "Accept: application/json" http://localhost/v1/countries?target=destination
[
    {
        "isoCode": "FR",
        "name": "France"
    },
    {
        "isoCode": "IE",
        "name": "Ireland"
    },
    {
        "isoCode": "ES",
        "name": "Spain"
    },
    {
        "isoCode": "GB",
        "name": "United Kingdom"
    }
]
```

## Prerequisites:

* python 2.7
* pip 8.1.2 (or superior)
* docker 1.12.1 (or superior)
* docker-compose 1.8.0 (or superior)

## Recommended:

* Python Virtualenv

## Running flask app (without docker):

```
virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate 
pip install -r requirements.txt
sudo python app.py (OBS: running as root because of port 80)
```

## Testing the python code (app.py):

```
source venv/bin/activate
python app_test.py
```

## Bulding the docker image:

```
docker-compose -f docker-compose.yml build
```

## Running the docker image:

```
docker-compose -f docker-compose.yml up -d
```

## Checking if the docker container is running:

```
curl --header "Accept: application/json" http://localhost/v1/countries?target=source
curl --header "Accept: application/json" http://localhost/v1/countries?target=destination
```

## Testing docker image:

```
docker-compose -f docker-compose.test.yml -p ci build
docker-compose -f docker-compose.test.yml -p ci up -d
docker logs -f ci_sut_1
```