# 啟動方式:uvicorn first:app --reload
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}

#http://127.0.0.1:8000/items/adf-1234-dfd
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

#http://127.0.0.1:8000/items2/?skip=0&limit=10
@app.get("/items2/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

#http://127.0.0.1:8000/items3/?q=false
@app.get("/items3/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


#http://127.0.0.1:8000/items4/foo?short=1
#http://127.0.0.1:8000/items/foo?short=True
#http://127.0.0.1:8000/items/foo?short=true
#http://127.0.0.1:8000/items/foo?short=on
#http://127.0.0.1:8000/items/foo?short=yes
@app.get("/items4/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

#Multiple path and query parameters
#http://127.0.0.1:8000/users/1234/items/foo
#{"item_id":"foo","owner_id":1234,"description":"This is an amazing item that has a long description"}
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

#http://127.0.0.1:8000/itemsn/foo-item?needy=sooooneedy
@app.get("/itemsn/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}




'''
first one will always be used since the path matches first.
'''
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]



@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


