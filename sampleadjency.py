class Vertex:
    def vertices(self,vertex,vertex1,vertex2,vertex3):
        self.name = [vertex,vertex1,vertex2,vertex3]
        self.s=sorted(self.name)
        self.mm=vertex
        self.md=vertex1
        self.me=vertex2
        self.mf=vertex3
        return self.s,"these that we enter and sort them in order"
    def add_edges(self,edge,edge1,edge2):
        self.edges=[edge]
        self.edges1=[edge1]
        self.edges2=[edge2]
        self.k=self.edges,self.edges1,self.edges2
        self.dek=[edge,edge1,edge2]
        return self.k,"these are edges that we give"
    def add_edges1(self,edge,edge1,edge2):
        self.edges=[edge]
        self.edges1=[edge1]
        self.edges2=[edge2]
        self.deks=[edge,edge1,edge2]
        self.kk=self.edges,self.edges1,self.edges2
        return self.kk,"these are edges that we give"
    def add_edges2(self,edge,edge1,edge2):
        self.edges=[edge]
        self.edges1=[edge1]
        self.edges2=[edge2]
        self.dekd=[edge,edge1,edge2]
        self.kkk=self.edges,self.edges1,self.edges2
        return self.edges,self.edges1,self.edges2,"these are edges that we give"
    def gen_vert_edges(self):
        self.de={self.mm:self.dek,self.md:self.deks,self.me:self.dekd}
        return self.de,"first edges we generate"
a=Vertex()
b=a.vertices("A","B","C","D")
c=a.add_edges("C","D","E")
d=a.add_edges1("C","D","A")
k=a.add_edges2("C","D","E")
s=a.gen_vert_edges()
print(s)
