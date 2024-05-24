"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
   a,b=record
   return b


def convert_coordinate(coordinate):
    return tuple(coordinate)


def create_record(azara_record, rui_record):
    if (azara_record[1])==rui_record[1][0]+rui_record[1][1]
        return azara_record+rui_record
    else:
        return "no coinciden"
