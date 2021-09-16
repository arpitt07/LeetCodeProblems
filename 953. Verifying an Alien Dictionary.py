class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        a = {} # dictionary to store the key value pair of the order
        new = [] # to store the translated words with its value

        #populate the dict with order key,value
        for i,v in enumerate(order):
            a[v] = i

        #populate a new list with characters translated according to the dict
        for w in words:
            temp = []
            for x in w:
                temp.append(a[x])
            new.append(temp)

        #comparison if the words are sorted lexicographically
        for w1, w2 in zip(new, new[1:]):
            if w1 > w2:
                return False
        return True

