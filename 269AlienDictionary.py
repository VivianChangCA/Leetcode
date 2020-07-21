class Solution:
    def alienOrder(self, words: List[str]) -> str:
        alien= defaultdict(list) 
        indegree=  Counter({c : 0 for word in words for c in word}) 
        for first, second in zip(words, words[1:]): 
            for c1,c2 in zip(first,second):
                if c1==c2: 
                    continue
                indegree[c2]+=1
                alien[c1].append(c2) 
                break
            else:
                if len(first)>len(second):
                    return ""
         
        q=[i for i in indegree if indegree[i]==0] 
        res= []
        while q:
            cur=q.pop(0)
            res+=cur
            for w in alien[cur]:
                indegree[w]-=1
                if indegree[w]==0:
                    q.append(w)
        if len(res)<len(indegree):
            return ''
        else:
            return "".join(res)
