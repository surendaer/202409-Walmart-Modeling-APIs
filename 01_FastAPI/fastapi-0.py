from fastapi import FastAPI # importing the FastAPI class from the fastapi module

app = FastAPI() # A Python class with API functionality, creating instance 'app'

# The path and operation type (GET, POST, etc) goes to the @app decorator.
# Decorators act on functions put right below it.
# @app is called the "path operation decorator"
# Example: for the URL www.example.com/foo/bar, the path will be '/foo/bar'
@app.get("/")   # The function below this handles GET requests that go to /.
def root():     # A Python function
    return {"message": "Hello World"}

@app.get("/items")
def read_items():
    return {"item1": "value1", "item2": "value2"}

# Other operations:
# @app.post(), @app.delete(), @app.put()
# Other lesser-known ones:
# @app.options(), @app.head(), @app.patch(), @app.trace()

