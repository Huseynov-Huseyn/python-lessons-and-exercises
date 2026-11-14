from Person import Person

p1 = Person("Emil", 25, "Huseynov")
print(p1.name)
# print(p1.__age)  # This will cause an error, because age is private
print(p1.get_age)
p1.set_age = 20
# This is how Python mangles the name:
print(p1._Person__age)  # Not recommended!

print(p1.birth_year)
