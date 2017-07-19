import random
import os

def main():
	topics = []
	with open("topics.txt") as f:
		for line in f:
			topics.append(line);
	maxvalue = len(topics) - 1
	print("Questions found:", maxvalue)
	rn = get_non_dupe_question(topics, [])
	rn2 = get_non_dupe_question(topics, [rn])
	extra = get_non_dupe_question(topics, [rn, rn2])
	print("Your randomly chosen non-duplicating questions: ")
	print(topics[rn].strip())
	print(topics[rn2].strip())

	print("Press any key to get an extra question to answer without preparation: ")
	os.system("pause")
	print(topics[extra].strip())

def get_non_dupe_question(topics, dupes):
	maxvalue = len(topics) - 1
	while True:
		rn = random.randint(0, maxvalue)
		if not dupes.__contains__(rn):
			return rn

if __name__ == '__main__':main()