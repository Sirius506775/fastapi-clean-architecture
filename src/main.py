from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.01", port=8000, reload=True)
