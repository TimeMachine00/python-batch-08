your_name = input("enter your name\n")

partner_name= input("enter your partner name\n")

t1, t2 = your_name.count('t'), partner_name.count('t')
r1, r2 = your_name.count('r'), partner_name.count('r')
u1, u2 = your_name.count('u'), partner_name.count('u')
e1, e2 = your_name.count('e'), partner_name.count('e')

a = str(t1+t2+r1+r2+u1+u2+e1+e2)

l1, l2 = your_name.count('l'), partner_name.count('l')
o1, o2 = your_name.count('o'), partner_name.count('o')
v1, v2 =your_name.count('v'), partner_name.count('v')
e11, e22= your_name.count('e'), partner_name.count('e')

b = str(l1+l2+o1+o2+v1+v2+e11+e22)

c= int(a+b)

if c >80:
    print("you both are good you can go for honeymoon")
elif c >60 and c<70:
    print("your pair is above average")
elif c>50 and c <60:
    print("your pair is ok")
else:
    print("your pair is not good")