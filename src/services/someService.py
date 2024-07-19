from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc, insert

# all database querying happen in this class


class SomeServiceClass:
    model = "some_model_class"  # multiple model classes can be used

    async def list(self, session: AsyncSession) -> list:
        statement = select(self.model).order_by(desc(self.model.created_at))
        result = await session.exec(statement)
        return result.all()

    async def create(self, data, session: AsyncSession) -> dict:
        data = data.to_dict()

        data_dict = self.model(**data)
        session.add(data_dict)
        await session.commit()
        return data_dict

    async def update(self, data, session: AsyncSession) -> dict:
        datainstance = await self.get(data.datainstanceId, session)
        if not datainstance:
            return None

        # update to db
        data_dict = data.to_dict()
        for k, v in data_dict.items():
            if v is not None:
                setattr(datainstance, k, v)

        await session.commit()
        return datainstance

    async def delete(self, instanceId: int, session: AsyncSession):
        instance = self.get(instanceId)
        if not instance:
            return None

        await session.delete(instance)
        await session.commit()
        return True

    async def get(self, instanceId: int, session: AsyncSession) -> dict:
        statement = select(self.model).where(
            self.model.signal_id == instanceId)
        result = await session.exec(statement)
        return result.first() if result is not None else None
