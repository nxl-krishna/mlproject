from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''this function return the requirement '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()##reading the line implicityl ass the \n as the new line is added so i want to remove it 
        requirements= [req.replace('\n','')for req in requirements ]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements        

setup(
    name='mlproject',
    version='0.0.1',
    author='krishna',
    author_email='krishnarathore2792005@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)