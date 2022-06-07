# Django-Error-Logging-Middleware
Task 2 of Upward Fintech Interview Process Logging error using Middleware

How to run the project on your device

1. Clone the Repository on local
```
git clone <url>
```

2. Create a virtual environment
```
python -m venv venv
```

3. Activate the virtual environment
```
venv\Script\activate
```

4. Install all Dependencies
```
pip install -r requirements.txt
```

5. Run Server
```
python manage.py runserver
```

6. Goto the Link displayed on the first page for Error Log Api

7. For Testing middleware create a error in codebase
```
eg: Try removing some leeter from views.py home view
```

8. List of Api's CRUD and Search
```
GET - http://127.0.0.1:8000/error-logs/
POST - http://127.0.0.1:8000/error-logs/
GET Single - http://127.0.0.1:8000/error-logs/{id}
PATCH - http://127.0.0.1:8000/error-logs/{id}/
DELETE - http://127.0.0.1:8000/error-logs/{id}/
SEARCH - http://127.0.0.1:8000/error-logs/?search={text-to-search}

NOTE: {id} should be replaced by appropriate id eg: 1
      {text-to-search} should be replaces by appropriate text eg: field-name
```

9. A Postman collection has been provided with the name "Django Error Log Middleware.postman_collection.json"

Hope you all Liked the solution, Thanks
