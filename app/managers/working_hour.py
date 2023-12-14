from app.models.pydantic import dto
from app.repositories import Repositories


class WorkingHourManager:
    @staticmethod
    async def log(log: dto.CreateLog) -> None:
        try:
            await Repositories.working_log.create_log(log=log)
        except Exception as ex:  # Catch Integrity error or something else, Exception for example
            pass

    @staticmethod
    async def total_time(employee_id: int) -> int:
        return await Repositories.working_log.get_total_time(employee_id=employee_id)

    @staticmethod
    async def salary(total_time_request: dto.ReadTotalTimeByPeriod) -> float:
        hour_rate = await Repositories.employee_rates.get_hour_rate(employee_id=total_time_request.employee_id)
        if hour_rate is None:
            # raise RequestedDataWasNotFound(f"Employee with id={total_time_request.employee_id} was not found")
            pass
        total_time_by_period = await Repositories.working_log.get_total_time_by_period(
            total_time_request=total_time_request
        )
        return total_time_by_period * hour_rate
