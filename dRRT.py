from PRM import generateRoadMap
from Node import Node
import numpy as np
from math import sqrt
from copy import deepcopy
from time import time

def drrt(visuals=False, mapString="map.txt", start=[[51, 71], [50, 33]], end=[[46, 30],[47, 64]]):

    #fixed_nodes = [[60, 38], [51, 47], [50, 33], [51, 71], [69, 72], [36, 38], [19, 61], [5, 93], [5, 93], [26, 95],
    #               [82, 96], [55, 97], [49, 16], [83, 37], [4, 5], [6, 22], [10, 37], [26, 34], [24, 10], [47, 5], [27, 3],
    #               [46, 30], [68, 3], [70, 20], [70, 32], [92, 6], [93, 27], [7, 61], [5, 79], [24, 73], [47, 64], [36, 60],
    #                [71, 59], [89, 59], [91, 78], [70, 87], [47, 89], [64, 5], [52, 60], [48, 61], [51, 38], [48, 36]]

    # start1 = [51, 71]
    # start2 = [50, 33]
    # end1 = [46, 30]
    # end2 = [47, 64]
    # start1 = [24, 10]
    # start2 = [70, 87]
    # end1 = [70, 20]
        # end2 = [24, 73]

    # fixed_nodes = [[25, 25], [25, 50], [25, 75],
    #                [50, 25], [50, 50], [50, 75],
        #                [75, 25], [75, 50], [75, 75]]
    

        #vertices, edges = generateRoadMap(0, 25, fixed_nodes)
    

    fixed_nodes = []
    for s in start:
        fixed_nodes.append(s)
    for e in end:
        fixed_nodes.append(e)

    vertices, edges = generateRoadMap(30, 40, fixed_nodes)
    from mapUtils import readMap
    map = readMap(mapString)

    from visualize import visualizeRoadMap, visualizeMap
    if visuals:
        visualizeMap(map, start, end, vertices)
        visualizeRoadMap(map, vertices, edges)
    

    GHat = []
    for i in vertices:
        for j in vertices:
                GHat.append([i, j])

    E_Hat = []
    for i in range(len(GHat)):
        for j in range(len(GHat)):
            if GHat[i] == GHat[j]:
                pass
            elif GHat[i][0] == GHat[j][0]:
                index1 = vertices.index(GHat[i][1])
                index2 = vertices.index(GHat[j][1])
                if [index1, index2] in edges or [index2, index1] in edges:
                    E_Hat.append([i, j])
            elif GHat[i][1] == GHat[j][1]:
                index1 = vertices.index(GHat[i][0])
                index2 = vertices.index(GHat[j][0])
                if [index1, index2] in edges or [index2, index1] in edges:
                    E_Hat.append([i, j])
            else:
                index1 = vertices.index(GHat[i][0])
                index2 = vertices.index(GHat[j][0])
                index3 = vertices.index(GHat[i][1])
                index4 = vertices.index(GHat[j][1])
                if ([index1, index2] in edges or [index2, index1] in edges) and (
                        [index3, index4] in edges or [index4, index3] in edges):
                        E_Hat.append([i, j])

    def getNearestNode(node, graph):
        nearesNode = [[], 99999]
        for i in graph:
            distance = sqrt((node[0][0] - i[0][0]) ** 2 + (node[0][1] - i[0][1]) ** 2 + (node[1][0] - i[1][0]) ** 2 + (
                        node[1][1] - i[1][1]) ** 2)
            if distance < nearesNode[1]:
                nearesNode[0] = deepcopy(i)
                nearesNode[1] = deepcopy(distance)
            return nearesNode[0]
    
    

    nodes = []
    result = []
    nodes.append(Node(start))
    prev = time()
    for i in range(5000):
        print(i)
        point = [[np.random.randint(0, 100), np.random.randint(0, 100)], [np.random.randint(0, 100), np.random.randint(0, 100)]]
        # point = end
        # point = GHat[np.random.randint(0, len(GHat))]
        # Update distances for pre existing nodes from new point
        for i in range(len(nodes)):
            nodes[i].updateDistance(point)
        # Sort existing node list by distance from new point
        nodes.sort(key=lambda x: x.distance)
        nearestNode = nodes[0]
        neighboursIndexList = []
        index = GHat.index(nearestNode.env)
        for i in E_Hat:
            if index in i:
                for tempVertex in i:
                    if tempVertex != index:
                            neighboursIndexList.append(tempVertex)

        neighboursList = []
        for index in neighboursIndexList:
            neighboursList.append(Node(GHat[index]))
        for i in range(len(neighboursList)):
            neighboursList[i].updateDistance(point)
        neighboursList.sort(key=lambda x: x.distance)
        for neighbour in neighboursList:
            if neighbour.env[0] != neighbour.env[1]:
                nodes.append(Node(neighbour.env, nearestNode))
                break
        if neighboursList[0].env == end:
            # for i in range(len(nodes)):
            #     nodes[i].updateDistance(end)
            result = list(Node(neighboursList[0].env, nearestNode).path())
            break
    # for i in result:
        #    print(i.env)
    time_needed = -1
    if len(result) > 0:
        time_needed = time()-prev
    if visuals:
        from visualize import visualizePath
        result = [i.env for i in result]
        visualizePath(map, start, end, result)

    return time_needed, len(result)
