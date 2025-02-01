#-*-coding:utf8;-*-
import requests
import json
import pandas as pd
import lesley
import datetime


r = requests.get("https://raw.githubusercontent.com/guangrei/APIHariLibur_V2/main/holidays.json")

js = json.loads(r.text)
del js["info"]

data = {}
for k,v in js.items():
    data[k] = v["summary"]

df = pd.DataFrame(list(data.items()), columns=["date", "label"])

df["date"] = pd.to_datetime(df["date"])
current_year = datetime.datetime.now().year
cal = lesley.plot_calendar(year=current_year, label_df=df, color='Oranges')

cal.save("public/index.html")
