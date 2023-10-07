from src.credit_classification.logger import logging
from src.credit_classification.exception import CreditException
from src.credit_classification.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig
from src.credit_classification.constants import *
from src.credit_classification.utils.utils import read_yaml_file

import os,sys

class configuration:
    
    def __init__(self, config_file_path:str = CONFIG_FILE_PATH, current_time_stamp: str = CURRENT_TIME_STAMP) ->None:
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp= current_time_stamp
        except Exception as e:
            raise CreditException(e,sys) from e 
        
    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        try:
            training_pipeline_config= self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir= os.path.join(ROOT_DIR,training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            training_pipeline_config= TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training Pipeline Config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise CreditException(e,sys) from e


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            artifact_dir= self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir= os.path.join(artifact_dir, DATA_INGESTION_ARTIFACT_DIR, self.time_stamp)
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            ingested_train_dir= os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_INGESTED_TRAIN_DIR_KEY])
            ingested_test_dir= os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_INGESTED_TEST_DIR_KEY])
            data_ingestion_config= DataIngestionConfig(ingested_train_dir=ingested_train_dir, ingested_test_dir=ingested_test_dir)

            logging.info(f" Data Ingestion Config :{data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise CreditException(e,sys) from e
        
    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_validation_config_info= self.config_info[DATA_VALIDATION_CONFIG_KEY]
            data_validation_artifact_dir= os.path.join(artifact_dir, DATA_VALIDATION_ARTIFACT_DIR, self.time_stamp)
            schema_file_path= os.path.join(ROOT_DIR,data_validation_config_info[DATA_VALIDATION_SCHEMA_DIR_KEY],
                                           data_validation_config_info[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY])
            status_file_path= os.path.join(data_validation_artifact_dir,data_validation_config_info[DATA_VALIDATION_STATUS_FILE_KEY])

            data_validation_config= DataValidationConfig(schema_file_path=schema_file_path,status_file_path=status_file_path)
            logging.info(f"Data validation Config :{data_validation_config}")
            return data_validation_config
        except Exception as e:
            raise CreditException(e,sys) from e