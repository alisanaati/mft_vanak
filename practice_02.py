# Question_1

duration = []
data = [50.3, 338.4, 626.5, 959.4, 1317.9, 1716.7, 2134.3, 2565.5, 3085.6, 3626.7]
for i in range(0, 9):
    res = (data[i + 1] - data[i])
    duration.append(res)
print(duration)

# Question_2

T1 = 300
T2 = 400
data = [50.3, 338.4, 626.5, 959.4, 1317.9, 1716.7, 2134.3, 2565.5, 3085.6, 3626.7]
duration = []
for i in range(0, 9):
    res = (data[i + 1] - data[i])
    duration.append(res)
text = ""
for j in range(0, 9):
    if duration[j] <= T1:
        text = text + "S"
    elif duration[j] >= T2:
        text = text + "L"
    else:
        text = text + "M"
print(text)

# Question_3

# سوال نا مفهوم بود، منظورشو نفهمیدم:/


# Question_Of_Soldiers

queue = "<<<<><<><"
lst = []
lst_index = []
for i in range(0,len(queue)):
    lst.append(queue[i])
for j in range (0,len(lst)):
        if lst[j] == ">":
                lst_index.append(j)
print(lst_index)


