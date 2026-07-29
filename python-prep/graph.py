# class TechGraph:
#     def __init__(self,is_directed=False):
#         self.adj_list={}
#         self.is_directed=is_directed

#     def add_vertex(self,vertex):
#         if vertex not in self.adj_list:
#             self.adj_list[vertex]=[]

#     def add_edge(self,u,v):
#         self.add_vertex(u)
#         self.add_vertex(v)

#         self.adj_list[u].append(v)

#         if not self.is_directed:
#             self.adj_list[v].append(u)

#     def display(self):
#         for vertex,neighbors in self.adj_list.items():
#             print(vertex,"->",neighbors)

# def run_graph_demo():
#     print("="*60)
#     print("demo 1 undirected (peer to peer)")
#     print("="*60)

#     mesh_network=TechGraph(is_directed=False)


#     mesh_network.add_edge("EdgeRouter_A","CoreSwitch")
#     mesh_network.add_edge("EdgeRouter_A","LoadBalancer")
#     mesh_network.add_edge("CoreSwitch_A","DatabaseMaster")
#     mesh_network.add_edge("LoadBalancer_1","Appserver_1")
#     mesh_network.add_edge("LoadBalancer_1","Appserver_2")
#     mesh_network.add_edge("Appserver_1","DatabaseMaster")
#     mesh_network.add_edge("Appserver_2","DatabaseMaster")

#     mesh_network.add_vertex("BackupStorage")

#     mesh_network.display()


#     print("="*60)
#     print("demo 2 directed (Micro service)")
#     print("="*60)

#     data_pipeline=TechGraph(is_directed=True)


#     data_pipeline.add_edge("Data Ingestion","API gateway")
#     data_pipeline.add_edge("API gateway","Auth Service")
#     data_pipeline.add_edge("API gateway","Order Processor")
#     data_pipeline.add_edge("API gateway","Inventory Service")

#     data_pipeline.add_edge("Order Processor","Kafka_Broker")
#     data_pipeline.add_edge("Kafka_Broker","Inventory_worker")
#     data_pipeline.add_edge("Kafka_Broker","Analytics Engine")
#     data_pipeline.add_edge("Inventory_worker","Relational_DB")
#     data_pipeline.add_edge("Analytics Engine","Data_baselakehouse")

#     data_pipeline.display()

# if __name__=="__main__":
#     run_graph_demo()

class systemetwork:
    def __init__(self,is_directed=False):
        self.adj_list={}
        self.is_directed=is_directed

    def add_node(self,node):
        if node not in self.adj_list:
            self.adj_list[node]=[]

    def add_edge(u,v):
        self.add_node(u)
        self.add_node(v)

        self.adj_list[u].append(v)

        if not self.is_directed:
            self.adj_list[v].append(u)