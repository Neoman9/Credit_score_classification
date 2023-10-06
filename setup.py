from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="Credit_score_classification"
VERSION="0.0.0"
AUTHOR="Neoman"
DESRCIPTION="A machine learning project focused on classifying credits scores to enable financial institutions, equipped with a predictive model,that makes it easy for approval or disapproval of loans to customers ."

REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."


def get_requirements_list() -> List[str]:
    """
    Description: This function will return list of libararies listed  in the requirements.txt file 
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(), 
install_requires=get_requirements_list()
)