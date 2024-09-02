class Solution(object):
    def reconstructQueue(self, people):
        """
        :type points: List[List[int]]
        :rtype: List[List[int]]
        """

        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for elem in people:
            queue.insert(elem[1], elem)
        return queue
