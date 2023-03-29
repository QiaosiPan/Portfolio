"""
File: boggle.py
Name: QiaosiPan
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	while True:
		row = user_input()
		if row is False:
			break
		word_set = read_dictionary(row)
		start = time.time()
		####################
		all_word = set()
		start_point(all_word, row, word_set)
		print('There are ', len(all_word), ' words in total.')
		####################
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def word_check(check, word_set):
	if check in word_set:
		print('True')


def read_dictionary(row):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	word_set = set()
	row_set = set(''.join(row))
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			# filter len(line) <= 4 & the line w/o any ele in row to reduce the word_set size
			if len(line) >= 4:
				for ele in row_set:
					if ele in line:
						word_set.add(line)
	return word_set


def has_prefix(sub_s, word_set):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param word_set:
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_set:
		if word.startswith(sub_s):
			return True
	return False


def user_input():
	input_info = '1234'
	user_row = []
	for i in range(4):
		s = input_info[i] + ' row of letters: '
		row = input(s).lower()
		# check if format of user input is legal
		if len(row) != 7:
			print('Illegal input')			# check length
			return False
		for j in range(7):
			if j % 2 == 1 and row[j] != ' ':
				print('Illegal input')		# check if there a space between each ele
				return
			elif j % 2 == 0 and not row[j].isalpha():
				print('Illegal input')		# check if each ele is alpha
				return
		user_row.append(''.join(row.split()))		# put each row into a list
	return user_row


def start_point(all_word, row, word_set):
	# choose the start point
	for x in range(4):
		for y in range(4):
			searching(row[x][y], all_word, x, y, [(x, y)], row, word_set)


def searching(word, all_word, cur_x, cur_y, index, row, word_set):
	# base case
	if len(word) >= 4 and word not in all_word and word in word_set:
		all_word.add(word)
		print('Found "', word, '"')
		# search if there is a longer one after an answer is found
		searching(word, all_word, cur_x, cur_y, index, row, word_set)
	else:
		for i in [-1, 0, 1]:
			for j in [-1, 0, 1]:
				cur_x += i
				cur_y += j
				if (cur_x, cur_y) not in index and 0 <= cur_x <= 3 and 0 <= cur_y <= 3:
					# choose
					index.append((cur_x, cur_y))
					word += row[cur_x][cur_y]
					if has_prefix(word, word_set):
						# explore
						searching(word, all_word, cur_x, cur_y, index, row, word_set)
					# un-choose
					index.pop()
					word = word[:-1]
					cur_x -= i
					cur_y -= j
				else:
					cur_x -= i
					cur_y -= j


if __name__ == '__main__':
	main()
