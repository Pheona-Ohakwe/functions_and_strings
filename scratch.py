
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!","I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]




def pos_and_neg_count():
    number_of_positive = 0
    number_of_negative = 0
    for sentence in python_reviews:
        for word in sentence.split():
            word = word.replace(".", "")
            if word.lower() in positive_words:
                number_of_positive += 1

    print(f"The number of positives are {number_of_positive}.")
    
    for sentence in python_reviews:
        for word in sentence.split():
            word = word.replace(".", "")
            if word.lower() in negative_words:
                number_of_negative += 1
                
    print(f"The number of negatives are {number_of_negative}.")
    
pos_and_neg_count()