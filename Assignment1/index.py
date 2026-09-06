"""
This program takes in 4 documents and will create an inverse index of the words in the documents.
"""

def lemmatize(word): 
    """
    Lemmatize the word using a map.

    Args:
        word (str): The word to be lemmatized.
    Returns:
        str: The lemmatized form of the word.
    """

    lemmatize_map = {
        "increases": "increase",
        "rising": "rise",
        "increasing": "increase",
        "sales": "sale",
        "homes": "home"
    }

    return lemmatize_map.get(word, word)  # Return the lemmatized word if found, else return the original word


def create_inverse_index(documents):
    """ 
    Creates an inverse index in the format: {word: {doc_id: frequency}}

    Args:
        documents (dict): A dictionary of documents with their id and text
    Returns:
        dict: An inverse index in the format: {word: {doc_id: frequency}}
    """

    inverse_index = {}

    for doc_id, text in documents.items():

        # Tokenize the text into words, convert to lowercase, remove punctuation
        words = [word for word in text.lower().split()]
        words = [word.strip('.,') for word in words]  # Remove punctuation

        for word in words:
            lemmatized = lemmatize(word)

            # Update the inverse index with the lemmatized word and its frequency in the document
            if lemmatized not in inverse_index:
                inverse_index[lemmatized] = {}
            if doc_id not in inverse_index[lemmatized]:
                inverse_index[lemmatized][doc_id] = 0
            inverse_index[lemmatized][doc_id] += 1

    return inverse_index


def main():

    # Define the documents

    documents = {
        1: "New homes sale increases.",
        2: "Home sale rising in July.",
        3: "Increasing home sales in July.",
        4: "July new home sales rise."
    }

    inverse_index = create_inverse_index(documents)

    print("\nInverse Index:\n")
    for key, value in inverse_index.items():
        print(f"{key}: {value}")
    print()


if __name__ == "__main__":
    main()