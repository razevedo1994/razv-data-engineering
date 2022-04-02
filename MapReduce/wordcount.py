from mrjob.job import MRJob


class SongCount(MRJob):

    def mapper(self, _, song):
        """
        Map step: Each line in de txt file is read as a key, value pair.
        In this case, each line in the txt file only contains a value but no key.
        _ Means that in this case, there is no key for each line.
        """
        yield song, 1

    def reducer(self, key, values):
        """
        Reduce step: Combine all tuples with the same key. In this case, the key is
        the song name. Then sum all the values of the tuple, which will give the total
        song plays.
        """
        yield key, sum(values)


if __name__ == "__main__":
    SongCount.run()
