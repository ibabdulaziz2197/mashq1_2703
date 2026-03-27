# 1
a = 10
res = "Musbat" if a > 0 else "Manfiy"

print(res)

# 2
a = 5
res = "Juft" if a > 5 else "Toq"

print(res)


# 3
max_num = lambda a, b: a if a > b else b

print(max_num(155, 22))



# 4
f = lambda x: "Musbat" if x > 0 else "Manfiy"

print(f(12))


# 5
f = lambda x: x*2 if x > 10 else x

print(f(22))


# 6
f = lambda x: x/2 if x % 2 == 0 else x * 3

print(f(15))


# 7
a = lambda a, b: a if a < b else b

print(a(4, 22))


# 8
f = lambda x: "OK" if x % 5 == 0 else "NO"

print(f(22))


# 9
f = lambda x: 100 if x > 100 else x

print(f(12404))


# 10
f = lambda x: -x if x < 0 else x

print(f(-41))
