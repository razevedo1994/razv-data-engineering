from twitter_hook import TwitterHook
import json
import os
from pathlib import Path


class TwitterOperator:
    def __init__(
        self,
        query,
        file_path,
        conn_id=None,
        start_time=None,
        end_time=None,
        *args,
        **kwargs
    ):
        self.query = query
        self.file_path = file_path
        self.conn_id = conn_id
        self.start_time = start_time
        self.end_time = end_time

    def create_parent_folder(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        #Path(Path(self.file_path).parent).mkdir(parents=True, exist_ok=True)

    def execute(self):
        hook = TwitterHook(
            query=self.query,
            conn_id=self.conn_id,
            start_time=self.start_time,
            end_time=self.end_time,
        )
        self.create_parent_folder()
        with open(self.file_path, "w") as output_file:
            for pg in hook.run():
                json.dump(pg, output_file, ensure_ascii=False)
                output_file.write("\n")


def main(**kwargs):
    TwitterOperator(kwargs['query'], kwargs['file_path']).execute()
