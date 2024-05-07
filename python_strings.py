#QUESTION 1

#Task 1 Part 1
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!","I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
keywordss = ["good", "excellent", "bad", "poor", "average"]
reviews = " ".join(python_reviews)
print(reviews)

#Part 2
product_reviews = ["The hair is really good quality." ,"Bought some hair yeesterday and honestly the hair is overpriced...", "I got hair from Abundance hair.co and it's nice and full of luster.",  "The hair is gorgeous. LOVE IT!", "Honestly the hair is trash don't reccomend."]
keywords=["good", "quality", "nice", "gorgeous", "trash", "overpriced"]

upper_case_reviews=[]
for sentence in product_reviews:
    for word in keywords:
        sentence = sentence.replace(word, word.upper())
        sentence = sentence.replace(word.title(), word.upper())
    upper_case_reviews.append(sentence)
    print(sentence)

print(upper_case_reviews)


#Task 2
# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
product_reviews = [ "The hair is really good quality and has great texture.", "Bought some hair yesterday and honestly the hair is horrible.", "It smells bad and I couldn't use it long very disapointing.", "I got hair from Abundance hair.co and it's amazing and full of luster.",  "The hair is great! Auwsome shine!", "Honestly the hair is subpar don't reccomend."]
number_of_positive = 0
number_of_negative = 0

def pos_and_neg_count():
    
    for sentence in python_reviews:
        for word in sentence.split():
            word = word.replace(".", "")
            if word.lower() in positive_words:
                number_of_positive + 1
print(f"The number of positves are {number_of_positive}.")

for sentence in python_reviews:
      for word in sentence.split():
          word = word.replace(".", "")
          if word.lower() in negative_words:
              number_of_negative += 1
print(f"The number of negatives are {number_of_negative}.")
      
      


#Task 3

#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
product_review = "The hair is really good quality and has great texture. Bought some hair yesterday and honestly the hair is horrible. It smells bad and I couldn't use it long very disapointing. I got hair from Abundance hair.co and it's amazing and full of luster. The hair is great! Auwsome shine! Honestly the hair is subpar don't reccomend."
print(product_review[:31])


#=======================================QUESTION 2: User Input Data Processor======================================================

#Task 1: Input Length Validator Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.
first_name=input("First name: ") 
last_name=input("Last name: ")
while True:
    
    if len(first_name) >= 2:
       print(len(first_name))
    if len(last_name) >= 2:
       print(len(last_name))
       break
    else:
        print("Last name must be at least 2 characters long")

print(f"Your name has been recorded as {first_name}{last_name}")

