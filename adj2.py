#258/SE/2017
Lists= {}
nodes=['A','B','C','D','E']
 
Lists[0] = ['B,C,E']
Lists[1] = ['A,C']
Lists[2] = ['A,B,D,E']
Lists[3] = ['C']
Lists[4] = ['A,C']

print("\nAdjacency lists with corresponding vertex\n")
n = len(Lists)
print("Vertx      Adjacency List")
for v in range(0,n):
    print(nodes[v],'     :     ',Lists[v])
        
    
    
