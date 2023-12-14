class Connection:
    def __init__(self, *args, **kwargs):
        pass

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def execute(self):
        pass


class PostgreSQL:
    def __init__(self):
        # configuring of database connection settings
        pass

    def open_connection(self) -> Connection:
        return Connection()
