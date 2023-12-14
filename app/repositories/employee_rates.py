from app.services import Services


class EmployeeRatesRepository:
    @staticmethod
    async def get_hour_rate(employee_id: int) -> int | None:
        query = """
            SELECT hour_rate 
            FROM employee_rates 
            WHERE employee_id = %(employee_id)s;
        """
        async with Services.postgres.open_connection() as connection:
            result = await connection.execute(query, {"employee_id": employee_id})
            result = result.fetchone()
            return result[0] if result is not None else result
