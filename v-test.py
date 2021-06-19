# import sys
# import random 

# f = sys.argv[1]
# l = sys.argv[2]

# def check(no):
# 	# print('here def')
# 	if (no<int(f) or no>int(l)):
# 		print('not valid no')
# 		return True

# while True:
# 	try:
# 			no = int(input(f'Between {f} to {l} Guess no: '))
# 		# print(f'here1{type(no)}')

# 			if(check(no)):
# 				# print('here2')
# 				continue

# 			elif(no == random.randrange(int(f),int(l))):
# 				print('Correct Choice')
# 				# print('here3')
# 				break

# 			else:
# 				# print('here4')
# 				continue

# 	except ValueError:
# 		print(" value error")

# import pyjokes
#
# print(pyjokes.get_joke())
#
# with open('C:/Users/Tushhh/OneDrive/Desktop/hello.txt', mode='w') as my_file:
#     # print(my_file.read())
#     #     my_file.write("FO")
#     #     my_file.write("remove all")
#     #     my_file.write('Append kiya')
#     # my_file.write('new file created using IDE')
#

#
#
# print(my_file.read())
# my_file.seek(0)
# print(my_file.readline())
# print('x')
# print(my_file.readline())
# print('x')
# print(my_file.readline())

# print(my_file.readlines())

#
# my_file.close()


import unittest
import v

class Test(unittest.TestCase):

	def test1(self):
		ans = 10
		data = 5
		result = v.mult(data)
		self.assertEqual(result,ans)

	def test2(self):
		ans = 20
		data = 10
		result = v.mult(data)
		self.assertEqual(result,ans)

	def test3(self):
		ans = 10
		data = 3
		result = v.mult(data)
		self.assertEqual(result,ans)

if __name__ == '__main__' :
		print(v.__name__)
		unittest.main()

