from mrjob.job import MRJob

class WordCounter(MRJob):
    def mapper(self, _, line):
        pass

    def reducer(self, key, values):
        pass

if __name__ == '__main__':
    WordCounter.run()