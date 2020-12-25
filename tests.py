import unittest

from myqueue import Queue, Element


class TestQueue(unittest.TestCase):

    def test_enqueue_dequeue(self):
        queue_for_tests = Queue()
        first_value = 1
        second_value = 2
        third_value = 3
        queue_for_tests.enqueue(first_value)
        queue_for_tests.enqueue(second_value)
        queue_for_tests.enqueue(third_value)
        self.assertEqual(queue_for_tests.tail_of_queue(), third_value)
        self.assertEqual(queue_for_tests.head_of_queue(), queue_for_tests.dequeue())
        
    def test_empty(self):
        queue_for_tests = Queue()
        self.assertIsNone(queue_for_tests.dequeue())
        self.assertEqual(queue_for_tests.size, 0)
        self.assertTrue(queue_for_tests.is_empty())
        
    def test_clear(self):
        queue_for_tests = Queue()
        queue_for_tests.enqueue(1)
        queue_for_tests.clear()
        self.assertIsNone(queue_for_tests.dequeue())
        self.assertEqual(queue_for_tests.size_of_queue(), 0)

if __name__ == '__main__':
    unittest.main()
