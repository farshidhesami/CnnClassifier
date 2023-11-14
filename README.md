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

## Create St_03 :
 - Create a file inside component "prepare_base_model.py " .
 - Copy from "st_02.ipynb" code @dataclass(frozen=True)-------> "class PrepareBaseModelConfig"  and paste to "config_entity.py" 
 - Copy from "st_02.ipynb" in "class ConfigurationManager" code add code "def get_prepare_base_model_config" code into the config_entity.py" . 
 - go to the "config" folder and add code in "configuration.py"-----> PrepareBaseModelConfig in code from cnnClassifier.entity import for active it go to next step.
 - Go to the "entity" and inside a __init__.py add a code "PrepareBaseModelConfig" .

## Update the components:
- Go to the component "prepare_base_model.py " and Copy from "st_02.ipynb" in "PrepareBaseModel class" copy all code and paste to component "prepare_base_model.py ".
- We have missing file and add into the code in  "pathlib" and "tensorflow" and "cnnClassifier.entity" .

## Update the pipeline :
- Create a file inside a pipeline "stage_02_prepare_base_model.py" and go to the "stage_01_data_ingestion.py" and copy all file and insted of "DataIngestionTrainingPipeline"---->  
- ----- > add a "PrepareBaseModelTrainingPipeline" and change a code and go to "st_02.ipynb" and copy from "Test a model" and add code to "stage_02_prepare_base_model.py".
- Go to the "components" and inside a __init__.py add a code "from cnnClassifier.components.prepare_base_model import PrepareBaseModel".
- Go to the "main.py" and add a code "from ..... import PrepareBaseModelTrainingPipeline" and then add code "STAGE_NAME = "Prepare base model" .
- For check a loggers , first delete a "artifacts" folder and open a Git Bash and Write a " python main.py".
- Open a logs and see all loggs .

# Create St_03 :
## Prepare Callbacks :
- Go to the research folder and create a "st_03.ipynb" add basic code.


## Update config.yaml :
- Go to config folder----> config.yaml and add code "prepare_callbacks" 

## Update the entity:
- Add dataclasses code .
- Add library "cnnClassifier.constants" and "cnnClassifier.utils" 

## Define a configuration manager :
- Add a class ConfigurationManager code .

## Define a components:
- Add a libraries
- Define a PrepareCallback class
- Define a Test model (config.get_prepare_callback_config).
- Run a code 
- Go to "artifacts" folder and "prepare_callbacks" created there and there are two folder "checkpoint_dir" and "tensorboard_log_dir" 
- Go to "st_03.ipynb" into the "entity" code copy a "@dataclass(frozen=True)" code into the entity folder "config_entity.py" 
- Go to the  entity folder "__init__.py" and add a code " PrepareCallbacksConfig" .
- Go to "st_03.ipynb" into the Define a configuration manager copy def get_prepare_callback_config code and paste it into the Config folder and "configuration.py" ------->
- -------->def get_prepare_callback_config(self) -> PrepareCallbacksConfig code  then add a "PrepareCallbacksConfig"  into the " from cnnClassifier.entity import" . 

- Create a file inside a "components" as s  " prepare_callback.py " and copy a code from "st_03.ipynb"-----> components PrepareCallback class and paste to "prepare_callback.py" with
  library code .
- Go to the  "components" folder and in " __init__.py" folder add code : "...........import PrepareCallback"
- No need to add a pipeline stage "PrepareCallback" ,because  PrepareCallback only responsible for Training and we will do in other stage as a "stage_03_training.py".

# Create St_04 :
## Training :
- Go to the "research" and create a " st_04.ipynb " and add code for go to "cnnClassifier" .

## Create a entity:
- Make a data class and base on create a "entity " code .

## Update config.yaml :
- Go to config folder----> config.yaml and add code "training" .

## Training :
 Go to the  " st_04.ipynb " folder and write a library .

 ## Define a configuration manager class :
- Add a code from "st_03.ipynb" class ConfigurationManager into the " st_04.ipynb " and then add training related configuration class into the code .
- Add a code from "st_03.ipynb" library  for class PrepareCallback at first add a: "import time"
- Then create a PrepareCallback class base on "st_03.ipynb" and copy and paste .
- Create a Training Components and copy code from "st_03.ipynb" library .
- Create a " class training " and  then "def get_base_model" and then add a "def train_valid_generator" 
  for image classification and "Staticmethod" and "Training method".
- Add a code from "st_03.ipynb" Test a model and add a "Training config" into the code .
- Check a "artifacts" and we have a "training" folder and inside it------> model.h5

- To see a prepare_callbacks : Go to the "artifacts" folder and "prepare_callbacks" folder
  and open a "tensorboard_log_dir" for run and see a log -----> Git Bash write a commend : 
  " tensorboard --logdir=artifacts/prepare_callbacks/tensorboard_log_dir/ "

- This message appear :
  Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
  TensorBoard 2.10.0 at http://localhost:6006/ (Press CTRL+C to quit)


# Create Training :
- Go to the SRC --------> Components --------> Create a "training.py" 

## Create a entity:
- Add a code from  "st_04.ipynb" and copy "Entity" @dataclass and copy to "entity"--------> config_entity.py .
- Go to the "entity"--------> __init__.py and add a code " TrainingConfig ".


## Define a configuration manager class :
- Add a code from "st_04.ipynb" and copy code into the configuration manager def get_training_config .after that add entity code into the "from cnnClassifier.entity import" .

## Define a Training Components :
- Add a code from  "st_04.ipynb" training components and add into the "training.py" . At first add a library like: "cnnClassifier" and "tensorflow" and "pathlib" then all 
  "class Training" code into the "training.py" .

## Update the pipeline :
- I need a create a file into the "pipeline"-------> "stage_03_training.py" 
- After that go to the "components" folder and add a code into the "__init__.py" code "from cnnClassifier.components.training import Training" 
- Go to the "stage_03_training.py" and add a code "ConfigurationManager" and "PrepareCallback, Training" and "logger" .
- Go to the "stage_02_prepare_base_model.py" and copy a "class PrepareBaseModelTrainingPipeline" and modification base on new "stage_03_training.py".

- Go to the "main.py" and then add a "cnnClassifier.pipeline.stage_03_training " code  "STAGE_NAME = "Training" 
- For test a code delete a "artifacts" folder and then open a terminal "python main.py" and "training" model created .