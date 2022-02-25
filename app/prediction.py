# create a prediction function 
import pandas as pd
import joblib
def predict( user_inputs):
    model = joblib.load("static/py/model.sav")
    X_scaler = joblib.load("static/py/x_scaler.sav")
    y_scaler  = joblib.load("static/py/y_scaler.sav")



    # get the user input data 
    BEDROOMS = user_inputs["BEDROOMS"]
    BATHROOMS= user_inputs["BATHROOMS"]
    LAND_AREA= user_inputs["LAND_AREA"]
    CBD_DIST= user_inputs["CBD_DIST"]
    GARAGE = user_inputs["GARAGE"]
    NEAREST_SCH_RANK = user_inputs["NEAREST_SCH_RANK"]
    NEAREST_STN_DIST = user_inputs["NEAREST_STN_DIST"]


    # store the input values into df 
    input_df = pd.DataFrame({
        "BEDROOMS":[BEDROOMS],
        "BATHROOMS": [BATHROOMS],
        "LAND_AREA": [LAND_AREA],
        "CBD_DIST":[CBD_DIST],
        "GARAGE" :[GARAGE],
        "NEAREST_SCH_RANK":[NEAREST_SCH_RANK],
        "NEAREST_STN_DIST": [NEAREST_STN_DIST]})




    # scale the X input df 
    X_scaled = X_scaler.transform(input_df)

    # obtain prediction (y) 
    prediction_scaled = model.predict(X_scaled)

    # scale prediction to human readable terms i.e. celcius 
    prediction = y_scaler.inverse_transform(prediction_scaled)
    return prediction 