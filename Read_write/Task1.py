
word_stats={}
with open("poem.txt","r") as x:
    for line in x:
        words=line.split(' ')
        for word in words:
            if word in word_stats:
                word_stats[word]+=1
            else:
                word_stats[word]=1
print(word_stats)

word_occurances=list(word_stats.values())
max_count=max(word_occurances)
print("Maximun count of word occurances is : ",max_count)

print("Word with max occurances are :")
for word,count in word_stats.items():
    if count==max_count:
        print(word)

print(word_occurances)
print(type(word_occurances))