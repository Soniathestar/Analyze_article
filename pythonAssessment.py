import re


def count_specific_word(text, word):
    # counts how many times "word" shows up in "text"
    if text == "" or word == "":
        return 0

    # find all words in the text 
    word_list = re.findall(r"[A-Za-z']+", text.lower())
    word = word.lower()

    count = 0
    for w in word_list:
        if w == word:
            count = count + 1

    return count


def identify_most_common_word(text):
    if text == "":
        return None

    word_list = re.findall(r"[A-Za-z']+", text.lower())

    if len(word_list) == 0:
        return None

    # count how many times each word appears using a dictionary
    word_counts = {}
    for w in word_list:
        if w in word_counts:
            word_counts[w] = word_counts[w] + 1
        else:
            word_counts[w] = 1

    # find the word with the highest count
    most_common = ""
    highest_count = 0
    for w in word_counts:
        if word_counts[w] > highest_count:
            highest_count = word_counts[w]
            most_common = w

    return most_common


def calculate_average_word_length(text):
    if text == "":
        return 0

    word_list = re.findall(r"[A-Za-z']+", text)

    if len(word_list) == 0:
        return 0

    total_letters = 0
    for w in word_list:
        total_letters = total_letters + len(w)

    average = total_letters / len(word_list)
    return average


def count_paragraphs(text):
    if text.strip() == "":
        return 1

    # split on blank lines 
    chunks = re.split(r"\n\s*\n", text.strip())

    count = 0
    for chunk in chunks:
        if chunk.strip() != "":
            count = count + 1

    if count == 0:
        return 1

    return count


def count_sentences(text):
    if text.strip() == "":
        return 1

    # split on ., !, or ? 
    pieces = re.split(r"[.!?]+", text)

    count = 0
    for piece in pieces:
        if piece.strip() != "":
            count = count + 1

    if count == 0:
        return 1

    return count


if __name__ == "__main__":
    file = open("news_article.txt", "r")
    article_text = file.read()
    file.close()

    # Count Specific Word
    search_word = "pie"
    result1 = count_specific_word(article_text, search_word)
    if result1 > 0:
        print("The word '" + search_word + "' appears " + str(result1) + " times.")
    else:
        print("The word '" + search_word + "' was not found.")

    # Identify Most Common Word
    result2 = identify_most_common_word(article_text)
    print("The most common word is: " + str(result2))

    # Calculate Average Word Length
    result3 = calculate_average_word_length(article_text)
    print("The average word length is: " + str(round(result3, 2)))

    # Count Paragraphs
    result4 = count_paragraphs(article_text)
    print("Number of paragraphs: " + str(result4))

    # Count Sentences
    result5 = count_sentences(article_text)
    print("Number of sentences: " + str(result5))

    # check a few words using a while loop
    print("\nChecking a few words:")
    words_to_check = ["pie", "technology", "sustainability", "notaword"]
    index = 0
    while index < len(words_to_check):
        w = words_to_check[index]
        c = count_specific_word(article_text, w)
        if c > 0:
            print(w + " was found " + str(c) + " times")
        else:
            print(w + " was not found")
        index = index + 1
