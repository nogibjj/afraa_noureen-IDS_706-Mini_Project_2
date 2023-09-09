# IDS_706 - Data Engineering Systems 
## Mini-Project 2 : Pandas Descriptive Statistics Script

[![CI](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/actions/workflows/cicd.yml)

***

### Goal of the Project
Mini-Project 2 modifies [this existing Github template](https://github.com/afraa-n/IDS_706-Data_Engineering_Systems) by handling the loading and manipulation of a movies dataset stored in a `.csv` file using the Pandas library. This entails extracting meaningful insights from the dataset by generating descriptive statistics.

The core functionality of this project involves identifying and presenting the movies with the highest ratings from the dataset. 

The accompanying Makefile automates essential development tasks, making it easier for developers to maintain code quality, run tests, and streamline the development workflow.

Dataset used: [Top-Rated Movies Data Set](https://www.kaggle.com/datasets/khalidalam980/top-rated-movies-data-set)

***

### Commands to Run the Repo

To run the project, you can use the Makefile and follow these commands:
1. ```
   # To install the required the python packages
   make install
   ```
2. ```
   # To check code style
   make lint
   ```
3. ```
   # To run tests
   make test
   ```
4. ```
   # To format the code
   make format
   ```
5. ```
   # To perform all the above tasks (install, test, format, lint)
   make all
   ```

***

### Result

1. On running ```make lint```:

![make lint](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/5c6d0c64-96d7-4860-aea1-7a65990d3ae8)

2. On running ```make test```, it passes the test:

![make test](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/099f4e59-e08c-48b8-8a46-93bdf96c0846)

3. On running ```make format```:

![make format](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/af82026d-b8d0-44ac-a9ca-342f73be980a)

***

### Output from test_main.py

On running test_main.py, it displays the descriptive statistics from the dataset as well as the top rated movies. It also ensures that there is a valid value returned from display_highest_votes() (from main.py) using the assert statement.

![test_main](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/8258a08c-2b19-464b-9e7d-b01ed3870adf)

***
