int_numbers = range(-5, 6)
# f = filter(lambda x: x[0] == '김', int_numbers)
f = filter(lambda x: x * 2, int_numbers)
m = map(lambda x: x * 2, int_numbers)

print("f=", list(f) )
print("m=", list(m))
