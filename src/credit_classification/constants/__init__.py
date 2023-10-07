import os
from datetime import datetime


def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


ROOT_DIR = os.getcwd()  #to get current working directory
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)



CURRENT_TIME_STAMP = get_current_time_stamp()


# Training pipeline related variable
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"


EXPERIMENT_DIR_NAME="experiment"
EXPERIMENT_FILE_NAME="experiment.csv"

# Data ingestion related variable 
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR= "data-ingestion"
DATA_INGESTION_INGESTED_TRAIN_DIR_KEY= "ingested_train_dir"
DATA_INGESTION_INGESTED_TEST_DIR_KEY= "ingested_test_dir"

  
# Data validation related Variable 
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_ARTIFACT_DIR= "data_validation"
DATA_VALIDATION_SCHEMA_DIR_KEY= "schema_dir"
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY= "schema_file_name"
DATA_VALIDATION_STATUS_FILE_KEY= "status_file"


