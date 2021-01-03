import time

import pyautogui


def click_function(count):
    print('starting clicks')
    pyautogui.click(clicks=count, interval=3)
    print('done')


def rightclick_function(count):
    print('eating')
    i = 0
    for i in range(count):
        pyautogui.mouseDown(button='right')
        time.sleep(3)
        pyautogui.mouseUp(button='right')
        i += 1
        print(i)


def scrolldown(count):
    pyautogui.scroll(-1)


def autorunner(count=10, eatcount=3, attackcount=500, foodcount=9):
    print('starting in 5 seconds')
    time.sleep(7)
    i = 0
    eatcounter = 0
    foodcounter = 0
    for i in range(count):
        click_function(attackcount)
        rightclick_function(eatcount)
        eatcounter += 3
        if eatcounter >= 61:
            scrolldown(1)
            eatcounter = 0
            foodcounter += 1

            if foodcounter == foodcount:
                break

    print('done running')


if __name__ == "__main__":
    loopcount = 180
    eatcount = 3
    attackcount = 500
    foodcount = 9
    useroption = input(f'''Enter "1" to run with the default values. It will attack and eat {loopcount} times. Each attack is 
    {attackcount} hits. Everytime it eats, it will try to eat {eatcount} time. It will also stop after it depletes {foodcount}
    stacks of food.
    Press "2" to change some of the settings.
          ''')

    if useroption == "1":
        autorunner()
    else:
        loopcount, eatcount, attackcount, foodcount = input(f'''Please enter the values you want to change in the 
        following order with no spaces"loopcount,eatcount,attackcount,foodcount" ''').split(',')
        autorunner(int(loopcount), int(eatcount), int(attackcount), int(foodcount))


