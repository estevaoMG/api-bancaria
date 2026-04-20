from fastapi import APIRouter, Depends, status

from src.schemas.transaction import TransactionIn
from src.security import login_required
from src.services.transaction import TransactionService
from src.views.transaction import TransactionOut

router = APIRouter(prefix="/transactions", dependencies=[Depends(login_required)])

service = TransactionService()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionOut)
async def create_transaction(transaction: TransactionIn):
    return await service.create(transaction)


@router.get("/", response_model=list[TransactionOut])
async def read_transactions(limit: int = 10, skip: int = 0):
    return await service.read_all(limit=limit, skip=skip)
