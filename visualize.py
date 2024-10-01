import matplotlib.pyplot as plt

def visualizeMap(map, start, end, fixed_nodes):
    plt.imshow(map, cmap="gray")
    for start_point in start:
        plt.scatter(start_point[0], start_point[1], color="red", s=40)
    for end_point in end:
        plt.scatter(end_point[0], end_point[1], color="green", s=40)

    for fixed_node in fixed_nodes:
        plt.scatter(fixed_node[0], fixed_node[1], color="yellow", s=1)

    plt.show()

def visualizePath(map, start, end, foundPath):
    plt.imshow(map, cmap="gray")
    for start_point in start:
        plt.scatter(start_point[0], start_point[1], color="red")
    for end_point in end:
        plt.scatter(end_point[0], end_point[1], color="green")

    colors = ["blue", "purple"]

    for i in range(len(foundPath)-1):
        for j in range(len(foundPath[i])):
            plt.plot([foundPath[i][j][0], foundPath[i+1][j][0]], [foundPath[i][j][1], foundPath[i+1][j][1]], color=colors[j % len(colors)])

    plt.show()


def visualizeRoadMap(map, vertices, edges):
    plt.imshow(map, cmap="gray")
    for edge in edges:
        plt.plot([vertices[edge[0]][0], vertices[edge[1]][0]], [vertices[edge[0]][1], vertices[edge[1]][1]], color="blue")
    plt.show()

