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

# class systemetwork:
#     def __init__(self,is_directed=False):
#         self.adj_list={}
#         self.is_directed=is_directed


#     def add_node(self,node):
#         if node not in self.adj_list:
#             self.adj_list[node]=[]

#     def add_edge(u,v):
#         self.add_node(u)
#         self.add_node(v)

#         self.adj_list[u].append(v)

#         if not self.is_directed:
#             self.adj_list[v].append(u)

# def influence_metric(network, user_profile):
#     if user_profile not in network:
#         return{"following":0,"followers":0}

#     out_degree=len(network.adj_list[user_profile])
#     in_degree=0

#     for user,follow_list in network.adj_list.items():
#         if user_profile in follow_list:
#             in_degree+=1

#     return{"following":out_degree,"followers":in_degree}

# def locate_file(network,current_folder,target_file,visited=None):
#     if visited is None:
#         visited=set()

#     if current_folder == target_file:
#         return True

#     visited.add(current_folder)

#     for neighbor in network.adj_list.get(current_folder, []):
#         if neighbor not in visited:
#             if locate_file(network, neighbor, target_file, visited):
#                 return True

#     return False
            
'''Track 'visiting' nodes in the current path vs 'fully_processed'nodes'''

# def cycle_detection(network):
#     visiting = set()
#     fully_processed = set()

#     for node in network.adj_list:
#         if node not in fully_processed:
#             if _has_cycle(network, node, visiting, fully_processed):
#                 return True

#     return False

# def _has_cycle(network, node, visiting, fully_processed):
#     if node in visiting:
#         return True
#     if node in fully_processed:
#         return False

#     visiting.add(node)

#     for neighbor in network.adj_list.get(node, []):
#         if _has_cycle(network, neighbor, visiting, fully_processed):
#             return True

#     visiting.remove(node)
#     fully_processed.add(node)
#     return False

'''You are designing a CI/CD build engine like Github Actions. Code tests depends on compilation, compilation depends on linting,
and deployment depends on passing tests.
You need to calculate the exact order to run these jobs.'''
from collections import deque

def topological_sort(jobs, dependencies):
    graph = {job: [] for job in jobs}
    indegree = {job: 0 for job in jobs}

    
    for u, v in dependencies:
        graph[u].append(v)
        indegree[v] += 1

    q = deque([job for job in jobs if indegree[job] == 0])

    order = []

    while q:
        curr = q.popleft()
        order.append(curr)

        for neighbor in graph[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

   
    if len(order) != len(jobs):
        return "Cycle detected! No valid execution order."

    return order


