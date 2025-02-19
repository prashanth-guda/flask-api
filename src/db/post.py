from src.db import BaseDbHepler

class post(BaseDbHepler):
    def __init__(self):
        super().__init__()
        self.collection  = self.dbc.async_io_db_client.get_collection('post')


    def add_post()
