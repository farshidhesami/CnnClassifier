## cnnClassifier : 
  - Best practice for "cnnClassifier"

## venv — Creation of virtual environments : 
  - conda create -n env1 python=3.8 -y
  - conda activate env1
  - pip install -r requirements.txt

## Src : 
  - Add a code in init__.py
  - Define a logger.
  - Define a test.py for check a logger. 
  - Run in Git Bash python test.py for check a logger.
      - [2023-11-04 17:40:07,657: INFO: test: Welcome to our custom Log].

## utils :
  - implementation utils 
  - make a common.py 
  - yaml file and ensure_annotations and json and box and pathlib .....
  - For explain ensure_annotations i add a in research folder trials.ipynb.


# Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py

# Create St_01 :
## Update config.yaml :
  - Go to config folder----> config.yaml
  - create a st_01.ipynb in research folder.
  - Add data_ingestion and add Github address :
     - https://github.com/farshidhesami/Branching-tutorial/raw/master/cat-dog-data.zip
  - Fill a params.yaml example(key:val)- This part should not be empty and after that we will add a right code .
  

## Update entity  :
  - Go to research folder and create a st_01.ipynb and make a Data Ingestion stage

## Update the configuration manager in src config:
  - Go to constants folder and add a code in init__.py  .
  - Go to st_01.ipynb in research folder and add a configuration manager code.
  - Go to utils and add a code in init__.py  .
  - Go to st_01.ipynb and add a code in configuration manager again.
  - Write a data ingestion class.
  - Go back to root folder and run a code .(os.chdir("../"))
  - Run all code 
  - Go to .gitignore and add a artifacts/* in end of code for help to Git Commit(is used to ignore everything in the artifacts/ directory) .

## Update the components:
  - Create a file inside component " data_ingestion.py "  
  - Create a file inside entity " config_entity.py " 
  - Copy from "st_01.ipynb" code data class and paste to config_entity.py
  - After that Update the configuration manager and Create a file in " config " a configuration.py 
  - Copy from "st_01.ipynb" code configuration manager to "configuration.py" import read_yaml and constants and pathlib and os .
  - Copy from "st_01.ipynb" code configuration manager to "configuration.py" code " class ConfigurationManager ".
  - Go to the "entity" and inside a __init__.py add a code "DataIngestionConfig".
  - Go to config and inside a "configuration.py" add a code cnnClassifier.entity import (DataIngestionConfig).

  - Now Update the components:
  - Go to "components" and inside a "data_ingestion.py" add a code from "st_01.ipynb" code "data_ingestion".
  - Add a tqdm(Import the tqdm module for progress bars) and pathlib(Import the Path class from the pathlib module).
  - Add a logger(Import a custom logger module) and get_size(Import a custom utility function for getting file size).
  - Copy from "st_01.ipynb" code "class DataIngestion" code by modification and add a "logger" in previous code .

  ## Update the pipeline :
  - Create a file inside a pipeline "stage_01_data_ingestion.py" and call a method from "st_01.ipynb" code "DataIngestion class".
  - Go to the "config" and inside a __init__.py add a code "ConfigurationManager".
  - Go to the "components" and inside a __init__.py add a code "DataIngestion" .
  - Go to the  pipeline "stage_01_data_ingestion.py" add a code "DataIngestion" and " logger ".
  - add a class DataIngestionTrainingPipeline in pipeline "stage_01_data_ingestion.py" .
  - Try-Except Block Copy from "st_01.ipynb" .
  
  ## Update the main.py :
  - Create a main.py and input from pipeline "stage_01_data_ingestion.py" code into the main.py .
  - Add a "DataIngestionTrainingPipeline" and "logger" .
  - Lets Run a code ,But at first delete a "artifacts" folder.
  - Go to Git Bash command and write a : python main.py
  - We should see a all "running_logs" in logs folder .


# Create St_02 :
## Prepare the Base Model :
- Go to research folder and create a "st_02.ipynb" 

## Update config.yaml :
- Go to "params.yaml" and add a code .
- Go to config folder----> config.yaml add "prepare_base_model" .

## Update the entity:
- Go to the entity folder and inside "Config_entity.py" copy entity class into the "st_02.ipynb".
- Copy from "st_01.ipynb" code configuration manager and add into the "st_02.ipynb" .
- Copy from "st_01.ipynb" code Class "ConfigurationManager" and change base on "PrepareBaseModelConfig".

## Update the components:
- Add a library from "st_01.ipynb" and add code into as new.
- Define a PrepareBaseModel class.(update_base_model and prepare_full_model ....)
- Write a code for test a model base on "ConfigurationManager" and get_prepare_base_model_config .
    - Total params: 14,764,866
    - Trainable params: 50,178
    - Non-trainable params: 14,714,688
- Open a artifacts folder and we have other model " prepare_base_model" and inside folder : Training model ---->"base_model_updated.h5" and Base model----> "base_model.h5" 
- 