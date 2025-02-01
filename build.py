# -*-coding:utf8;-*-
import requests
import json
import pandas as pd
import lesley
import datetime
from bs4 import BeautifulSoup


def update_title(file_path: str, new_title: str) -> None:
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    if soup.title:
        soup.title.string = new_title
    else:
        head_tag = soup.head
        if head_tag is None:
            head_tag = soup.new_tag("head")
            soup.html.insert(0, head_tag)

        title_tag = soup.new_tag("title")
        title_tag.string = new_title
        head_tag.append(title_tag)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(soup))


r = requests.get(
    "https://raw.githubusercontent.com/guangrei/APIHariLibur_V2/main/holidays.json"
)

js = json.loads(r.text)
del js["info"]

data = {}
for k, v in js.items():
    data[k] = v["summary"]

df = pd.DataFrame(list(data.items()), columns=["date", "label"])

df["date"] = pd.to_datetime(df["date"])
current_year = datetime.datetime.now().year
cal = lesley.plot_calendar(year=current_year, label_df=df, color="Oranges")

cal.save("index.html")
update_title("index.html", "Indonesian Holidays Calendar")
