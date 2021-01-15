# Machine_Learning_Project

## Table of Contents
  * [Introduction](#Introduction)
  * [Technologies and Libraries](#Technologies-and-Libraries)
  * [Running the website](#Running-the-website)
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

* Open the command prompt, and go to the location that this depository is stored on your machine. From there, type in the following commands:

    a) Windows:

        * set FLASK_APP=Power_Est.py

        * python -m flask run

    b) Linux:

        * export FLASK_APP=Power_Est.py

        * python3 -m flask run

    After this, the user should be able to access the operational html file at: http://127.0.0.1:5000/

    c) Docker:

        * docker build . -t power-image

        * docker run --name power-container -d -p 5000:5000 power-image

## Research
Research for the assignment was conducted through extensive internet research. A bibliography has been included at the end of the <a href="Regression models review notebook.ipynb">jupyter notebook</a> that details all the articles consulted. Throughout the notebook, hyperlinks have been included to articles directly cited.

## Questions Asked
The assignent set was as follows:
* ... create a web service that uses machine learning to make predictions based on the data set powerproduction available on Moodle. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. You must then develop a web service that will respond with predicted power values based on speed values sent as HTTP requests. Your submission must be in the form of a git repository containing, at a minimum, the following items:
    1. <a href="Regression models review notebook.ipynb">Jupyter notebook</a> that trains a model using the data set. In the notebook you should explain your model and give an analysis of its accuracy.
    2. <a href="Power_Est.py">Python script</a> that runs a <a href="/static/Front_Page.html">web service</a> based on the model, as above.
    3. <a href="Dockerfile">Dockerfile</a> to build and run the web service in a container.
    4. Standard items in a git repository such as a README.

## Status
The status of this project is complete. As there is a submission date of the 15th January, 2021, the files will not be altered, from their current format, after that date. Where the last push/alter date is prior to the 15th January, 2021, that date can be viewed as the completion date.
 
## Other Information
### About the Author
The author is a student of the Galway Mayo Institute of Technology, studying for a Higher Diploma in Science (Data Analytics). In addition, they work as a consultant in the financial services sector in Ireland, focusing on data migrations, and system replatforming for Irish and international financial institutions.

### Contact
The author can be contacted using Clauricaune@gmail.com.
