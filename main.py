import time

import keyboard
import os

os.chdir('C:\Program Files (x86)\Steam\steamapps\common\Rust')

x = input("1 for crate 2 for chinook 3 for excavator: ")[0]
key = input("key to bind: ")[0]

while True:
    keyboard.wait(key)
    time.sleep(0.2)
    file = open('output_log.txt')
    gg = file.readlines()
    # matches = [match for match in gg if "laptoploop" in match]
    # if len(matches) > 1 and int(match.strip(string.ascii_letters)) > 1:
    #     print(matches[-1])

    # match = [match for match in gg if "helicopter" in match]
    # if len(match) > 1 and int(match.strip(string.ascii_letters)) > 1:
    #     print(match[-1])

    if x == "1":
        match = [match for match in gg if "laptoploop" in match]
        if not match:
            print("No crate in logfile!")
        if len(match) > 1:
            rb = match[-1]
            if int(rb[len(rb) - 2]) > -1:
                print("detected " + rb[len(rb) - 2] + " crate(s)")

    if x == "2":
        match1 = [match for match in gg if "ch47" in match]
        if not match1:
            print("No chinook in logfile!")
        if len(match1) > 1:
            rb = match1[-1]
            if int(rb[len(rb) - 2]) > -1:
                print("detected " + rb[len(rb) - 2] + " chinook(s)")

    if x == "3":
        match2 = [match for match in gg if "excavator" in match]
        if not match2:
            print("No excavator in logfile!")
        if len(match2) > 1:
            rb = match2[-1]
            print(rb)
            if int(rb[len(rb) - 2]) > -1:
                print("detected excavator running")
            else:
                print("detected no excavator running")
