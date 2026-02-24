from fastapi import FastAPI
app = FastAPI(title="my-fastapi-pro")

@app.get("/")
def read_root():
    return {"message": "Welcome to my-fastapi-pro API"}
