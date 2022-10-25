"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""

import csv
def howmanyfiles(n):
    n = int(input('Input how many files would you like to read: '))
    i = 0
    mystring = []

    while i < n:
        i += 1
        filename = input('Gimme filename: ')
        with open(filename) as opened_file:
            infile = opened_file.read()
            mystring.append(infile)

    with open('result.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(mystring)
    print(mystring)

howmanyfiles(2)