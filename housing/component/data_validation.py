from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact

class DataValidation:

    def __init__(self, data_validation_config: DataValidationConfig, 
                 data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e:
            raise HousingException(e,sys) from e
    
    def is_train_test_file_sxists(self)-> bool:
        try:
            logging.info("checking for training and test file availability")
            train_file_exists = False
            is_test_file_exists = False

            train_file_path= self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exists = os.path.exists(train_file_path)
            is_test_file_exists = os.path.exists(test_file_path)
            
            is_available = is_train_file_exists and is_test_file_exists 

            logging.info(f"Is train and test file exists?->{is_available}")

            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path

                massage = f"Training file: {training_file} or Testing file: {testing_file}"\ 
                "is not present"
                logging.info(massage)
                raise Exception(massage) 
            
            return is_available
        except Exception as e:
            raise HousingException(e,sys) from e

    def validate_dataset_scheama(self)-> bool:
        try:
            validation_status : False
            #validate training and testing dataset using schema file    
            # 1.no. of column
            # 2.check the value of ocean proximity
            #acceptable values  
            # 3.check column names 


            validation_status = True
            return validation_status
        
        except Exception as e:
            raise HousingException(e,sys) from e


    def initiate_data_validation(self):
        try:
            self.is_train_test_file_sxists()
            self.validate_dataset_scheama()


        except Exception as e:
            raise HousingException(e,sys) from e
                 
                 
                 
        pass 