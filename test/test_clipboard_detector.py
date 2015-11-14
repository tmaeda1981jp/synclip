#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import unittest
from clipboard_detector import ClipboardDetector
from Queue import Queue

class TestClipboardDetector(unittest.TestCase):


    def test_memorize(self):
        q = Queue()
        q.put(1)
        q.put(2)
        q.put(3)

        detector = ClipboardDetector(q)
        detector.memorize(4)
        self.assertEqual(detector._ClipboardDetector__queue.qsize(), 4)


if __name__ == '__main__':
    unittest.main()
