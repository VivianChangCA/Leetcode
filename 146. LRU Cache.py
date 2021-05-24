class LRUCache:

    def __init__(self, capacity: int):
        self.size=capacity
        self.cache=OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.cache: return -1 
        val=self.cache[key]
        self.cache.pop(key)
        self.cache[key]=val
        return val 
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:  del self.cache[key]
        self.cache[key]=value
        if len(self.cache) > self.size:
            self.cache.popitem(last= False)
