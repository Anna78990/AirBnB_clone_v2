#!/usr/bin/python3
a = '37705d25-8903-4318-9303-6d6d336a22c1'
n = '-122.431297'
r = '0001'
at = '37.773972'
p = '300'

print("id.isalpha = {}".format(a.isalpha()))
print("longitude.isalpha = {}".format(n.isalpha()))
print("roomn.isalpha = {}".format(r.isalpha()))
print("alt.isalpha = {}".format(at.isalpha()))
print("price.isalpha = {}".format(p.isalpha()))

print("id.isnumeric() = {}".format(a.isnumeric()))
print("longitude.isnumeric() = {}".format(n.isnumeric()))
print("roomn.isnumeric() = {}".format(r.isnumeric()))
print("alt.isnumeric() = {}".format(at.isnumeric()))
print("price.isnumeric() = {}".format(p.isnumeric()))

n = float(n)
at = float(at)
p = float(p)

print("-----------")
print("longitude.is_integer() = {}".format(n.is_integer()))
print("alt.is_integer() = {}".format(at.is_integer()))
print("price.is_integer() = {}".format(p.is_integer()))
