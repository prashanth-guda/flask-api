from src.db import BaseDbHepler

class users(BaseDbHepler):
    def __init__(self):
        super().__init__()
        self.collection  = self.dbc.async_io_db_client.get_collection('users')

    def add_user