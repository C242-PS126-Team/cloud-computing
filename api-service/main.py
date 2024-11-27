from fastapi import FastAPI

app = FastAPI()

# Endpoint Default untuk page utama
@app.get("/")
def greet():
    return {"message": "Hello, World!"}

# Endpoint untuk mendapatkan pesan
@app.get("/api/")
def greet():
    return {"message": "Hello, this page for api!"}

# todo

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
