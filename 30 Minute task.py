import datetime


def Birth_Year(age):
    return int(datetime.datetime.now().strftime('%Y')) - int(age) - 1

name = input('What is your name?  ').capitalize()
age = input("How old are you ?  ")

print("OMG {}, you are {} years old so you were born in {} ".format(name, age, Birth_Year(age)))
