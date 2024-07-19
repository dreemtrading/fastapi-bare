from fastapi import status, APIRouter, Depends
from ..database.__connector__ import get_session
from sqlmodel.ext.asyncio.session import AsyncSession

class_router = APIRouter()

# all api keys go in here


@class_router.get('/')
async def home():
    return {"message": "welcome to dreem "}


# passing session
@class_router.post('/get-name', status_code=status.HTTP_201_CREATED)
async def add(session: AsyncSession = Depends(get_session)):
    pass
