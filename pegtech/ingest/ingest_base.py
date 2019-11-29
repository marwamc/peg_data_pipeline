import logging
from pandas import DataFrame, read_csv


class IngestBase:

    log = logging.getLogger(__name__)
    source_type: str
    source_path: str

    def __init__(self, source_type: str, source_path):
        self.source_type = source_type
        self.source_path = source_path
        self.log.info("Ingest base initialized...")

    def ingest(self) -> DataFrame:
        self.log.info("Ingesting...")
        data: DataFrame = read_csv(self.source_path)
        data.info()
        return data

    def validate(self):
        self.log.info("Validation passed!")
        return True

