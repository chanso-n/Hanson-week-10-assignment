import os

working_directory = input('What directory would you like to use? ')

os.chdir(working_directory)

filename = input('What would you like to name your file? ')

name = input('What is your name? ') + ', '
address = input('What is your address? ') + ', '
phone_number = input('What is your phone number? ')


with open(filename, 'a') as f:
    f.write(name)
    f.write(address)
    f.write(phone_number)


with open(filename, 'r') as reader:
    print(reader.read())
