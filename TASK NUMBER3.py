


def analyze_text(text, min_length=3, ignore_stopwords=None):
    if ignore_stopwords is None:
        ignore_stopwords = []
     
    words = text.split()
    count = 0   
    
    for word in words:
        if len(word) >= min_length and  word not in ignore_stopwords:
            count += 1        
    
    return count    

result = analyze_text("Hello  Ana, How are you", min_length=3,ignore_stopwords=[])
print(result)









 
