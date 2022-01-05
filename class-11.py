# a = input('what is your first name?\n')
# b= input('what is your last name?\n')
#
# # c = a+ " " + b
#
# print("your full name is\n", {a},{b})


n=int(input("how many persons are going to tour\n"))
total_expenses= float(input('enter your total expenses\n'))

total_donation=float(input("how much percentage you would like to donate\n"))
donated_amount=total_donation/100*total_expenses

total_amount=total_expenses+donated_amount
amount_per_each_person= total_amount/n
# amount_per_each_person= total_amount*(total_donation/n)

print(f"amount for each person:{amount_per_each_person}")
print(f"amount of donation:{donated_amount}")