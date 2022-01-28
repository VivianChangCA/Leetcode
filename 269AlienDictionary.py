class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indegree = {c:0 for word in words for c in word}
        
        for w1,w2 in zip(words,words[1:]):
            for c1, c2 in zip(w1,w2):
                if c1 == c2: continue
                indegree[c2] +=1
                graph[c1].append( c2)
                break
            else: # w1= apples w2= apple , for 走完都沒有走到break,就跳到else
                if len(w1) > len(w2): return ""
        
        q = [ c for c in indegree if indegree[c] == 0 ]
        print(q,indegree)
        
        res =[]
        while q: 
            cur = q.pop()
            res.append(cur)
            for w in graph[cur]:
                indegree[w] -= 1
                if indegree[w] == 0 : q.append(w)
                    
        if len(res) < len(indegree):
            return ""
        else:
            return "".join(res)
                
                
                
        
        
