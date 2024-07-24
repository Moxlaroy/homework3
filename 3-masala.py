class RepeatString:
    @staticmethod
    def repeat_words(S):
        words = S.split()
        repeated_words = []
        for word in words:
            count = words.count(word)
            if count > 1 and word not in repeated_words:
                repeated_words.append(word)

        return repeated_words



S = "python java python php python c++ javascript python"
result = RepeatString.repeat_words(S)
print(result)
