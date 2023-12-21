from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.app_layer.interfaces.unit_of_work.sql import IUnitOfWork
from app.config import Config
from app.infra.repositories.sqla.carts import CartsRepository
from app.infra.repositories.sqla.items import ItemsRepository


class Uow(IUnitOfWork):
    def __init__(
        self,
        session_factory: async_sessionmaker[AsyncSession],
        config: Config,
    ) -> None:
        self._session_factory = session_factory
        self._config = config

    async def __aenter__(self) -> IUnitOfWork:
        self._session = self._session_factory()

        self.items = ItemsRepository(session=self._session)
        self.carts = CartsRepository(session=self._session, config=self._config.CART)

        return await super().__aenter__()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def shutdown(self) -> None:
        await self._session.close()
