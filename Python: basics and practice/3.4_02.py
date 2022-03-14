import csv

with open("Crimes.csv") as f:
    crimes_list = csv.DictReader(f)
    crimes_list = [i["Primary Type"] for i in crimes_list]

    most_common_value = None
    sum_most_common_value = 0

    for i in set(crimes_list):
        sum = crimes_list.count(i)
        if sum > sum_most_common_value:
            sum_most_common_value = sum
            most_common_value = i

    print(most_common_value)
