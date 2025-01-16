import re

def split_text_by_words(text, max_words=80):
    """
    Splits a text into chunks such that each chunk contains at most `max_words`.
    The splitting is done at sentence boundaries (., ?, !, or newlines).

    :param text: The text to be split.
    :param max_words: The maximum number of words allowed in each chunk.
    :return: A list of text chunks.
    """
    sentences = re.split(r'(\.|\?|!|\n)', text)  # Split text while retaining punctuation
    chunks = []
    current_chunk = ""

    # Iterate over pairs: (sentence, punctuation) in steps of 2
    for i in range(0, len(sentences) - 1, 2):
        sentence = sentences[i].strip()
        punctuation = sentences[i + 1].strip() if i + 1 < len(sentences) else ""
        combined_sentence = sentence + punctuation

        if not combined_sentence.strip():
            # Skip empty strings
            continue

        # Count words to decide if we need a new chunk
        if len(current_chunk.split()) + len(combined_sentence.split()) <= max_words:
            if current_chunk:
                current_chunk += " " + combined_sentence
            else:
                current_chunk = combined_sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = combined_sentence

    # Append the last chunk
    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks
