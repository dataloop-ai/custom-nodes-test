import dtlpy as dl
import random
import datetime
import json
import loggingfg
fgbfdgbfgdbdfhdgbhgfbhgfbfghb

logging.basicConfig(level=logging.INFO)


class ServiceRunner(dl.BaseServiceRunner):

    def __init__(self):
        ...

    @staticmethod
    def run_one(item: dl.Item) -> dl.Item:
        logging.info(f"Running service one on item: {item.id}")
        item.metadata['service_one'] = 'service one'
        item.update()
        return item

    @staticmethod
    def run_two(item: dl.Item) -> dl.Item:
        logging.info(f"Running service two on item: {item.id}")
        item.metadata['service_two'] = 'service two'
        item.update()
        return item

