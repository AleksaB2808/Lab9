import re

def task1(s):
    return bool(re.match(r'^[a-z0-9]+$', s))

def task2(s):
    return bool(re.search(r'[A-Z]', s))

def task3(s):
    return bool(re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', s))

def task4(s):
    return bool(re.match(r'^([01]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])$', s))

def task5(s):
    return bool(re.match(r'^\d{5}(?:[-\s]\d{4})?$', s))

def task6(s):
    return bool(re.match(r'^[a-z0-9_-]{6,12}$', s))

def task7(s):
    return bool(re.match(r'^[456]\d{3}(-?\d{4}){3}$', s))

def task8(s):
    return bool(re.match(r'^\d{3}-\d{2}-\d{4}$', s))

def task9(s):
    return bool(re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%]).{8,}$', s))

def task10(s):
    return bool(re.match(r'^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$', s))
