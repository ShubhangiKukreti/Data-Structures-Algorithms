def reverse(input_string):
    if not input_string or len(input_string) < 2 or type(input_string) != "str":
        return "Invalid input"
    else:
        return input_string[::-1]


def reverse_two(input_string):
    if not input_string or len(input_string) < 2 or type(input_string) != "str":
        return "Invalid input"
    else:
        i = len(input_string) - 1
        new_string = ""
        while i >= 0:
            new_string += input_string[i]
            i -= 1
        return new_string


user_input = input(print("Enter a string"))

print(reverse(user_input))
