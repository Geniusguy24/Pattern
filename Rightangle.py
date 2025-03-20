print("Half Pyramid pattern of stars:")
n = int(input("Please Enter a number:"))

for i in range(n):
    for j in range(i+1):
        print("* ", end= "")
    print()
