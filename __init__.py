"""Convert epoch in milliseconds to and time to epoch milliseconds"""

from albertv0 import *

import time
from os import path

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Mills"
__version__ = "0.1"
__trigger__ = "ep "
__author__ = "Bharat Kalluri"
__dependencies__ = []

icon_path = "{}/icons/{}.svg".format(path.dirname(__file__), "clock")


def handleQuery(query):
    if query.isTriggered:
        if not query.isValid:
            return

        if query.string.strip():
            return parse_input(query.string)
        else:
            return Item(
                id=__prettyname__,
                icon=icon_path,
                text=__prettyname__,
                subtext="Type in a date for epoch or epoch for date",
                completion=query.rawString,
            )


def parse_input(query):
    try:
        int(query.replace(" ", ""))
    except:
        return Item(
            id=__prettyname__,
            icon=icon_path,
            text="Please input a integer or date in dd mm yy",
            subtext="Type in a date for epoch or epoch for date",
            completion=query.rawString,
        )
    if len(query.split(" ")) == 1:
        time_str = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(query) / 1000))
        return Item(
            id=__prettyname__,
            icon=icon_path,
            text=time_str,
            subtext="Epoch in local timezone(IST)",
            actions=[ClipAction("Copy to clipboard", str(time_str))])
    else:
        if len(query.split(" ")) != 3:
            return Item(
                id=__prettyname__,
                icon=icon_path,
                text="Input complete date",
                subtext="input date in format dd mm yy"
            )
        pattern = '%d %m %Y'
        time_str = int(time.mktime(time.strptime(query, pattern)))
        return Item(
            id=__prettyname__,
            icon=icon_path,
            text=str(time_str * 1000),
            subtext="Epoch in local timezone(IST)",
            actions=[ClipAction("Copy to clipboard", str(time_str * 1000))])
