from src.credit_classification.entity.config_entity import DataIngestionConfig
from src.credit_classification.entity.artifact_entity import DataIngestionArtifact
from src.credit_classification.exception import CreditException
from src.credit_classification.logger import logging
from src.credit_classification.constants import *
import pandas as pd
import os
import sys

class DataIngestion:

    def __init__ (self, data_ingestion_config : DataIngestionConfig):
        try:
            logging.info(f"{'>>' *20} Data Ingestion Started. {'<<' * 20}" )
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise CreditException(e,sys) from e
        
    def input_test_train_into_paths(self)->DataIngestionArtifact:
        try:
            train_dataframe = pd.read_csv("C:\\Users\\neo\\Downloads\\archive (4)\\train.csv")
            test_dataframe = pd.read_csv("C:\\Users\\neo\\Downloads\\archive (4)\\test.csv")

            train_file_name= "train"
            test_file_name= "test"

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir, train_file_name)
            test_file_path= os.path.join(self.data_ingestion_config.ingested_test_dir, test_file_name)

            logging.info(f"Exporting training dataset to file: [{train_file_path}]")
            train_dataframe.to_csv(train_file_path, index=False)

            logging.info(f"Exporting test dataset to file: [{test_file_path}]")
            test_dataframe.to_csv(test_file_path, index=False)

            data_ingestion_artifact = DataIngestionArtifact( train_file_path=train_file_path,test_file_path=test_file_path, is_ingested=True, message=f"Data ingestion completed successfully.")
            logging.info(f"Data Ingestion artifact: [{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise CreditException(e, sys) from e
        

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            return self.input_test_train_into_paths()

        except Exception as e:
            raise CreditException(e,sys) from e
        
    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")
    