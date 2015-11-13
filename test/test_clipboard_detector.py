#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import unittest
from clipboard_detector import ClipboardDetector

class TestClipboardDetector(unittest.TestCase):


    def test_append(self):
        detector = ClipboardDetector([1,2,3])
        detector.append(4)
        self.assertEqual(len(detector._ClipboardDetector__memos), 4)


    def test_append_shift_values_when_memos_length_are_over_10(self):
        detector = ClipboardDetector(list(xrange(1, 11))) # [1..10]
        detector.append(11) # [2..11]
        self.assertEqual(len(detector._ClipboardDetector__memos), 10)
        self.assertEqual(detector._ClipboardDetector__memos[0],  2)
        self.assertEqual(detector._ClipboardDetector__memos[-1], 11)


if __name__ == '__main__':
    unittest.main()
