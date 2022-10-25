"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
   read_numbers(5)
    No numbers entered

"""


def read_numbers(n: int) -> str:
    numbers = []
    i = 0
    while i < n:
        i += 1
        number = input('Write your number: ')
        if number.isdigit():
            integer = int(number)
            numbers.append(integer)

    if len(numbers) > 0:
        result = sum(numbers)/len(numbers)
        str_1 = "Avg"
        print(str_1, ': ', result)
        return str_1
    else:
        str_2 = 'No numbers entered'
        print(str_2)
        return str_2

read_numbers(3)










