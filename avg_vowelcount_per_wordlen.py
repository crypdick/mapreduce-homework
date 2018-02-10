from mrjob.job import MRJob

class ThreeLetterWordCounter(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            yield (word, 1)

    def reducer(self, key, values):
        if len(key) != 3:
            return None
        yield (key, sum(values))

if __name__ == '__main__':
    ThreeLetterWordCounter.run()