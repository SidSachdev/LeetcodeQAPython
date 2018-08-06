class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key2value = {}
        self.key2index = {}
        self.index2key = {}
        self.index_counter = 0
        self.delete_counter = 0
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key2value:
            old_index = self.key2index[key]
            del self.index2key[old_index]
            self.index_counter += 1
            self.key2index[key] = self.index_counter
            self.index2key[self.index_counter] = key
        return self.key2value.get(key, -1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.key2value:
            old_index = self.key2index[key]
            del self.index2key[old_index]
        else:
            if len(self.key2value) >= self.cap:
                while self.delete_counter not in self.index2key:
                    self.delete_counter += 1
                LRUkey = self.index2key[self.delete_counter]
                del self.key2value[LRUkey]
                del self.index2key[self.delete_counter]
                del self.key2index[LRUkey]
        self.key2value[key] = value
        self.index_counter += 1
        self.index2key[self.index_counter] = key
        self.key2index[key] = self.index_counter

