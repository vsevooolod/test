from app.services import Services
from app.models.pydantic import dto


class WorkingLogRepository:
    @staticmethod
    async def create_log(log: dto.CreateLog) -> None:
        query = """
            INSERT INTO working_log (employee_id, time) 
            VALUES (%(employee_id)s, %(time)s);
        """
        async with Services.postgres.open_connection() as connection:
            await connection.execute(query, log.model_dump())

    @staticmethod
    async def get_total_time(employee_id: int) -> int:
        query = """
            SELECT SUM(time_in_seconds) 
            FROM working_log 
            WHERE employee_id = %(employee_id)s;
        """
        async with Services.postgres.open_connection() as connection:
            result = await connection.execute(query, {"employee_id": employee_id})
            return result.fetchone()[0] * 60 * 60

    @staticmethod
    async def get_total_time_by_period(total_time_request: dto.ReadTotalTimeByPeriod) -> int:
        # запрос на получение
        pass
