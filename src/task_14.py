import numpy as np


def task14():
    months = [
    "січень", "лютий", "березень",
    "квітень", "травень", "червень",
    "липень", "серпень", "вересень",
    "жовтень", "листопад", "грудень"
    ]

    seasons_tuple = tuple()
    for i in range(0, len(months), 3):
        season = tuple([months[i], months[i+1], months[i+2]])
        seasons_tuple = seasons_tuple + (season,)

    print(seasons_tuple)