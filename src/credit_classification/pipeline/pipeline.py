from src.credit_classification.logger import logging, get_log_file_name
from src.credit_classification.exception import CreditException
from src.credit_classification.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from src.credit_classification.entity.config_entity import DataIngestionConfig
from src.credit_classification.config.configuration import configuration
from src.credit_classification.entity.experiment import Experiment
from src.credit_classification.constants import *


from src.credit_classification.components.data_ingestion import DataIngestion
from src.credit_classification.components.data_validation import DataValidation




import os 
import sys
from collections import namedtuple
from datetime import datetime
import uuid 
from multiprocessing import process
from typing import List 
from threading import Thread
import pandas as pd

Experiment = namedtuple("Experiment", ["experiment_id", "initialization_timestamp", "artifact_time_stamp",
                                       "running_status", "start_time", "stop_time", "execution_time", "message",
                                       "experiment_file_path", "accuracy", "is_model_accepted"])

class Pipeline(Thread):
    experiment: Experiment = Experiment(*([None] * 11))
    experiment_file_path = None

    def __init__(self, config: configuration )->None:
        try:
            os.makedirs(config.training_pipeline_config.artifact_dir, exist_ok=True)
            Pipeline.experiment_file_path=os.path.join(config.training_pipeline_config.artifact_dir,EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME)
            super().__init__(daemon=False, name="pipeline")
            self.config = config
        except Exception as e:
            raise CreditException(e, sys) from e
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise CreditException(e, sys) from e
        
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_ingestion_artifact= data_ingestion_artifact, data_validation_config=self.config.get_data_validation_config())
            return data_validation.initiate_data_validation()
        
        except Exception as e:
            raise CreditException(e,sys) from e