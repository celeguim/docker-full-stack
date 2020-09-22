```

sudo docker build --tag my-python-app .

sudo docker run --rm --name python-app -p 5000:5000 my-python-app

sudo docker kill $(sudo docker ps -a -q)

yes| docker system prune
yes| docker volume prune

```

### Stack
````shell script
docker-compose -f docker-compose.yaml up -d

````

### Start MySQL
```
docker network create my-network

docker run --rm --name mysqldb --network my-network -e  MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=mysqldb -d -p 3306:3306 mysql:5.7

docker logs mysqldb

docker exec -it mysqldb mysql -u root --password=root -e 'show databases;'

docker exec -it mysqldb mysql -u root --password=root -e 'use mysqldb; show tables;'

docker kill $(docker ps -a -q)
```

