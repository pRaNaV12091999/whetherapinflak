from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("Data_sets/stations.txt" , skiprows=17)

variable = "Hello there"
@app.route("/")
def home():
    return render_template("home.html",data = stations)

@app.route("/api/v1/<station>/<date>")
def about(station,date):
    df = pd.read_csv("Data_sets/TG_STAID"+str(station).zfill(6)+".txt",skiprows = 20 , parse_dates = ["    DATE"])
    temperature = df.loc[df['    DATE']== date]['   TG'].squeeze()/10

    print(station)
    # temperature = 23
    return {"station":station,
            "date":date,
            "temperature":temperature
    }


@app.route("/api/v1/<station>")
def all_data(station):
    df = pd.read_csv("Data_sets/TG_STAID" + str(station).zfill(6) + ".txt", skiprows=20, parse_dates=["    DATE"])
    results = df.to_dict(orient = "records")
    return results

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station,year):
    df = pd.read_csv("Data_sets/TG_STAID" + str(station).zfill(6) + ".txt", skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient = "records")
    return result


if __name__=="__main__":
    app.run(debug=True)
