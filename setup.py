from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup function
PROJECT_NAME= "housing-predictor"
VERSION="0.0.2"
AUTHOR="Devdatta"
DESCRIPTION= "This is first FSDS machine learning project"
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return a list of requirement mention in requirements.txt file

    return this function is going to return a list which contain name of libraries mentioned in requirements.txt file  
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description= DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()

)
