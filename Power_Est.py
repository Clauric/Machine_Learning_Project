import flask as fl
import numpy as np
import joblib

app = fl.Flask(__name__)                                        # Create a new web app.

@app.route("/")                                                 # Add root route.
def home():                                                     # Home page
    return app.send_static_file("Front_Page.html")              # Return the index.html file

@app.route("/api/Lin/<float:speed>", methods = ["GET"])         # If the Linear Regression button is chosen
def Lin_Reg(speed):                                             # Call the linear regression function
    lin_model_load = joblib.load("Models/lin_reg.pkl")          # Reimport the linear regression model
    power_est = np.round(lin_model_load.predict([[speed]])[0], 3)   # Use the linear regression model to estimate the power for the user inputted speed
    power_est = str(power_est)                                  # Convert the power estimates to strings
    return (power_est)                                          # Return the power estimate

@app.route("/api/RFR/<float:speed>", methods = ["GET"])         # If the Random Forest Regression button is chosen
def RFR_Reg(speed):                                             # Call the random forest regression function
    RFR_model_load = joblib.load("Models/RFR.pkl")              # Reimport the random forest regression model
    power_est = np.round(RFR_model_load.predict([[speed]])[0], 3)   # Use the random regression model to estimate the power for the user inputted speed
    power_est = str(power_est)                                  # Convert the power estimates to strings
    return (power_est)                                          # Return the power estimate

@app.route("/api/DTR/<float:speed>", methods = ["GET"])         # If the Decision Tree regression button is chosen
def DTR_Reg(speed):                                             # Call the Decision Tree regression function
    DTR_model_load = joblib.load("Models/DTR.pkl")              # Reimport the Decision Tree regression model
    power_est = np.round(DTR_model_load.predict([[speed]])[0], 3)   # Use the Decision Tree regression model to estimate the power for the user inputted speed
    power_est = str(power_est)                                  # Convert the power estimates to strings
    return (power_est)                                          # Return the power estimate

@app.route("/api/SIG/<float:speed>", methods = ["GET"])         # If the Sigmoid Analysis button is chosen
def SIG_Reg(speed):                                             # Call the Sigmoid Analysis function
    def sigmoid(x, L ,x0, k, b):                                # Function to define the sigmoid
        y = L / (1 + np.exp(-k*(x-x0)))+b                       # Sigmoid formula
        return y                                                # Return the coefficients for the sigmoid curve
    
    value = np.round([[speed]][0], 3)                           # Fix array issue for inputted speed and round
    popt = np.genfromtxt("Models/popt.csv", delimiter = ",")    # Reimport the optimised values for the sigmoid curve    
    power_est = np.round(sigmoid(value, *popt)[0], 3)           # Use the Sigmoid Analysis model to estimate the power for the user inputted speed
    power_est = str(power_est)                                  # Convert the power estimates to strings
    return (power_est)                                          # Return the power estimate
