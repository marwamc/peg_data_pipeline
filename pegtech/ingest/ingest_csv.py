import logging
from pandas import DataFrame, read_csv

from pegtech.ingest.ingest_base import IngestBase


class IngestCsv(IngestBase):

    log = logging.getLogger(__name__)
    source_name: str    #
    source_path: str

    def __init__(self, source_name: str, source_path: str):
        super().__init__(source_name, source_path)
        self.source_name = source_name
        self.source_path = source_path
        self.log.info("Ingest csv initialized...")

    def ingest(self) -> DataFrame:
        self.log.info("Ingesting...")
        data: DataFrame = read_csv(self.source_path, sep=',')
        data.info()
        #self.log.info(f"Ingested data: \n{data.info()}")
        #data.describe()
        return data

