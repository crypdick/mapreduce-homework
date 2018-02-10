from mrjob.job import MRJob

class AvgNVowelsPerWordlen(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            yield (len(word), word)

    def reducer(self, key, words):
        num_words = 0
        num_vowels = 0
        for word in words:
            num_words += 1
            for char in list(word):
                if char.lower() in 'aeiou':
                    num_vowels += 1

        yield (key, num_vowels/num_words)

if __name__ == '__main__':
    AvgNVowelsPerWordlen.run()