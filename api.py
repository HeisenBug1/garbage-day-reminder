from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
import trash

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/garbage", status_code=status.HTTP_200_OK)
async def get_garbage_date(response: Response):
    garbage = trash.initialize(api=True)
    if garbage is None:
        response.status_code = status.HTTP_204_NO_CONTENT
        garbage = "Garbage data not found. Run trash.py in terminal first."
    else:
        garbage = trash.check_garbage_day(garbage, api=True)
    
    return garbage