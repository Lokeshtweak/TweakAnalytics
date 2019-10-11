# tpl=(1,2,3,4,5,6,7)
# a=iter(tpl)
# print(next(a))
# print(next(a))
# for i in a:
#     print(i)
# for fruit in ['apple','banana','mango']:
#     print("I like",fruit)
# class MyNumbers:
  # def __iter__(self):
  #   self.a = 1
  #   return self
  #
  # def __next__(self):
  #   x = self.a
  #   self.a += 1
  #   return x

# myclass = MyNumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# # print(next(myiter))
#
#
# class mynumbers:
#   def __iter__(self):
# #     self.a = 1
# #     return self
# #
# #   def __next__(self):
# #     if self.a <= 20:
# #       x = self.a
# #       self.a += 1
# #       return x
# #     else:
# #       raise StopIteration
# #
# # p1=mynumbers()
# # p=iter(p1)
# #
# # for x in p:
# #     print(x)
#
#
# mytuple = ("apple", "banana", "cherry","mango")
# myit = mytuple
# for x in myit:
#
#  print("i like "+x)


#  def fact(x):
#    if x == 1:
#      return 1
#    else:
#      result = x * fact(x - 1)
#      return result
# print(fact(10))
# x = int(10)
# print(fact(x))

def fact(c):
  if c == 1:
    return 1
  else:
    result = c + fact(c -1 )
    return result
print(fact(11))