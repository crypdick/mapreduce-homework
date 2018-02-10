from mrjob.job import MRJob

class AlphabeticCounter(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            yield (word[0].lower(), 1)

    def reducer(self, key, values):
        yield (key, sum(values))

if __name__ == '__main__':
    AlphabeticCounter.run()