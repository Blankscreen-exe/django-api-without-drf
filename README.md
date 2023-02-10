# Django API Without DRF

This is an attempt at making and API without the help of DRF.

Note that it still has security issues since `@csrf_expemt` decorators are used for its views in `../api/views.py`. Although there is a workaround for this but that would make this API more complex.

> The version of `Django` I'm using is `4.1.6`.

## Installation

- install all the dependencies using `pipenv`
```
cd ./django-api-without-drf
pipenv install
```
- then start the server using the following
```
python manage.py runserver
```
- After that the server wil be available at [http://localhost:8000/](http://localhost:8000/)

## API

`models.py` uses the following structure
```
item:       CharField     (max_length=100)
featured:   BooleanField  (default=False)
price:      IntegerField  (default=0)
```

### **GET Request**

> http://localhost:8000/item

Gets a list of all items

### **Post Request**

> http://localhost:8000/item

Posts a single item with the data present in the request body*.

### **Put Request**

> http://localhost:8000/item/:id

Updates an item at the specified *id*(integer) with the request body*.

### **Delete Request**

> http://localhost:8000/item/:id

Deletes an item at the specified *id*(integer).

### *Request Body

The body in raw `JSON` format looks like this:

```
{
"item": "your item name",
"featured": false,
"price": 1234
}
```

