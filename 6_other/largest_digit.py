"""
File: largest_digit.py
Name: QiaosiPan
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	if n < 0:
		n = -n		# if n < 0, need to make it < 0 first.
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, max_c):
	if n == 0:
		return max_c
	else:
		c = n % 10			# n divided by 10 and the remainder will be the last number of n
		if c > max_c:
			max_c = c		# check if c is the maximum number
		return find_largest_digit_helper((n-c)//10, max_c)		# use recursive to search each digit


if __name__ == '__main__':
	main()
