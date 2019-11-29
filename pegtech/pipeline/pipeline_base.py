import copy
import logging

from pandas import DataFrame
from pandas.util import hash_pandas_object
from theano import function


from pegtech.data_eng.logging.peg_logging import set_log_record_field
from pegtech.ingest.ingest_base import IngestBase
from pegtech.persist.persist_base import PersistBase
from pegtech.transform.transform_base import TransformBase


class PipelineBase:
    log: logging = logging.getLogger(__name__)
    data: DataFrame
    ingestor: IngestBase
    transformer: TransformBase
    outputter: PersistBase

    def __init__(self, ingestor: IngestBase, transformer: TransformBase, outputter: PersistBase):
        set_log_record_field(request_status="INITIALIZING")
        assert ingestor.validate()
        assert ingestor.validate()
        assert ingestor.validate()
        self.ingestor = ingestor
        self.transformer = transformer
        self.outputter = outputter
        set_log_record_field(request_status="INITIALIZED")
        self.log.info("Base pipeline initialized...")


    @classmethod
    def vanilla(cls):
        empty_pipeline = PipelineBase(ingestor=None, transformer=None, outputter=None)
        return empty_pipeline


    def ingest(self):
        set_log_record_field(request_status="INGESTING")
        self.data = self.ingestor.ingest()
        set_log_record_field(request_status="INGESTED")
        self.log.info("Ingested...")
        return self


    def transform(self):
        set_log_record_field(request_status="TRANSFORMING")
        self.data = self.transformer.transform(self.data)
        set_log_record_field(request_status="TRANSFORMED")
        self.log.info("Transformed...")
        return self


    def transform_custom(self, custom_transform_func: function):
        set_log_record_field(request_status="TRANSFORMING")
        self.data = custom_transform_func(self.data)
        set_log_record_field(request_status="TRANSFORMED")
        self.log.info("Applied custom transform...")
        return self


    def persist(self):
        set_log_record_field(request_status="PERSISTING")
        self.outputter.output(self.data)
        set_log_record_field(request_status="PERSISTED")
        self.log.info(f"Output delivered to: {self.outputter.output_destination}")
        return self


    def validate_custom(self, custom_validation_func: function):
        set_log_record_field(request_status="VALIDATING")
        self.log.info(f"Running validation function: {custom_validation_func.__name__}")
        is_data_validated: bool = custom_validation_func(self.data)
        if is_data_validated:
            set_log_record_field(request_status="VALIDATED")
            self.log.info("Validated!")
            return self
        else:
            set_log_record_field(request_status="FAILED_VALIDATION")
            fail_message = f"Data FAILED Validation! {self.data.info()}"
            self.log.warning(fail_message)
            raise RuntimeWarning(fail_message)


    def copy_shallow(self):
        pipeline_shallow_copy = copy.copy(self)
        self.log.debug("INSPECT")
        self.compare_object_hashes(pipeline_shallow_copy)
        return pipeline_shallow_copy


    def copy_deep(self):
        pipeline_deep_copy = copy.deepcopy(self)
        self.log.debug("INSPECT")
        self.compare_object_hashes(pipeline_deep_copy)
        return pipeline_deep_copy


    def compare_object_hashes(self, b: object):
        reslt_str = '\n'
        for attr in self.__dict__.keys():
            if "data" == attr.lower():
                reslt_str += f"{attr} | OLD: {hash_pandas_object(self.__getattribute__(attr)).sum()}  "
                reslt_str += f"NEW: {hash_pandas_object(b.__getattribute__(attr)).sum()} "
            else:
                reslt_str +=  f"{attr} | OLD: {self.__getattribute__(attr).__hash__()}  "
                reslt_str += f"NEW: {b.__getattribute__(attr).__hash__()}"
            reslt_str += "\n"
        self.log.debug(reslt_str)
        return reslt_str




