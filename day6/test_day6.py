import unittest
from day6 import start_of_packet_loc, start_of_message_loc


class TestSuite(unittest.TestCase):
    def test_start_of_packet_loc(self):
        tests = [
            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
            ("nppdvjthqldpwncqszvftbrmjlhg", 6),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
        ]
        for t in tests:
            self.assertEqual(start_of_packet_loc(t[0]), t[1])

    def test_start_of_message_loc(self):
        tests = [
            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
            ("nppdvjthqldpwncqszvftbrmjlhg", 23),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
        ]
        for t in tests:
            self.assertEqual(start_of_message_loc(t[0]), t[1])


if __name__ == "__main__":
    unittest.main()
