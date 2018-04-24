# test-project

#### Description:

this django app gets exchange rates from ECB RSS channel, stores them in a postgres database and serves them via REST API

#### Technologies used:
django, gunicorn, postgres, docker, feedreader, djangorestframework

[see the requirements.pip file](config/requirements.pip)

#### Installation:
- have a virtual machine with debian 8
- install docker CE and docker-compose
- download the repo and `cd` to the main directory
- run `docker-compose up`
- open `localhost:8000` in the browser

You should see "Hello World!!" message.

#### REST Endpoints:
- `localhost:8000/exchange_rates/` - list of all exchange rates
- `localhost:8000/exchange_rates/by_currency/<CURRENCY>`, ex. `localhost:8000/exchange_rates/by_currency/USD` - list filtered by currency

#### Possible improvements:
Currently the app is in the "working in progress" state
- write tests
- use celery for scraping data
- throw exceptions when input is not correct
- add exchange rates list filtering by date (`ExchangeRateViewSet#get_queryset`)
- access to detail of an exchange rate (`get` method of the `ExchangeRateViewSet`)
- add cron job to run a command to scrap new exchange rates once a day
- add frontend web
