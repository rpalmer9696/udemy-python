temperatures = [10, -20, -289, 100]
LOWEST_TEMP = -273


def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c*9/5+32
        return f


with open('text.txt', 'w') as file:
    [file.write(str(c_to_f(i)) + "\n") for i in temperatures if i > LOWEST_TEMP]
