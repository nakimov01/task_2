import uvicorn
from fastapi import FastAPI

app = FastAPI()
char = []
@app.get("/")
def Root():
    return "Hello World"

@app.get("/api/products")
def watch_all_products():
    global char
    if len(char) == 0:
        return "Пусто"
    else:
        return char

@app.get("/api/products/{id}")
def watch_current_product(id: int):
    global char
    for i in range(len(char)):
        if char[i]["id"] == id:
            return char[i]

    return "Тут нет такого значения"

@app.post("/api/products/new")
def create_new_product(id: int, name: str, description: str, prise:float):
    global char
    mag = {
        "id": id,
        "name": name,
        "description": description,
        "prise": prise
    }
    char.append(mag)
    return char

@app.put("/api/products/edit/{id}")
def edit_product(id: int, name: str, description: str, prise:float):
    global char
    for i in range(len(char)):
        if char[i]["id"] == id:
            char[i]["name"] = name
            char[i]["description"] = description
            char[i]["prise"] = prise
            return char[i]
    return "Пусто"

@app.delete("/api/products/delete/{id}")
def delete_product(id: int):
    global char
    for i in range(len(char)):
        if char[i]["id"] != id:
            del char[i]
            return {"Ошибка": "Запрос не был найден"}
    return {"Ответ": "Запрос был удален"}

if __name__ == '__main__':
    uvicorn.run(app, host = "127.0.0.1", port=8000)