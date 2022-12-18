from collections import Counter

values = []


def unpacking(file):
    with open(file, "r") as file:
        for value in file:
            str(value).replace(value[:-2], '')
            values.append(int(value))


def def_list_size(list):
    list_size = len(list)
    return f"The list has {list_size} values in it"


def average_value(list):
    average_value = (sum(list)/len(list))
    return f"The average of each value is {average_value}. When rounded up it is {int(average_value)}"


def most_common_value(list):
    counts = Counter(list)
    most_common = counts.most_common(1)
    return f"The most common value is '{most_common[0][0]}' occurring '{most_common[0][1]}' times"


unpacking("MOCK_DATA.csv")
print(def_list_size(values))
print(average_value(values))
print(most_common_value(values))
