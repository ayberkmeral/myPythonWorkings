with open("story.txt","r") as f:
    story=f.read()

words=set() #set in order to make words unique list would be duplicate
start_of_the_word=-1 # index -1 ise başını bulamadık demek

target_start="<"
target_end=">"

for i,char in enumerate(story):
    if char==target_start:
        start_of_the_word=i

    if char==target_end and start_of_the_word !=-1:
        word=story[start_of_the_word:i+1]
        words.add(word)
        start_of_the_word=-1

answers={}

for word in words:
    answer=input(f"enter a word for {word}: ")
    answers[word]=answer


for word in words:
    story.replace(word,answers[word])

print(story)

