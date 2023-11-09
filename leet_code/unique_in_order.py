old = ['a','b','a','d','c','b','d','i','c']

print(set(old)) 
"""order is not achived"""

"""unique"""
new = []
for i in old:
    if i not in new:
        new.append(i)

print(new)

"""alternative"""
new2 = list(dict.fromkeys(old).keys())
print(new2)