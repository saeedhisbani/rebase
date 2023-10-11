#!/usr/bin/env python
def main():
    print('main function is made by user 1 and pushed to github.com')
    func1user1()
    funcuser2()
#<<<<<<< HEAD
    func2user2()
    func3user2()
#=======
    func2user1()
#>>>>>>> 823f1f2 (user no 1 function 2)

def func1user1():
    print('Function 1 of user No 1')

def func2user1():
    print('Function 2 of user No 1')

def funcuser2():
    print('Function 1 of user No 2')

def func2user2():
    print('Function 2 of user No 2')
def func3user2():
    print('Function 3 of user No 2')

main()
