# a = int(input("enter your percentage"))
#
# if a ==40:
#     print("you failed")
# elif a ==60:
#     print("you got first second class")
# elif a==70:
#     print("you got first class")
# elif a==80:
#     print("congratulation,you got distiction")
# else:
#     print("enter proper percentage")
# print("bye")

# restauren menu

veg = ['curd rice', 'veg biryani','dosa','idly']
non_veg=['chcken biryani', 'tandoori', 'mutton biryani','fish']
waiter=input('sir you want veg or non veg?')
if waiter=='veg':
    waiter2=input("this is veg menu select your item")
    if waiter2 in veg:
        print("sir this is your item")
    else:
        print("there is no item")
elif waiter=='non veg':
    waiter3=input("sir this is your non-veg menu, select item")
    if waiter3 in non_veg:
        print("sir this is your item")
    else:
        print('there is no item')

print("thank you for visiting our restaurent")


