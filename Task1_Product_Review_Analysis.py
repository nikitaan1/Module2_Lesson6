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


 