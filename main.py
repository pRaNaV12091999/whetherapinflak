from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

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

if __name__=="__main__":
    app.run(debug=True)
