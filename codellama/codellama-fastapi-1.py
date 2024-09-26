from fastapi import FastAPI

app = FastAPI()


@app.get("/")   # The function below this handles GET requests that go to /.
def root():     # A Python function
    return {"message": "Hello Surendra"}

@app.get("/items/{item_id}")
async def read_items(item_id: int):
    return {"item_id": item_id}

@app.put("/items/{item_id}")
async def update_item(item_id: int):
    return {"message": f"Update item with ID {item_id}"}

@app.post("/items")
async def create_item():
    item = {"name": "Foo", "price": 42.0}
    return {"message": "Create new item", "item": item}
    # return {"message": "Create new item"}