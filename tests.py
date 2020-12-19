import unittest

from myqueue import Queue, Element


class TestQueue(unittest.TestCase):

    def test_enqueue_dequeue(self):
        queue_for_tests = Queue()
        queue_for_tests.enqueue(1)
        self.assertEqual(queue_for_tests.tail.value, 1)
        self.assertEqual(queue_for_tests.dequeue(), 1)
        
    def test_empty(self):
        queue_for_tests = Queue()
        self.assertIsNone(queue_for_tests.dequeue())
        self.assertEqual(queue_for_tests.size, 0)
        
    def test_clear(self):
        queue_for_tests = Queue()
        queue_for_tests.enqueue(1)
        queue_for_tests.clear()
        self.assertIsNone(queue_for_tests.dequeue())
        self.assertEqual(queue_for_tests.size, 0)        

if __name__ == '__main__':
    unittest.main()
