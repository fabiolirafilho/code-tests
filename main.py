from lib.utils import trim_str_stream
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Stream handler simple prog"
    )
    parser.add_argument("stream", type=str)
    args = parser.parse_args()
    stream = args.stream
    sys.stdout.write(trim_str_stream(stream))