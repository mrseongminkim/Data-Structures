def countDiff(self):
    d = {}
    node = self.head
    while node != None:
        val = node.data
        if val in d:
            d[val] += 1
        else:
            d[val] = 1
        node = node.next
        return d
