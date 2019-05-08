def color(c):
    color_code = {"red": "31", "green": "32","yellow":"33" , "blue":"34", "purple":"35" , "white":"30"}

    def decorator(f):
        def inner(*args):
            res = "\033[" + color_code[c] + ";0m" + str(f(*args)) + "\033[0m"
            return res
        return inner
    return decorator





@color("blue")
def echo(s):
    return s


print(echo("hello"))
