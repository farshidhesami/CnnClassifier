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

## Update config.yaml :
  - Go to config folder----> config.yaml
  - create a st_01.ipynb in research folder.
  - Add data_ingestion and add Github adress :
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
  - sdf 