# Question_1
weight = input("please enter your weight in 'kilogram':")
weight = float(weight)
height = input("please enter your height in 'meter':")
height = float(height)
BMI = weight / (height * height)
if BMI < 18.5:
    print("Underweight")
if (BMI >= 18.5) and (BMI < 25):
    print("Normal")
if (BMI >= 25) and (BMI <= 30) :
    print("Overweight")
if BMI > 30 :
    print("Obesity")

# Question_2
cond = input("Do you use SI units?(please answer with 'y' or 'yes' or 'n' or 'no')")
if cond == "Y" or cond == "y" or cond == "yes" or cond == "YES":
    weight = input("please enter your weight in 'kilogram':")
    weight = float(weight)
    height = input("please enter your height in 'meter':")
    height = float(height)
    BMI = weight / (height * height)
    if BMI < 18.5:
        print("Underweight")
    if (BMI >= 18.5) and (BMI < 25):
        print("Normal")
    if (BMI >= 25) and (BMI <= 30):
        print("Overweight")
    if BMI > 30:
        print("Obesity")
if cond == "NO" or cond == "N" or cond == "n" or cond == "no":
    weight = input("please enter your weight in 'pound':")
    weight = float(weight)
    height = input("please enter your height in 'inch':")
    height = float(height)
    BMI = (weight / (height * height)) * 703
    if BMI < 18.5:
        print("Underweight")
    if (BMI >= 18.5) and (BMI < 25):
        print("Normal")
    if (BMI >= 25) and (BMI <= 30):
        print("Overweight")
    if BMI > 30:
        print("Obesity")

# Question_3
text = input("please enter your text:")
len_text = len(text)
len_text_2 = len_text / 2
len_text_2 = int(len_text_2)
left = text[:len_text_2:-1]
right = text[len_text_2: :-1]
print(left)
print(right)




