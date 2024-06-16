import sys
from customer_personality.components.data_ingestion import DataIngestion
from customer_personality.components.data_validation import DataValidation


from customer_personality.exception import AppException


class TrainingPipeline:
    def __init__(self):
        try:
            self.data_ingestion = DataIngestion()
            self.data_validation = DataValidation()
            
        except Exception as e:
            raise AppException(e, sys) from e
        

    def start_training_pipeline(self):
        """
        Starts the training pipeline
        :return: none
        """
        try:
            self.data_ingestion.initiate_data_ingestion()
            self.data_validation.initiate_data_validation()

            
        except Exception as e:
            raise AppException(e, sys) from e
