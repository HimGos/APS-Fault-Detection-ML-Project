from sensor.entity import artifact_entity, config_entity
from sensor.exception import SensorException
from sensor.logger import logging
import os, sys
from scipy.stats import ks_2samp
from typing import Optional
import pandas as pd
import yaml

class DataValidation:

    def __init__(self, data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
            self.validation_error = dict()
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
            threshold = self.data_validation_config.missing_threshold
            null_report = df.isna().sum()/df.shape[0]
            #selecting column name which contains null values
            drop_column_names = null_report[null_report>0.3].index
            self.validation_error["dropped_columns"] = drop_column_names
            df.drop(list(drop_column_names), axis=1, inplace=True)

            #return None no column left
            if len(df.columns)==0:
                return None
            return df
        except Exception as e:
            raise SensorException(e, sys)


    def is_required_columns_exists(self, base_df:pd.DataFrame, current_df:pd.DataFrame)->bool:
        try:
            base_columns = base_df.columns
            current_columns = current_df.columns

            missing_columns = []
            for base_column in base_columns:
                if base_column not in current_columns:
                    missing_columns.appent(base_column)

                
            if len(missing_columns)>0:
                self.validation_error["Missing columns"] = missing_columns
                return False
            return True

        except Exception as e:
            raise SensorException(e, sys)

    def data_drift(self, base_df:pd.DataFrame, current_df:pd.DataFrame):
        try:
            drift_report = dict()

            base_columns = base_df.columns
            current_columns = current_df.columns

            for base_column in base_columns:
                base_data, current_data = base_df[base_column], current_df[base_column]
                #Null hypohesis is that both columns data drawn from same distribution
                same_distribution = ks_2samp(base_data, current_data)

                if same_distribution.pvalue>0.05:
                    #We are accepting null hypothesis
                    drift_report[base_column]= {
                        "pvalues":same_distribution.pvalue,
                        "same_distribution":True
                    }
                    #same distribution
                else:
                    drift_report[base_column]={
                        "pvalues":same_distribution.pvalue,
                        "same_distribution":False
                    }

        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        try:
            pass

        except Exception as e:
            raise SensorException(e, sys)

    def write_yaml_file(file_path, data:dict):
        try:
            file_dir = os.path.dirname(file_path)

            os.makedirs(file_dir, exist_ok=True)
            with open(file_path,"w") as file_writer:
                yaml.dump(data,file_writer)

        except Exception as e:
            raise SensorException(e, sys)