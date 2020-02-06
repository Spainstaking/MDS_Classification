import time
from MatrixAdjacency import *
import LpSolve.Lp  # 需 import 到模块





# params 文件所在的路径，文件名，基因名
def MDS_Nodes(genefile_path):
    MatrixAdjacency_Net, SumNodeNum, List_Node = MatrixAdjacency.Init(genefile_path)



    startTime = time.process_time()

    # ##################LpSolve_output_start##################
    prob = LpSolve.Lp.Solve(MatrixAdjacency_Net, SumNodeNum)
    x_list = []
    for i, v in enumerate(prob.variables()):
        # print(v, v.varValue)
        if v.varValue == 1.0:
            index = int(v.name[10:]) - 1  # 变量是从x1开始，判断是第？个数据
            x_list.append(index)  # 第index个位置
        elif v.varValue != 0.0:
            print('\tvalue：\t', int(v.name[10:]))
            raise ValueError("有值不为0或1")
    # print(x_list)
    # x_list.sort(reverse=False)
    # print('x_list : ', x_list)

    # 原节点ID
    res_list = []
    for i in x_list:   # x_list存放 最小控制集点的  所在的位置----（从0开始）
        res_node = MatrixAdjacency.FindObject(List_Node, i)
        res_list.append(res_node)
    # print('res_list', res_list)

    # ##################LpSolve_output_end##################
    endTime = time.process_time()

    return res_list
