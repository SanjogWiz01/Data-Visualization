import json
import random

data = [
    {"id": 1, "name": "Sanjog  ", "age": 21, "salary": "45000", "city": "Pokhara", "join_date": "2023-01-10"},
    {"id": 2, "name": "Aayush", "age": "", "salary": "50000", "city": "kathmandu", "join_date": "2022-12-05"},
    {"id": 3, "name": "Ramesh", "age": 25, "salary": "not_known", "city": "Lalitpur ", "join_date": "2023/02/15"},
    {"id": 4, "name": "Sita", "age": 22, "salary": "38000", "city": "Pokhara", "join_date": "invalid"},
    {"id": 5, "name": "Hari", "age": None, "salary": "60000", "city": "Biratnagar", "join_date": "2021-11-20"},
    {"id": 6, "name": "Gita ", "age": 24, "salary": "52000", "city": "kathmandu", "join_date": "2020-06-01"},
    {"id": 7, "name": "Bikash", "age": 23, "salary": "49000", "city": "Pokhara", "join_date": "2023-03-12"},
    {"id": 8, "name": "Manish", "age": 28, "salary": "1000000", "city": "Butwal", "join_date": "2022-05-19"},
    {"id": 9, "name": "Nisha", "age": 26, "salary": "47000", "city": "Dharan", "join_date": "2021-09-25"},
    {"id": 10, "name": "Kiran", "age": 24, "salary": "51000", "city": "Pokhara", "join_date": "2023-01-10"},
    {"id": 11, "name": "Sanjog  ", "age": 21, "salary": "45000", "city": "Pokhara", "join_date": "2023-01-10"},
    {"id": 12, "name": "Prakash", "age": "", "salary": "48000", "city": "Birgunj", "join_date": "2022-10-14"},
    {"id": 13, "name": "Anita", "age": 22, "salary": None, "city": "Janakpur", "join_date": "2021-08-09"},
    {"id": 14, "name": "Deepak", "age": 27, "salary": "55000", "city": " Kathmandu", "join_date": "2020-12-31"},
    {"id": 15, "name": "Sunita", "age": 23, "salary": "43000", "city": "Hetauda", "join_date": "wrong"},
    {"id": 16, "name": "Nabin", "age": 29, "salary": "65000", "city": "Pokhara", "join_date": "2019-04-22"},
    {"id": 17, "name": "Alina", "age": None, "salary": "47000", "city": "Dhangadhi", "join_date": "2021-07-17"},
    {"id": 18, "name": "Roshan", "age": 26, "salary": "52000", "city": "Butwal", "join_date": "2022-03-30"},
    {"id": 19, "name": "Puja", "age": 24, "salary": "48000", "city": "Pokhara", "join_date": "2023-02-01"},
    {"id": 20, "name": "Suman", "age": "", "salary": "50000", "city": "kathmandu", "join_date": "2021-05-11"}
]

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("data.json file created successfully")