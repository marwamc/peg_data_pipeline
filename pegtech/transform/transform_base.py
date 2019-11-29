import logging

from pandas import concat, DataFrame
from pandas.compat.numpy import function


class TransformBase:
    log = logging.getLogger(__name__)

    def __init__(self):
        self.log.info("initialized...")

    def transform(self, data: DataFrame) -> DataFrame:
        self.log.info(f"Will transform data: {data.keys()}")
        transformed_data = DataFrame(data=data)
        self.log.info(f"Transformed data to: {transformed_data.info()}")
        return transformed_data


    def custom_transform(self, custom_transform_function: function, data: DataFrame) -> DataFrame:
        transformed_data = custom_transform_function(data)
        self.log.info(f"Transformed data to: {transformed_data.show()}")
        return transformed_data



