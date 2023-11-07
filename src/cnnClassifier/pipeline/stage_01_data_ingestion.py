# DataIngestionTrainingPipeline Class
from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import DataIngestion
from cnnClassifier import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()                                # Create a configuration manager object
        data_ingestion_config = config.get_data_ingestion_config()     # Get data ingestion configuration
        data_ingestion = DataIngestion(config=data_ingestion_config)   # Create a DataIngestion object with the configuration
        data_ingestion.download_file()                                 # Attempt to download a file
        data_ingestion.unzip_and_clean()                               # Attempt to unzip and clean the downloaded file
        
        
# Try-Except Block       
try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()   
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()
except Exception as e:
    raise e