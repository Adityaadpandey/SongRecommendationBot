import pywhatkit
import excel2

def try1():
    import excel
    number = input('ok! which song or singer----')
    excel.data_entry(number)
    pywhatkit.playonyt(number)


def try2():

    excel2.anything()


while True:
    var = input("type __type__or history __hist__ ")
    if var == "type":
        try1()
    elif var == "hist":
        try2()                                          
    elif var == "HIST":
        try2()
    elif var == "TYPE":
        try1()
    else:
        break