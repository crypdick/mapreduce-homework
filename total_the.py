from mrjob.job import MRJob

class TheCounter(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            yield (word, 1)

    def reducer(self, key, values):
        if key != 'the':
            return None
        yield (key, sum(values))

if __name__ == '__main__':
    TheCounter.run()