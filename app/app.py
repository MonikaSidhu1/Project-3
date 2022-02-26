from flask import Flask, render_template 
import pandas as pd
from prediction import predict

# create app 
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/price")
def price():
    return render_template("predict.html")

@app.route("/about")
def about():
     return render_template("about.html")

@app.route("/visualisations")
def visualisations():
     return render_template("visualisations.html")



@app.route("/api/predict/<BEDROOMS>/<BATHROOMS>/<LAND_AREA>/<CBD_DIST>/<GARAGE>/<NEAREST_SCH_RANK>/<NEAREST_STN_DIST>", methods=["GET"])
def do_predict(BEDROOMS, BATHROOMS, LAND_AREA,CBD_DIST,GARAGE,NEAREST_SCH_RANK,NEAREST_STN_DIST):
    user_input = {
        "BEDROOMS":float(BEDROOMS),
       "BATHROOMS": float(BATHROOMS),
      "LAND_AREA": float(LAND_AREA),
      "CBD_DIST":float(CBD_DIST),
       "GARAGE" :float(GARAGE),
     "NEAREST_SCH_RANK":float(NEAREST_SCH_RANK),
    "NEAREST_STN_DIST": float(NEAREST_STN_DIST)
    }
    prediction = predict(user_input)[0][0].round(2)


    return {"prediction": prediction}

if __name__ == "__main__":
    app.run(debug=True)

