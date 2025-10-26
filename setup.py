'''
This setup.py file is an essential part of my packaging and 
distributing Python project. It is used by setuptools to define the configuration 
of my project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Reading lines from the file
            lines=file.readlines()
            # Processing each line
            for line in lines:
                requirement=line.strip()
                # Ignoring empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ashwath Bala S",
    author_email="ashwathbala510@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)