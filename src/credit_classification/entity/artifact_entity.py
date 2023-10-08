from collections import namedtuple

DataIngestionArtifact= namedtuple("DataIngestionArtifact", ["train_file_path", "test_file_path", "is_ingested", "ingestion"])

DataValidationArtifact= namedtuple("DataValidationArtifact", ["schema_file_path", "is_validated", "message", "status_file_path"] )