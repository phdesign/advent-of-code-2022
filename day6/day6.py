import sys


def start_of_packet_loc(input):
    return next(
        i + 4 for i in range(len(input)) if len(set(input[i : i + 4])) == 4
    )


def start_of_message_loc(input):
    return next(
        i + 14 for i in range(len(input)) if len(set(input[i : i + 14])) == 14
    )


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        print(start_of_message_loc(f.read()))


if __name__ == "__main__":
    main()
