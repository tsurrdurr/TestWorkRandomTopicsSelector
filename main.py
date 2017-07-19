import random

def main():
	topics = []
	with open("topics.txt") as f:
		for line in f:
			topics.append(line);
	maxvalue = len(topics) - 1
	print(maxvalue)
	rng = random.randint(0, maxvalue)
	print(topics[rng].strip())
	while True:
		rng2 = random.randint(0, maxvalue)
		if rng2 != rng:
			break
	print(topics[rng2].strip())

if __name__ == '__main__':main()