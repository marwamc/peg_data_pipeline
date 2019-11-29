import logging

from pandas import DataFrame

from pegtech.persist.persist_base import PersistBase


class PersistCsv(PersistBase):
    log = logging.getLogger(__name__)

    def __init__(self, output_destination: str):
        super().__init__(output_destination)
        self.output_destination = output_destination
        self.log.info("initialized...")

    def output(self, data: DataFrame):
        data.to_csv(path_or_buf=self.output_destination)
        return data

