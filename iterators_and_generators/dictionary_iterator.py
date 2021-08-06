class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj
        self.dict_keys = list(self.dict_obj.keys())
        self.start = 0
        self.end = len(self.dict_obj)

    def __iter__(self):
        return self

    def __next__(self):
        if self.end == self.start:
            raise StopIteration
        i = self.start
        current_result = (self.dict_keys[i], self.dict_obj[self.dict_keys[i]], )
        self.start += 1
        return current_result

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
