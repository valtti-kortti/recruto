from fastapi import FastAPI, Query

app = FastAPI()
@app.get("/")
def read_root(name: str = Query("world"), message: str = Query("")):
    name = name.strip()
    message = message.strip()
    if message:
        return f"Hello {name} {message}"
    else:
        return f"Hello {name}"