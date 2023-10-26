import dtlpy as dl
import random
import datetime
import json
import logging

logging.basicConfig(level=logging.INFO)


class ServiceRunner(dl.BaseServiceRunner):

    def __init__(self):
        ...

    @staticmethod
    def one(item: dl.Item) -> dl.Item:
        logging.info(f"Running service one on item: {item.id}")
        item.metadata['service_one'] = 'service one v2'
        item.update()
        return item

    @staticmethod
    def two(item: dl.Item) -> dl.Item:
        logging.info(f"Running service two on item: {item.id}")
        item.metadata['service_two'] = 'service two v2'
        item.update()
        return item

