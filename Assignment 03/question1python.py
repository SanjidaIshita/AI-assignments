def sumQ(A, I, T):
   if A == 0:
       return 0
   elif A >= 1:
       return sumQ(A - 1, I, T) + T + (A - 1) * I


f = int(input("First Number: "))
d = int(input("Interval: "))
n = int(input("Total Terms: "))

print("Series Sum: ", sumQ(n, d, f))
