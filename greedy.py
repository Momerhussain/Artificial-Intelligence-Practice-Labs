import queue as q
class greedysearch:
    def search(self,d,start,goal):
        que=q.PriorityQueue()
        que.put((start.h,start))
        path=list()
        while(not que.empty()):
            node=que.get()
            node=node[1]
            path.append(node)
            que=q.PriorityQueue()
            if node.name==goal.name:
                return path
            else:
                for child in d[node]:
                    if child not in path:
                        que.put((child.h,child))
        return ["error"]
class node:
    def __init__(self,name,h):
        self.name=name
        self.h=h
s=node('s',7)
a=node('a',6)
b=node('b',5)
c=node('c',4)
d=node('d',2)
g=node('g',0)

d={s:[a,b],a:[s,g],b:[s,c],c:[b,d],d:[g,c],g:[a,d]}
obj=greedysearch()
print([x.name for x in obj.search(d,s,g)])
