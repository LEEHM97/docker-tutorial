from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_wolrd():
    return {"message": "Hello World"}


if __name__ == "__main__":   # pragma: no cover
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
