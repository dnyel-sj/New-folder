import math

# دریافت دو عدد از کاربر
a = int(input("add aval ra vared kn : "))
b = int(input("add dovom ra vared kn : "))

# محاسبه GCD با استفاده از الگوریتم اقلیدس
gcd = math.gcd(a, b)

# چاپ GCD
print("bozorgtarin maghsom alyh moshtarak : ", gcd)
