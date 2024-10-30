from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

import uvicorn

from user.interface.controllers.user_controller import router as user_routers

app = FastAPI()
app.include_router(user_routers)


# fastapi에서 400 에러를 422로 처리하고 있기 때문에 , 예외 핸들러를 등록하여 응답코드를 400으로 변경
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors(), "body": exc.body},
    )


@app.get("/")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.01", port=8000, reload=True)
