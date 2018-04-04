
class ArraySequences(object):
    def __init__(self):
        pass

    def anagram_checker(self, a, b):
        a = a.replace(' ', '').lower()
        b = b.replace(' ', '').lower()

        if len(a) != len(b):
            return False

        count = {}

        for each in a:
            if each in count:
                count[each] += 1
            else:
                count[each] = 1
        for each in b:
            if each in count:
                count[each] -= 1
            else:
                count[each] = 1

        for key in count:
            if count[key] != 0:
                return False

        return True
