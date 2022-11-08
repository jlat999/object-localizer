# Introduction
The aim of this project is to detect and estimate the absolute position of certain objects in the ground from an aerial system.

# Getting started 
This project is made using python3.
Please, make use of a virtual environment or a docker using the modules listed in the requirements.txt.
You can create a python virtual environment with python3-venv with:
```shell
python3 -m venv path/to/your/new/virtual_environment
```
And activate it with:
```shell
source path/to/your/new/virtual_environment/bin/activate
```
Then you can install the requirements as:
```shell
pip install -r requirements.txt
```

You can also update the '*requirements.txt*' file using:
```shell
pip3 freeze > requirements.txt
```
Please note that the '*requirements.txt*' file should also be updated when necessary with every new pull request.

# Build and Test
#TODO Document how to run the unit tests or the pipeline.

# Contribute 
To contribute to this project, clone the repository, create a new branch with your changes and add it to the main branch via a pull request.
NOTE! We make use of black formatter to keep the same format along the project and make the code review easier.

First create and go to your branch:
```sh
git checkout -b your_branch_name
```

Work on your brach and save your work as usual:
```sh
git add --all
git commit -m "mensaje explicando cambios"
git push origin your_branch_name
```
