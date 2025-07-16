# Calculating quadratic roots

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
root1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
root2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
print("Root1: ",root1)
print("Root2: ",root2)
