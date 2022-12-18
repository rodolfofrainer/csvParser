values = []
with open("MOCK_DATA.csv", "r") as file:
    for value in file:
        str(value).replace(value[:-2], '')
        values.append(int(value))

print(values)
