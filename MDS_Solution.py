import time
from MatrixAdjacency import *
import LpSolve.Lp  # 需 import 到模块
import copy
# from pulp import *



# params 文件所在的路径，文件名，基因名
def MDS_Nodes(genefile_path):

    startTime = time.process_time()
    MatrixAdjacency_Net, SumNodeNum, List_All, data_shape, list_critical, list_redundant = MatrixAdjacency.Init(genefile_path)
    endTime = time.process_time()

    # print("初始化邻接矩阵的时间: ", endTime-startTime)
    # print('\n')

    startTime1 = time.process_time()
    # ##################LpSolve_output_start##################
    prob, var, variables = LpSolve.Lp.First(MatrixAdjacency_Net, SumNodeNum, list_critical, list_redundant)
    # print(type(variables))
    # prob_mid = LpSolve.Lp.Mid(prob.deepcopy(), var, variables, list_critical, list_redundant)
    prob_end, status, objective = LpSolve.Lp.End(prob.deepcopy())

    # prob_end = LpSolve.Lp.End(prob.deepcopy())
    # status = LpStatus[prob_end.status]
    # objective = value(prob_end.objective)

    x_list = []
    for i, v in enumerate(prob_end.variables()):

        if v.varValue == 1.0:
            index = int(v.name[10:])  # 变量是从x0开始，判断是第？个数据
            x_list.append(index)  # 第index个位置
        elif v.varValue != 0.0:
            print(v, v.varValue)
            raise ValueError("有值不为0或1")

    print('---------------------')
    print('最大连通子图节点数: ', len(List_All))
    '''
    # 查看list_critical都在MDS算出的点中
    if set(list_critical) < set(x_list):
        print('yes')
    '''

    list_intermittent = []

    # MDS计算得出x_list，查看x_list中  除list_critical外 其他是否为critical
    print('最初的critical节点个数：', len(list_critical))
    unknown_critical = list(set(x_list) ^ set(list_critical))  # ^反交集

    startTime = time.process_time()

    C_critical = []
    for ele in unknown_critical:

        temp_prob = prob.deepcopy()
        temp_prob += var[variables[ele]] == 0.0  # ignore it
        temp_prob, temp_status, temp_obj = LpSolve.Lp.End(temp_prob)
        # temp_status = LpStatus[temp_prob.status]
        # temp_obj = value(temp_prob.objective)
        if temp_obj == objective:
            # print(ele, '为intermittent')
            list_intermittent.append(ele)
        elif temp_obj > objective:
            # print('可解-->', temp_status)
            # print(ele, '为critical')
            C_critical.append(ele)
        else:  # maybe no feasible,also to be critical
            raise Exception('need edit code: critical')
    endTime = time.process_time()
    # print(unknown_critical, "计算unknown_critical的时间: ", endTime - startTime)
    # 至此x_list的节点都判断完毕

    # 查看剩下的点是否为redundant
    startTime1 = time.process_time()
    known_all = list(set(x_list) | set(list_redundant))  # 并集
    unknown_redundant = list(set(range(SumNodeNum)) ^ set(known_all))

    R_redundant = []
    for ele in unknown_redundant:
        temp_prob = prob.deepcopy()
        temp_prob += var[variables[ele]] == 1.0
        temp_prob, temp_status, temp_obj = LpSolve.Lp.End(temp_prob)
        if temp_obj == objective:
            # print(ele, 'is intermittent')
            list_intermittent.append(ele)
        elif temp_obj > objective:
            # print(ele, 'is redundant')
            prob += var[variables[ele]] == 0.0
            R_redundant.append(ele)
        else:
            raise Exception('need edit code:redundant')
    endTime1 = time.process_time()
    # print(unknown_redundant, "计算unknown_redundant的时间: ", endTime1 - startTime1)

    # print('------------------------')

    all_critical = list(set(C_critical) | set(list_critical))
    all_intermittent = list_intermittent
    all_redundant = list(set(list_redundant) | set(R_redundant))

    print('all_critical:', len(all_critical))
    print('all_intermittent:', len(all_intermittent))
    print('all_redundant:', len(all_redundant))

    # '''
    # 原节点ID
    res_list_critical = []
    res_list_intermittent = []
    res_list_redundant = []
    for i in all_critical:   # x_list存放 最小控制集点的  所在的位置----（从0开始）
        res_list_critical.append(int(List_All[i]))
    for j in all_intermittent:  # x_list存放 最小控制集点的  所在的位置----（从0开始）
        res_list_intermittent.append(int(List_All[j]))
    for k in list_redundant:   # x_list存放 最小控制集点的  所在的位置----（从0开始）
        res_list_redundant.append(int(List_All[k]))
    # '''

    # ##################LpSolve_output_end##################
    # prob_end, status, objective = LpSolve.Lp.End(prob)

    return res_list_critical, res_list_intermittent, res_list_redundant
