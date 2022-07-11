data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('loading finished!',len(data),'record')


sum_len = 0
for words in data:
	sum_len = sum_len + len(words)
print(sum_len/len(data))	


new = []
for words in data:
	if len(words) < 100:
		new.append(len(words))
print('Total:',len(new),'records and the lenth of record less 100')	