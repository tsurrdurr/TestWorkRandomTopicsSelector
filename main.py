import random

def main():
	topics = []
	with open("topics.txt") as f:
		for line in f:
			topics.append(line);
	maxvalue = len(topics) - 1
	print("Questions found:", maxvalue)
	rn = random.randint(0, maxvalue)
	rn2 = get_non_dupe_question(topics, [rn])
	print("Your randomly chosen non-duplicating questions: ")
	print(topics[rn].strip())
	print(topics[rn2].strip())

def get_non_dupe_question(topics, dupes):
	maxvalue = len(topics) - 1
	while True:
		rn = random.randint(0, maxvalue)
		if not dupes.__contains__(rn):
			return rn

if __name__ == '__main__':main()