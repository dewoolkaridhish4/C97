sentence = input("Enter A Sentence = ")
charectercount=0
wordcount = 1 
for i in sentence:
    charectercount=charectercount+1
    if(i==' '):
        wordcount=wordcount+1

print("Number of charecters in the given sentence = ")
print (charectercount)
print("Number of words in the given sentence = ")
print (wordcount)