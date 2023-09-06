from os import system, name


def clear():
    # for windows the name is "nt"
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')