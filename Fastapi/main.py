from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read():
    return {"example":"Hello World"}


