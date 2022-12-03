from sensor.entity import artifact_entity, config_entity
from sensor.exception import SensorException
from sensor.logger import logging
import os, sys
from scipy.stats import ks_2samp
from typing import Optional
import pandas as pd

class DataValidation:

    def __init__(self, data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise SensorException(e,sys)


    def drop_missing_values_columns(self, df:pd.DataFrame)->Option[pd.DataFrame]:
        """
        This function will drop column which contains missing value more than specified threshold

        df: Accepts a pandas dataframe
        threshold: Percentage criteria to drop a column
        ===============================================================================
        returns Pandas DataFrame if atleast single column is avaliable after missing columsn drop else None
        
        """
        try:
            null_report = df.isna().sum()/df.shape[0]

            #selecting column name which contains null values
            drop_column_names = null_report[null_report>0.3].index
            df.drop(list(drop_column_names), axis=1, inplace=True)

            #return None no column left
            if len(df.columns)==0:
                return None
            return df
        except Exception as e:
            raise SensorException(e, sys)


    def is_required_columns_exists(self,base_df, present_df)->bool:
        try:
            pass

        except Exception as e:
            raise SensorException(e, sys)


    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        pass