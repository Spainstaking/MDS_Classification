import numpy as np
import random

# 根据数据集的得出 邻接矩阵
def MatrixAdjacency(List_All, SumNodeNum, NetData):
    MatrixAdjacency = np.zeros([SumNodeNum, SumNodeNum])  # 矩阵从0开始
    for col in range(NetData.shape[0]):
        i = int(NetData[col][0])
        j = int(NetData[col][1])
        # 这里需查找i,j 在list_All中对应的索引
        ID1 = SearchIndex(List_All, i)
        ID2 = SearchIndex(List_All, j)
        MatrixAdjacency[ID1, ID2] = -1
        MatrixAdjacency[ID2, ID1] = -1
    for i in range(SumNodeNum):
        MatrixAdjacency[i, i] = -1
    return MatrixAdjacency


# 从Data读入数据集，并分析 数据集 的信息，返回节点list_All(升序)，list_All中包含多余节点0
def Data_Shape(Data):
    List_A = []
    List_B = []
    List_All = []
    for row in range(Data.shape[0]):  # row
        List_A.append(Data[row][0])
        List_B.append(Data[row][1])

    List_A = list(set(List_A))
    List_B = list(set(List_B))
    List_All = list(set(List_A) | set(List_B))
    random.shuffle(List_All)
    # List_All.sort(reverse=False)

    length_A = len(List_A)
    length_B = len(List_B)
    length_All = len(List_All)
    MaxNodeNum = int(max(max(List_A), max(List_B)))
    # print('\t数据集长度：' + str(Data.shape[0]))
    # print('\t第一列节点长度：(' + str(length_A) + ')')
    # print('\t第二列节点长度：(' + str(length_B) + ')')
    # print('\t节点总个数：(' + str(length_All) + ')')
    # print('\t最大节点值为：' + str(MaxNodeNum))
    # print(List_All)
    return length_All, List_All


# 找到目标  在节点列表中的位置(节点列表的节点从小到大排列存入)
def SearchIndex(List_All, SearchID):
    flag = False
    for Index in range(len(List_All)):
        if List_All[Index] == SearchID:
            flag = True
            return Index
    if not flag:
        print("cannot find ID")


# 找到所在节点列表位置的 目标
def FindObject(List_All, Index):
    return int(List_All[Index])


# 开始
def Init(NetFile):
    NetData = np.loadtxt(NetFile)
    SumNodeNum, List_All = Data_Shape(NetData)

    MatrixAdjacency_Net = MatrixAdjacency(List_All, SumNodeNum, NetData)
    # np.savetxt("Adjacency.txt", MatrixAdjacency_Net, fmt='%d')
    return MatrixAdjacency_Net, SumNodeNum, List_All
