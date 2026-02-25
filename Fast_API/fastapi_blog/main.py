from fastapi import FastAPI

app = FastAPI()

#route
@app.get("/")
def home():
    return {"message" : "Hello World!"}