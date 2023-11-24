
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())

#input format
"""The input is read by the provided locked code template. In the first line, there is a single integer  denoting the number of queries. Each of the following  lines contains a stream_name followed by integer , and it corresponds to a single test for your function."""
queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    #out put format
    """The output is produced by the provided and locked code template. For each of the queries (stream_name, n), if the stream_name is even then print_from_stream(n) is called. Otherwise, if the stream_name is odd, then print_from_stream(n, OddStream()) is called."""
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())