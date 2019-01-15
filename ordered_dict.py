class OrderedDict:
    def __init__(self):
        self._keys = []
        self._values = []

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def __setitem__(self, key, value):
        # if the key exists in the list, and you wanna change it to a
        # new value... update the value
        if key in self._keys:
            key_index = self._keys.index(key)  # 'a' is in spot 0, an int
            # Update the related value
            self._values.pop(key_index)  # remove from this index
            self._values.insert(key_index, value)  # add value at this index
        else:
            self._keys.append(key)
            self._values.append(value)

    def items(self):
        result = []
        for key, value in zip(self._keys, self._values):
            result.append((key, value))
        return result

    def __getitem__(self, a_key):
        for key, value in zip(self._keys, self._values):
            if key == a_key:
                return value
        raise KeyError(repr(a_key))

    def __contains__(self, a_key):
        return a_key in self._keys
#         for key in self._keys:
#             if key == a_key:
#                 return True
#         return False

    def __len__(self):
        return len(self._keys)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for key, value in zip(self._keys, self._values):
            if key not in other or other[key] != value:
                return False
        return True

    def __ne__(self, other):
        if self.__str__() != other.__str__():
            return True
        return False

    def __str__(self):
        s = '{'
        for key, value in zip(self._keys, self._values):
            s += '{}: {}, '.format(repr(key), repr(value))
        s = s.rstrip(', ')
        s += '}'
        return s

    __repr__ = __str__

    def __add__(self, other):
        new = OrderedDict()
        for key, value in self.items():
            new[key] = value

        for key, value in other.items():
            new[key] = value

        return new

    @classmethod
    def from_keys(cls, sequence):
        new = cls()
        for elem in sequence:
            new[elem] = None
        return new

    # def __setitem__(self, key, value):





# d1 = OrderedDict()
# d1['a'] = 1
# d1['b'] = 2
# print(d1)
#
# d2 = OrderedDict()
# d2['b'] = 2
# d2['a'] = 1
# print(d2)

# d1 = OrderedDict()
# d1['a'] = 1
# d1['b'] = 2
# # print(d1)
# print(d1._keys)  # is a list
# print(d1._values)  # is a list
# print(d1.items())
#
#
#
#
# d2 = OrderedDict()
# d2['c'] = 3
# d2['a'] = 4  # repeated
# # print(d2)
#
#
# d3 = d1 + d2
# # print(d3)
#
#
# assert d3 == {
#     'a': 4,  # updated
#     'b': 2,
#     'c': 3
# }
