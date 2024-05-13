print("hello world")


# n number of nodes
# edges // number of connections and beteween any of the nodes.

# 0 -1 
# 1-2
# 3-4
# 3-5
# connected has one or more item in edges list
# each item has on of the 2 points of the other
# for example [0,1] , [1,2]
# [0,1] and [1,2] count is increaded by one 
# in serach for connected points
# the rest of poinst will be isolated points



# for example to validate n = 10
# 0,1,2 = one component
# 3,4 = 2nd component 
# 5,6,7,8,9,10 = 6 different componenets.
# total wil be 8 


# method to caculate connected components and make the inital count
# the rest of the n components will be added to the total count.

def calculate_connected_components(n, edges):
    
    preious_connected_nodes = []
    connected_nodes = []
    count = 0
    for item in edges:
        # check for connected nodes.
        # find connected node
        for node1, node2 in item:
            if node1 in connected_nodes or node2 in connected_nodes:
                continue
            connected_nodes.append(node1)
            connected_nodes.append(node2)

            count+1
    
    # get the rest of the nodes count, wouldn'nt be valid solution.?
    for single_item in range()
    return count

    

    # the rest of them are not connected so each 

    