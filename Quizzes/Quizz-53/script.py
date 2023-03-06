class WordCounter():
    def __init__(self, text) -> None:
        for char in "-.,;:!?":
            text = text.replace(char, "")
        self.words = text.split()
    def count_words(self):
        self.results = {}
        for word in self.words:
            if word.lower() in self.results:
                self.results[word.lower()] += 1
            else:
                self.results[word.lower()] = 1
    def get_results(self):
        return self.results


text = "This is a test text. This text will be counted."
counter = WordCounter(text)
counter.count_words()
result = counter.get_results()
print(result)