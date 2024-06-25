#voting eligibility check
name=input('enter your name : ')
print( "hello welcome:",name )

age=int(input("enter your age: "))

print(age)

if age >= 18:
    print(name + "you are eligible to vote")
else:
    print(name +'you cant vote till you turn 18')

