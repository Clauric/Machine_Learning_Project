# Machine_Learning_Project

## Table of Contents
  * [Introduction](#Introduction)
  * [Technologies and Libraries](#Technologies-and-Libraries)
  * [Setup](#Setup)
  * [Research](#Research)
  * [Questions Asked](#Questions-Asked)
  * [Status](#Status)
  * [Other Information](#Other-Information)
  
  ## Introduction
This ReadMe, and the associated files in this git repository, were written for assignment in the Machine Learning module, as part of a Higher Diploma in Science (Data Analytics). The specific questions to be answered are listed in the Questions Asked section below.

## Technologies and Libraries
### Main Platform
* Python 3.7.9

### External libraries
These are libraries that are not normally part of the standard installation with Python, and will need to be installed prior to running some of these scripts. The questions that the libraries are needed for is listed after the library name.

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Joblib](https://joblib.readthedocs.io/en)
* [Matplotlib.pyplot](https://matplotlib.org/)
* [NumPy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [PrettyTable](https://pypi.org/project/prettytable/)
* [SciPy](https://www.scipy.org/)
* [SciKitLearn](https://scikit-learn.org/stable/)

## Running the website
There is a html file in the <a href="/static">Static</a> that is the front end of power predicition application.

After downloading this repository, there are a number of ways that the user can run the power predictions application.

1) Open the command prompt, and go to the location that this depository is stored on your machine. From there, type in the following commands:
    a) Windows:
        * set FLASK_APP=Power_Est.py
        * python -m flask run

    b) Linux:
        * export FLASK_APP=Power_Est.py
        * python3 -m flask run

    After this, the user should be able to access the operational html file at: http://127.0.0.1:5000/

    c) Docker:
        * docker build . -t power-image
        docker run --name power-container -d -p 5000:5000 power-image
        
## Research
Research for the assignment was conducted through extensive internet research. A bibliography for each task is included in Jupyter Notebook, at the end of each section.

## Questions Asked
The assignment was broken into 4 parts. The specific tasks are listed in the notebook, and are summarised as follows:
1. Print the square root of 2 to 100 decimal places without the importation of any libraries.
2. Discuss the Chi-squared test for independence, and reproduce the results of the given test.
3. Discuss standard deviation, the difference between populationa and standard deviation with relation to accuracy of the estimate, and provide an example.
4. Explain k-means clustering with regards to the Fisher's Iris dataset, and discuss the implications.

## Note on task 4
The code for task #4 was originally written in the week of November 30th, 2020. The task was subsequently changed to be a question on K-nearest neighbour (KNN), as oppesed to k-means. However, by the time that the change in the task was clarified, 95% of the write-up, and 100% of the code had been completed and committed to the notebook. As such, it was not changed to reflect the change in the question.

## Status
The status of this project is complete. As there is a submission date of the 18th December, 2020, the files will not be altered, from their current format, after that date. Where the last push/alter date is prior to the 18th December, 2020,, that date can be viewed as the completion date.
 
## Other Information
### About the Author
The author is a student of the Galway Mayo Institute of Technology, studying for a Higher Diploma in Science (Data Analytics). In addition, they work as a consultant in the financial services sector in Ireland, focusing on data migrations, and system replatforming for Irish and international financial institutions.

### Contact
The author can be contacted using Clauricaune@gmail.com.