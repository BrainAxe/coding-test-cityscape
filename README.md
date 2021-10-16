# coding-test-cityscape

## Introduction
This project contains a single post api request for room booking which takes four fields(booking_date, status, first_name, last_name, email) and give response either 'Successfully Booked' or 'Already Booked' according to on that day's room status. Please check the `Postman` collection for POST form data structure.

# Technology
  1. Django 3.2
  2. Postgres
  3. Redis
  4. Nginx
  5. Locust
  6. Docker


## Installation

### Docker
1. Clone this repo and enter inside
2. Run `docker-compose up --build`
3. Server will be on http://127.0.0.1:1337
4. Import the `Postman` collection which contains a single post api request for room booking 


## Load Test
Inside the `loadTest` directory `locustfile` is located.

1. Run `pip install locust`
2. Start the docker containers
3. Go inside `loadTest`
4. Run `locust --host=http://localhost:1337`
5. Open Browser and go to **http://localhost:8089**

## Future Work
 - [ ] FrontEnd
 - [ ] Load Balancer
