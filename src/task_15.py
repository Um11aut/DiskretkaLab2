from datetime import datetime

def convert_to_datetime(date_string):
    try:
        date_format = "%d.%m.%Y"
        datetime_obj = datetime.strptime(date_string, date_format)
        
        return datetime_obj
    except ValueError:
        return None

def sort_tuple(t):
    def get_birthdate(item):
        return convert_to_datetime(item[1])

    sorted_tuple = tuple(sorted(t, key=get_birthdate))
    return sorted_tuple

def task15():
    data = (["Іванов Іван Іванович", "15.04.1990"],
        ["Петров Петро Петрович", "25.03.1985"],
        ["Сидоров Олексій Андрійович", "05.07.1995"])
    print(sort_tuple(data))