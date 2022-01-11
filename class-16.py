# finding trssure box
import random

path = ['left', 'right']
path_select= random.choice(path)
# print(path_select)

stage2= ['swim', 'boat']
stage2_select=random.choice(stage2)
# print(stage2_select)

stage3 = ['red', 'yellow','blue','green']
stage3_select= random.choice(stage3)
# print(stage3_select)

a = input("select your path, left or right\n")

if a!=path_select:
    print("you lost game, you are a meal for evil")
elif a ==path_select:
    a2= input("enter your choice of transport, swim or boat")
    if a2!=stage2_select:
        print("you lost game")
    elif a2==stage2_select:
        a3=input("enter corrct room color, red, green, yellow, blue\n")
        if a3!=stage3_select:
            print("you lost game, dont worry you have atleast evil powers")
        elif a3==stage3_select:
            print("yes you made it ...this is tresssure room and get it")