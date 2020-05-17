import numpy as np
import random
import time
from MaxConn import addNodesEdges  #编译从 MDS目录下找到

import networkx as nx

# np.set_printoptions(suppress=True)
def select_critical(G):
    list_critical = []
    list_degreeOne = [temp_node for temp_node, temp_degree in G.degree() if temp_degree == 1]
    for u, v in G.adjacency():  # 2 {0: {}, 1: {}, 3: {}}
        if len(v) >= 2:   # 该节点有两个以上的相邻节点
            count = 0
            for uu, vv in v.items():
                if uu in list_degreeOne:  # 相邻节点的度为1的 节点
                    count += 1
            if count >= 2:  # 有两个以上 相邻节点的度为1的 节点
                list_critical.append(u)
    return list_critical


def select_redundant(G, list_critical, nodes):

    list_redundant = []
    for u, v in G.adjacency():  # u 结点的邻居们v
        count_uu = 0
        # print('----')
        # print(u,'+',v)
        for uu, vv in v.items():
            count_uu += 1
            # print(uu)  # uu 为u的邻居结点
            if uu not in list_critical:
                # print('not in')
                break
            else:
                # print('uu',uu)
                if count_uu == len(v): # 再次判断：u的邻居都是critical，即u为redundant
                    list_redundant.append(u)
        continue
    return list_redundant
# 根据数据集的得出 邻接矩阵

'''
def MatrixAdjacency_past(List_All, SumNodeNum, NetData):
    # from scipy.sparse import dok_matrix
    # prepare2_start = time.process_time()

    # MatrixAdjacency = dok_matrix((SumNodeNum, SumNodeNum), dtype=np.int32)
    MatrixAdjacency = np.zeros([SumNodeNum, SumNodeNum])  # 矩阵从0开始

    for data in NetData:
        # random.shuffle(List_All)位置被打乱了，每次可以构造不同的邻接矩阵
        ID1 = List_All.index(int(data[0]))
        ID2 = List_All.index(int(data[1]))

        MatrixAdjacency[ID1, ID2] = -1
        MatrixAdjacency[ID2, ID1] = -1

    for i in range(SumNodeNum):
        MatrixAdjacency[i, i] = -1

    # prepare2_end = time.process_time()
    # print('执行一次“矩阵存储”的时间为: ', prepare2_end - prepare2_start)

    return MatrixAdjacency
'''
def MatrixAdjacency_now(List_All, SumNodeNum, NetData, Netfile):
    prepare2_start = time.process_time()

    nodes = list(i for i in range(SumNodeNum))
    edges = []

    # with open(Netfile, "r") as file:
    #     for line in file:
    # for data in NetData:(不如for line in open())
    for line in open(Netfile, "r"):
        node1, node2 = line.strip('\n').split(' ')

        node1 = List_All.index(int(node1))
        node2 = List_All.index(int(node2))
        edges.append(tuple([node1, node2]))



    prepare2_end = time.process_time()
    # print('执行一次“矩阵存储”的时间为: ', prepare2_end - prepare2_start)
    return nodes, edges

'''
def MatrixAdjacency_now2(List_All, SumNodeNum, NetData, Netfile):

    import pandas as pd
    nodes = list(i for i in range(SumNodeNum))
    df = pd.read_csv(Netfile, header=None)
    df = df[0].str.split(' ')

    prepare2_start = time.process_time()
    aa = [list(map(eval, i)) for i in df]
    prepare2_1end = time.process_time()
    print('执行一次“1”的时间为: ', prepare2_1end - prepare2_start)

    ll = [[List_All.index(j) for j in k] for k in aa]
    prepare2_2end = time.process_time()

    print('执行一次“2”的时间为: ', prepare2_2end - prepare2_1end)


    edges = list(tuple(i) for i in ll)
    prepare2_3end = time.process_time()
    print('执行一次“3”的时间为: ', prepare2_3end - prepare2_2end)

    prepare2_end = time.process_time()
    print('执行一次“0+1+2+3+4”的时间为: ', prepare2_end - prepare2_start)
    return nodes, edges
'''
# 从Data读入数据集，并分析 数据集 的信息，返回节点list_All
def Data_Shape(Data):

    List_A = []
    List_B = []

    for row in range(Data.shape[0]):  # rows
        List_A.append(Data[row][0])
        List_B.append(Data[row][1])

    List_A = list(set(List_A))
    List_B = list(set(List_B))
    List_All = list(set(List_A) | set(List_B))
    # random.shuffle(List_All)
    # List_All.sort(reverse=False)
    '''
    length_A = len(List_A)
    length_B = len(List_B)
    # print('\t第一列节点长度：(' + str(length_A) + ')')
    # print('\t第二列节点长度：(' + str(length_B) + ')')
    '''
    length = len(List_All)
    # MaxNodeNum = int(max(max(List_A), max(List_B)))
    # print('\t最大节点值为：' + str(MaxNodeNum))
    # print('List_All:  ', List_All)
    return length, List_All


# 开始
def Init(NetFile):
    NetData = np.loadtxt(NetFile)
    SumNodeNum, List_All = Data_Shape(NetData)
    data_shape = NetData.shape[0]

    # '''方法一
    nodes, edges = MatrixAdjacency_now(List_All, SumNodeNum, NetData, NetFile)

    G = nx.Graph()
    addNodesEdges(G, False, nodes, edges)

    list_critical = []
    list_redundant = []
    list_critical = select_critical(G)
    list_redundant = select_redundant(G, list_critical, nodes)

    edges_add = []
    tuples_diagonal = tuple((tuple([i, i]) for i in nodes))
    [edges_add.append(i) for i in tuples_diagonal]
    G.add_edges_from(edges_add)



    MatrixAdjacency_Net, _ = nx.attr_sparse_matrix(G)   # A = nx.adj_matrix(G)




    '''方法二
    MatrixAdjacency_start = time.process_time()
    MatrixAdjacency_Net = MatrixAdjacency_past(List_All, SumNodeNum, NetData)
    print(MatrixAdjacency_Net)
    MatrixAdjacency_end = time.process_time()
    print('执行一次MatrixAdjacency的时间为: ', MatrixAdjacency_end - MatrixAdjacency_start)
    '''

    return MatrixAdjacency_Net, SumNodeNum, List_All, data_shape, list_critical, list_redundant
