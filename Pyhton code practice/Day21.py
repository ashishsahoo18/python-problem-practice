def transform_sentence(sentence: str) -> str:
    words = sentence.split()

    for i, word in enumerate(words):
        result = [word[0]]  # first character unchanged

        for j in range(1, len(word)):
            previous = word[j - 1].lower()
            current = word[j]

            if previous < current.lower():
                result.append(current.upper())
            elif current.lower() < previous:
                result.append(current.lower())
            else:
                result.append(current)

        words[i] = "".join(result)

    return " ".join(words)