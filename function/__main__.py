import pywhatkit
import main.excel2 as excel2
import time

def try1():
    import main.excel as excel
    number = input('ok! which song or singer----')
    excel.data_entry(number)
    pywhatkit.playonyt(number)


def try2():
    excel2.anything('data')


while True:
    print("1.play music \n2.play music from database \n3.exit\n")
    var = int(input("Enter your choice: "))
    if var == 1:
        try1()
        time.sleep(5)
    elif var == 2:
        try2()
        time.sleep(5)
    elif var == 3:
        exit()

# while True:
#     var = input("type __type__or history __hist__ ")
#     if var == "type":
#         try1()
#     elif var == "hist":
#         try2()                                          
#     elif var == "HIST":
#         try2()
#     elif var == "TYPE":
#         try1()
#     else:
#         break