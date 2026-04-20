from databases.interfaces import Record

from src.database import database
from src.exceptions import AccountNotFoundError, BusinessError
from src.models.account import accounts
from src.models.transaction import TransactionType, transactions
from src.schemas.transaction import TransactionIn


class TransactionService:
    # =========================
    # LISTAR TODAS AS TRANSAÇÕES (GLOBAL)
    # =========================
    async def read_all(self, limit: int, skip: int = 0) -> list[Record]:
        query = transactions.select().limit(limit).offset(skip)
        return await database.fetch_all(query)

    # =========================
    # LISTAR POR CONTA
    # =========================
    async def read_by_account(
        self, account_id: int, limit: int, skip: int = 0
    ) -> list[Record]:
        query = (
            transactions.select()
            .where(transactions.c.account_id == account_id)
            .limit(limit)
            .offset(skip)
        )
        return await database.fetch_all(query)

    # =========================
    # CRIAR TRANSAÇÃO
    # =========================
    @database.transaction()
    async def create(self, transaction: TransactionIn) -> Record:
        query = accounts.select().where(accounts.c.id == transaction.account_id)
        account = await database.fetch_one(query)

        if not account:
            raise AccountNotFoundError

        if transaction.type == TransactionType.WITHDRAWAL:
            balance = float(account.balance) - transaction.amount
            if balance < 0:
                raise BusinessError("Operation not carried out due to lack of balance")
        else:
            balance = float(account.balance) + transaction.amount

        transaction_id = await self.__register_transaction(transaction)
        await self.__update_account_balance(transaction.account_id, balance)

        query = transactions.select().where(transactions.c.id == transaction_id)
        return await database.fetch_one(query)

    # =========================
    # UPDATE BALANCE
    # =========================
    async def __update_account_balance(self, account_id: int, balance: float) -> None:
        command = (
            accounts.update().where(accounts.c.id == account_id).values(balance=balance)
        )
        await database.execute(command)

    # =========================
    # INSERT TRANSACTION
    # =========================
    async def __register_transaction(self, transaction: TransactionIn) -> int:
        command = transactions.insert().values(
            account_id=transaction.account_id,
            type=transaction.type,
            amount=transaction.amount,
        )
        return await database.execute(command)
