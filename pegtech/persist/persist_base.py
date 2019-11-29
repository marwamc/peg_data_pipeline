import logging

from pandas import DataFrame


class PersistBase:
    log = logging.getLogger(__name__)
    output_destination: str

    def __init__(self, output_destination: str):
        self.output_destination = output_destination
        self.log.info("initialized...")

    def output(self, data: DataFrame):
        data.to_csv(path_or_buf=self.output_destination)
        return 

