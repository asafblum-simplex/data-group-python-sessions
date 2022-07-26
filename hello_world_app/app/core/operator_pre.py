w = 20
x = 10
y = 15
z = 2

result_1 = (w + x) * y / z
result_2 = ((w + x) * x) / z
result_3 = ((w + x) * (y / z)) ** z
result_4 = w + (x * y) / z

print('The value of (w+x)* y/z is', result_1)
print('The value of ((w+x)*x)/z is', result_2)
print('The value of ((w+x)*(y/z))**z is', result_3)
print('The value of w+(x*y)/z is', result_4)
