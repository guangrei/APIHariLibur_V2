# -*- coding: utf-8 -*-
import unittest
import json


def coba(jsfile: str) -> bool:
    try:
        with open(jsfile, "r") as f:
            json.loads(f.read())
        return True
    except BaseException as e:
        print(e)
        return False


class JsonTest(unittest.TestCase):
    def test_calendar(self) -> None:
        self.assertTrue(coba("calendar.json"))

    def test_calendarmin(self) -> None:
        self.assertTrue(coba("calendar.min.json"))

    def test_holidays(self) -> None:
        self.assertTrue(coba("holidays.json"))


if __name__ == "__main__":
    unittest.main()
