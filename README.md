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

### These are the prerequisites to run the flask restful app, build and run the docker container:

* Vagrant

```
vagrant up
vagrant ssh
```

OBS: Vagrant box port 80 is being mapped by port 8080 on the local machine.

or

* python 2.7 (conservative approach)
* virtualenv 15.0.1 (or superior)
* pip 8.1.1 (or superior)
* pip install -r requirements.txt
* docker 1.12.1 (or superior)
* docker-compose 1.5.2 (or superior)

## Running flask app (without docker):

```
virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
sudo venv/bin/python app.py
(OBS: running as root because of port 80, never do this in production)
[How to run a server on port 80 as a normal user on Linux?](http://serverfault.com/a/112798)
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

Remember to stop any container running on port 80.

You can stop all containers with:
```
docker stop $(docker ps -a -q)
```

```
docker-compose -f docker-compose.test.yml -p ci build
docker-compose -f docker-compose.test.yml -p ci up -d
docker logs -f ci_sut_1
```

# Travis:

There's an integration with [Travis CI](https://travis-ci.org/) to test the python code.

# Brief discussion of:

## Security:

### Concerns:

* DDoS (Distributed Denial-of-Service) attack
* Kernel exploits (shared Kernel, magnifying the vulnerabilities)
* Container breakouts (potential privilege escalation attacks)
* Poisoned images

### Possible solutions:

* Autoscaling
* LoadBalancer
* Caching
* Applying latest updates
* Keeping track of systems, their change history
* Auditing containers change history to check malicious alterations and try to roll-back the containers to a know good state
* Worry about potential privilege escalation attacks
* Use the exact priviledge you need in your application
* Images must be up-to-date and to not contain versions of software with known vulnerabilities

## Monitoring (Amazon ECS):

### ELK (built or paid):

ELK = ElasticSearch, Logstash and Kibana. The ELK Stack is downloaded 500,000 times every month, making it the world’s most popular log management platform.

Logstash collects and parses logs, and then Elasticsearch indexes and stores the information. Kibana then presents the data in visualizations that provide actionable insights into one’s environment.

[The Open Source Elastic Stack](https://www.elastic.co/products)

### Cloudwatch (AWS):

Collects and processes raw data from Amazon ECS into readable, near real-time metrics.

#### Available Metrics and Dimensions:

##### Amazon ECS Metrics:

* CPUReservation
* CPUUtilization
* MemoryReservation
* MemoryUtilization

##### Dimensions for Amazon ECS Metrics:

* ClusterName
* ServiceName

##### Cluster Utilization:

Cluster utilization is measured as the percentage of CPU and memory that is used by all Amazon ECS tasks on a cluster when compared to the aggregate CPU and memory that was registered for each active container instance in the cluster.

##### Service Utilization:

Service utilization is measured as the percentage of CPU and memory that is used by the Amazon ECS tasks that belong to a service on a cluster when compared to the CPU and memory that is defined in the service's task definition.

[Amazon ECS CloudWatch Metrics](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html)

### Datadog (paid):

Datadog understands the difference between pets and cattle, so when ECS brings new containers online, Datadog automatically begins tracking their metrics.

[Monitor Docker on AWS ECS](https://www.datadoghq.com/blog/monitor-docker-on-aws-ecs/)
