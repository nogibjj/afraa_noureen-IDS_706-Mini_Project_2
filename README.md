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

![make lint](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/ea6d3f8b-e4ad-46d1-ad62-0d8bef14971f)


2. On running ```make test```, it passes the test:

![make test](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/ab0e7d9a-4fc2-48ec-8889-5391c69a3503)


3. On running ```make format```:

![make format](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/d66deb88-4408-486d-b7f7-1183c9979995)

***

### Output from test_main.py

On running test_main.py, it displays the descriptive statistics from the dataset as well as the top rated movies. This file generates and displays the plot for popularity vs vote_average. It also ensures that there is a valid value returned from display_highest_votes() (from main.py) using the assert statement.

![test_main 1](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/5c6f1802-185b-4b43-9f25-a4da4ca28dfc)
![test_main 2](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/0dfdd41e-b5d3-4677-9481-5a1e3386c452)

### Data Visualization (popularity vs vote_average scatter plot)

![graph](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/476e7e81-f410-4eda-88d8-a4c3b94ef922)

***
