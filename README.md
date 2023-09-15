# Currency converter

This application allows you can convert any currency to any other currency.

You need to send get-request like "api/rates?from=CUR1&to=CUR2&value=AMOUNT" where instead of CUR1 you put 3-letters
abbreviation for converted currency, instead of CUR2 - new currency, instead of AMOUNT - amount (int or float number) 
of converted currency.

### Example
GET /api/rates?from=USD&to=RUB&value=10
#### Response:
{
"result": 921.6
}

## Installation
    * Clone repository
    * Create virtual environment and activate it
    * Install packages from requirements.txt: pip install -r requirements.txt
    * Create .env file with necessary information
    * Create database: python manage.py migrate
    * Launch server: python manage.py runserver
    * To create docker image: sudo docker-compose up -d
    * Run migration: docker-compose exec web python manage.py migrate --noinput