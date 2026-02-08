from fastapi import FastAPI

app=FastAPI()
@app.get("/")
def home():
    return {"message":"FastAPI running"}

@app.get("/health")
def health():
    return{"message":"yupp server is working "}