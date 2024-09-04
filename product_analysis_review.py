# Task 1: Keyword Highlighter

'''
Create a program that searches through reviews list and looks for keywords such as 'good', 'excellent','bad','poor' and 'average'.
I want to Capitalize those keywords then print out each review
Print out each review with the keywords in uppercase so they stand out.

**Reviews**
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."

So for the first string in the reviews list, we want it to say: "This product is really GOOD, I'm impressed with its quallity

# # '''

def review_finder(reviews, keywords):
        updated_reviews = []

        for review in reviews: # This should run through all the reviews one by one
                for keyword in keywords:
                        if keyword in review: # This should pull my keyword from each review
                              review = review.replace(keyword, keyword.upper())  # The .replace should rplace my keywords for captital letter cause i used .upper
                updated_reviews.append(review)
        return updated_reviews


        # These will be my reviews and the keywords i want to use
reviews = [ "This product is really good. I'm impressed with its quality.",
                "The performance of this product is excellent. Highly recommended!",
                "I had a bad experience with this product. It didn't meet my expectations.",
                "the quality of the product is poor . Wouldn't recommend it to anyone.",
                "The product was average. Nothing extraordinary about it."]

keyword = ['good','excellent', 'bad', 'poor', 'average']

updated_reviews = review_finder(reviews, keyword)
for review in updated_reviews:
        print(review)


#Taks 2: Sentiment tally

'''
Develop a function that tallies the number of positive and negative words in each review. 
The function should return the total count of positive and negative words.

         positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
        negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
'''

def list_of_words(reviews, positive_words, negative_words):
    
    negative_words_count = 0
    positive_words_count = 0

    for review in reviews:
        for word in positive_words:
                positive_words_count += review.lower().count(word.lower())
        for word in negative_words:
                        negative_words_count += review.lower().count(word.lower())
    return positive_words_count, negative_words_count
        
    
# The 2 list of words that i'm going to pull my information from

positive_words = ['good', 'excellent', 'great', 'awesome', 'fantastic', 'superb', 'amazing']
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    
total_positive_words, total_negative_words = list_of_words(reviews, positive_words, negative_words)

print(f"Total positive words: ", total_positive_words)
print(f"Total negative words: ", total_negative_words)








#Task 3 Review Summary

'''
Implement a script that takes the first 30 charecters of the review and appends "..." to create a summary
Ensure that the summary does not cut off in the middle of the word

Example: "This product is really good, I'm..."
'''
for review in reviews:
    # Step 1 slice the review at the 30th char
    if len(review) > 30:
        sliced_review = review[:30]

        # Step 2 if the 30th char cuts in a word, we want to cut to the next full word so we add a condition
        if sliced_review[-1] != ' ' and review[30] != ' ':
            sliced_review = sliced_review.rsplit(' ',1)[0]

        ## Step 3 add "...' to the end of the phrase
        short_review = sliced_review + '...'
    
    else:
        short_review = review
    print(short_review)