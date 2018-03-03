#select two news article in which common vocabulary to be extracted
article1 = """ any article from source"""
article2 = """ any article from source"""

#Remove all special characters from text
article1 = article1.replace(",", "").replace("\n", "").replace('.', '').replace('"', '').replace("!","").replace("?","").casefold()
article2 = article2.replace(",", "").replace("\n", "").replace('.', '').replace('"', '').replace("!","").replace("?","").casefold()

#Split the text into words
article1_words = article1.split(" ")
print("First article words :",article1_words)
article2_words = article2.split(" ")
print("Second article words :",article2_words)

#Create vocabulary out of list of words
article1_vocab = set(article1_words)
print("First article vocabulary :",article1_vocab)
article2_vocab = set(article2_words)
print("Second article vocabulary :",article2_vocab)

#Final step to extract common vocabulary between two article
common_vocab=article1_vocab & article2_vocab
print("Common vocabulary :",common_vocab)

#Print statement after each line of code is optional but it's a good practice as it helps
#us keep track of the function of that particular line of code
