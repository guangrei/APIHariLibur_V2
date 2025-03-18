# -*-coding:utf8;-*-
import json
import pandas as pd
import lesley  # type: ignore[import-untyped]
import datetime
from bs4 import BeautifulSoup
from typing import Dict, Any


class generate_html_calendar:
    def __init__(
        self,
        json_path: str,
        save_path: str,
        title: str = "Indonesian Holidays Calendar",
    ) -> None:
        self.json_path = json_path
        self.save_path = save_path
        self.title = title
        self.generate()

    def generate(self) -> None:
        with open(self.json_path, "r") as f:
            js = json.loads(f.read())
            del js["info"]

        data: Dict[str, Any] = {}
        for k, v in js.items():
            data[k] = v["summary"]

        df = pd.DataFrame(list(data.items()), columns=["date", "label"])

        df["date"] = pd.to_datetime(df["date"])
        current_year = datetime.datetime.now().year
        cal = lesley.plot_calendar(year=current_year, label_df=df, color="Oranges")

        cal.save(self.save_path)
        self.update_title()

    def update_title(self) -> None:
        with open(self.save_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        if soup.title:
            soup.title.string = self.title
        else:
            head_tag = soup.head
            if head_tag is None:
                head_tag = soup.new_tag("head")
                soup.html.insert(0, head_tag)  # type: ignore[union-attr]

            title_tag = soup.new_tag("title")
            title_tag.string = self.title
            head_tag.append(title_tag)

        with open(self.save_path, "w", encoding="utf-8") as file:
            file.write(str(soup))


if __name__ == "__main__":
    from PhantomBrowser import Browser

    browser = Browser()
    jf = browser.download(
        "https://raw.githubusercontent.com/guangrei/APIHariLibur_V2/main/holidays.json",
        folder="/tmp",
        overwrite=True,
    )
    generate_html_calendar(jf, "index.html")
