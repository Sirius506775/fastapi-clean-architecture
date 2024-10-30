from fastapi import FastAPI

import uvicorn

from user.interface.controllers.user_controller import router as user_routers

app = FastAPI()
app.include_router(user_routers)


@app.get("/")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.01", port=8000, reload=True)
