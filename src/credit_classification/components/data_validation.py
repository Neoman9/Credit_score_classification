from src.credit_classification.logger  import logging
from src.credit_classification.exception import CreditException
from src.credit_classification.entity.config_entity import DataValidationConfig
from src.credit_classification.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from src.credit_classification.config.configuration import configuration
from src.credit_classification.utils.utils import *
from src.credit_classification.constants import *



import os, sys
import pandas as pd

class DataValidation:

    def __init__ (self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig ):

        try:
            logging.info(f"{'>>' * 20} Data Validation log started {'<<' * 20} \n\n")
            self.data_validation_config= data_validation_config
            self.data_ingestion_artifact= data_ingestion_artifact
            self.data_validation_config.schema_file_path= read_yaml_file(self.data_validation_config.schema_file_path)
        except Exception as e:
            raise CreditException(e,sys) from e
        
    def validate_number_of_columns(self, dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns = len(self.data_validation_config.schema_file_path["columns"])
            logging.info(f"Required number of columns: {number_of_columns}")
            logging.info(f"Data frame has columns: {len(dataframe.columns)}")
            if len(dataframe.columns)==number_of_columns:
                validation_status = True
                with open(self.data_validation_config.status_file_path, 'w') as f:
                    f.write(f"Validation status: {validation_status}")

            else:
                validation_status= False
                with open(self.data_validation_config.status_file_path, 'w') as f:
                    f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise CreditException(e,sys) from e 
        
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise CreditException(e,sys) from e
        
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            error_message= ""
            train_file_path= self.data_ingestion_artifact.train_file_path
            
            #Reading data from train and test file location
            train_data_frame = DataValidation.read_data(train_file_path)

            #Validate number of columns
            status = self.validate_number_of_columns(dataframe=train_data_frame)
            if not status:
                error_message=f"{error_message}Train dataframe does not contain all columns.\n"
            
            data_validation_artifact = DataValidationArtifact(schema_file_path=self.data_validation_config.schema_file_path,
                                                              is_validated= status,
                                                              status_file_path=self.data_validation_config.status_file_path,message="data Validation performed")
            
            logging.info(f"Data Validation Artifact :{data_validation_artifact}")

            return data_validation_artifact
        except Exception as e:
            raise CreditException(e,sys) from e
        
    def   __del__(self):
        logging.info(f"{'>>'*30}Data Validation log Completed.{'<<'*30} \n\n")
    