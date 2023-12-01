import sys

sum = 0
digits = {
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9
}

# We want to check our strings backwards if it's at the end of the line.
def reverse_process_string(string):
	built_string = ''
	string_list = list(string)
	while len(string_list) > 0:
		built_string = string_list.pop() + built_string
		for num in digits:
			if num in built_string:
				return digits[num]

# We want to check our strings forwards if it's at the beginning of the line.
def forward_process_string(string):
	built_string = ''
	for c in string:
		built_string+=c
		for num in digits:
			if num in built_string:
				return digits[num]

# Process each line.
def process_line(line):
	global sum
	nums = []
	string = ''
	for s in line:
		if s.isdigit():
			# If we hit a digit, check for any numbers in the preceeding string.
			if not nums:
				string_num = forward_process_string(string)
				if string_num:
					nums.append(int(string_num))
			nums.append(int(s))
			string = ''
		else:
			string+=s
	# Handly any numbers in a remaining string.
	if not nums:
		string_num = forward_process_string(string)
	else: 
		string_num = reverse_process_string(string)
	if string_num:
		nums.append(int(string_num))

	new_num = str(nums[0]) + str(nums[-1])
	sum+=(int(new_num))

# Run the string processor
def process_file(file_name):
	with open(file_name) as f:
		for line in f:
			line = line.strip()
			if line == '':
				continue
			process_line(line)
	print(sum)

if len(sys.argv) > 1:
    process_file(sys.argv[1])
else:
    print('I need a file')
