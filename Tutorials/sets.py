# marks=set()
# print(type(marks))
# n=int(input("Enter marks of student 1: "))
# marks.add(n)
# n=int(input("Enter marks of student 2: "))
# marks.add(n)
# n=int(input("Enter marks of student 3: "))
# marks.add(n)
# print(marks)


n1={2,45,37,29,17}
n2={3,5,45,27,29,19}
n3={2,29}
print(n1.union(n2))
print(n1.intersection(n2))
print(n1.difference(n2))
print(n1.issuperset(n3))