#Task 1
#Task 1

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

words = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    uppercase_review = review
    for word in words:
        if word in review:
            uppercase_review = uppercase_review.replace(word, word.upper())
    print(uppercase_review)

#Task2 

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def review_count(st):
    review = st.lower()
    pos_count = 0
    neg_count = 0
    for word in positive_words:
        if word in review:
            pos_count += 1
    
    for word in negative_words:
        if word in review:
            neg_count += 1
    return f"pos_count: {pos_count}, neg_count: {neg_count}"

