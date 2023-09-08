# IDS_706-Data_Engineering_Systems : Mini-Project 2

[![CI](https://github.com/afraa-n/IDS_706-Data_Engineering_Systems/actions/workflows/cicd.yml/badge.svg)](https://github.com/afraa-n/IDS_706-Data_Engineering_Systems/actions/workflows/cicd.yml)

***

#### It includes:
1. **.devcontainer**: configuration folder which contains a **Dockerfile** and **devcontainer.json**.
  - ** Dockerfile**: specifies the instructions for building a Docker container image that will be used as the development environment.
  - **devcontainer.json**: defines the settings for the development container, such as which Dockerfile to use and environment variables.
2. **Makefile**: contains a set of rules that define how to compile source code, run tests, and perform other development tasks. 
3. **requirements.txt**: lists all the external libraries and dependencies required for the project to run correctly. It is commonly used with package managers like pip to install the necessary packages and helps ensure that everyone working on the project uses the same versions of libraries, which is important for reproducibility and compatibility.
4. **workflows**: contains configuration files for defining and automating various tasks, processes, and workflows within the GitHub repository.
5. **main.py**: contains a basic function which reads a .csv file into a dataframe and returns the value from a particular cell.
6. **test_main.py**: checks if the value returned my main.py is corrrect.
7. **README**: gives developers a detailed description of the GitHub project.
8. **.gitignore**: specifies files and directories that should be ignored by Git, the version control system used by GitHub. Changes in files or directories in the .gitignore file will not be tracked by Git, and they will not be included in the version history.

***
