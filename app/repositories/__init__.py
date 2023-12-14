from app.repositories.working_log import WorkingLogRepository
from app.repositories.employee_rates import EmployeeRatesRepository


class Repositories:
    working_log: WorkingLogRepository = WorkingLogRepository()
    employee_rates: EmployeeRatesRepository = EmployeeRatesRepository()
