from mrjob.job import MRJob


class SongCount(MRJob):

    def mapper(self, _, song):
        yield song, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == "__main__":
    SongCount.run()
