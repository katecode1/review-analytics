data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('loading finished!',len(data),'record')


average = []
for words in data:
	average.append(len(words))
k = sum(average) / len((data))
print(k)
