import logging

from pegtech.data_eng.logging.peg_logging import setup_logging, set_log_record_field
from pegtech.ingest.ingest_csv import IngestCsv
from pegtech.persist.persist_csv import PersistCsv
from pegtech.pipeline.pipeline_base import PipelineBase

setup_logging()


def run():
    log = logging.getLogger('case_a')
    set_log_record_field(pipeline_name="PEGAfrica")
    log.info("START processing case study A")

    customer_pipeline: PipelineBase = PipelineBase(
        ingestor=IngestCsv(source_name='', source_path='../../peg_case_studies/case_a/case_a_data/Customers_Information.csv'),
        transformer=None,
        outputter=None
    )


    customer_pipeline.ingest()


    log.info("FINISH processing case study A")
    return


if __name__ == '__main__':
    run()
