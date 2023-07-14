# Setup IDE VSCode
## Download and install

## Setup Python
### venv 
Python 3.8.10 or 3.9

## PyBricks
Setup PyBricks for use in development for code completion.
'''
pip install pybricks==3.1.0
'''



# About Python
## Paths
Python looks for modules in:
* local directory
* path

know your path using:
import os
print(os.path)

These locations are combined together.  You could have 2 folders of the same name and the files (modules) will be included.  This is called your namespace.

If you use an __init__.py file, this will designate a default package and this will cause the folder with the __init to be included and the other matching dir on the path to be rejected.  This creates a package.

## know the imports you have
'''
pip freeze > requirements.txt
'''


