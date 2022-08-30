class graph:
    def _init_(self,gdict=None):
        if gdict == None:
            gdict = {}
        self.gdict = gdict

    #to print vertices
    def displayvertex(self):
        return list(self.gdict.keys())

    #to print edges
    def displayedges(self):
        edgelist = []
        for vertex1 in self.gdict.keys():
            for vertex2 in self.gdict[vertex1]:
                if [vertex1,vertex2] not in edgelist:
                    edgelist.append([vertex1,vertex2])
                else:
                    continue
        return edgelist

    #to add vertex
    def addvertex(self, newvertex):
        self.newvertex = newvertex
        if self.newvertex not in self.gdict.keys():
            self.gdict[self.newvertex] = []

    #to add edge
    def addedge(self, newedge):
        self.newedge = newedge
        vertex1,vertex2 = self.newedge
        if vertex1 in self.gdict:
            self.gdict[vertex1].append(vertex2)
        else:
            self.gdict[vertex1] = [vertex2]



graph_elements = { "a" : ["b","c"],"b" : ["a", "d"],"c" : ["a", "d"],"d" : ["b","c","e"],"e" : ["d"] }
obj = graph(graph_elements)
print(obj.displayvertex())
print(obj.displayedges())
obj.addvertex("f")
obj.addedge(["e","f"])
print(obj.displayvertex())
print(obj.displayedges())