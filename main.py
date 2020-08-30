import datetime
import os


def run(command):
    print("What time do you want to shutdown/reset Computer?")
    h = int(input("Hour: (0-24)"))
    m = int(input("Minute: (0-60)"))
    s = int(input("Second: (0-60)"))
    while True:
        x = datetime.datetime.now()
        if h == x.hour and m == x.minute and s == x.second:
            os.system(command)

sdasdasdas
def main():
    print("What do you want to do?", "1. Shutdown", "2. Restart", "3. Exit")
    command = input("You chose: ")
    if command == "1":
        run("shutdown /s /t 1")
    elif command == "2":
        run("shutdown /r /t 1")
    elif command == "3":
        exit()
    else:
        exit()


main()
