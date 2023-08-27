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
    def runOne(item: dl.Item) -> dl.Item:
        logging.info(f"Running service one on item: {item.id}")
        item.metadata['service_one'] = 'service one'
        item.update()
        return item

    @staticmethod
    def runTwo(item: dl.Item) -> dl.Item:
        logging.info(f"Running service two on item: {item.id}")
        item.metadata['service_two'] = 'service two'
        item.update()
        return item

