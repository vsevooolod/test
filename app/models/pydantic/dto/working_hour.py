from pydantic import BaseModel


class CreateLog(BaseModel):
    employee_id: int
    time: int


class ReadTotalTimeByPeriod(BaseModel):
    employee_id: int
    date_from: int
    date_to: int
