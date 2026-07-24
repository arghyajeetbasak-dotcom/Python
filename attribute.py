class attribute:
    a=1
object=attribute()
object.a=0
print(object.a)
print(attribute.a)
print(__name__)