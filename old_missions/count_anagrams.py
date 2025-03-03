from collections import defaultdict


def countSentences(wordSet, sentences):
    # Step 1: Group words by their sorted character form (to find anagrams)
    anagram_dict = defaultdict(set)

    for word in wordSet:
        sorted_word = ''.join(sorted(word))  # Sort letters to find anagram groups
        anagram_dict[sorted_word].add(word)

    # Convert the anagram dictionary to map word to anagram count
    word_to_anagram_count = {}
    for anagram_group in anagram_dict.values():
        for word in anagram_group:
            word_to_anagram_count[word] = len(anagram_group)

    result = []

    # Step 2: Process each sentence
    for sentence in sentences:
        words = sentence.split()
        num_sentences = 1

        for word in words:
            num_sentences *= word_to_anagram_count.get(word, 1)  # Default to 1 if no anagram exists

        result.append(num_sentences)

    return result


# Example usage:
wordSet = ["listen", "silent", "it", "is"]
sentences = ["listen it is silent"]
print(ÏSentences(wordSet, sentences))  # Output: [4]
