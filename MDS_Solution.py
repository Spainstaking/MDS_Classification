import time
from MatrixAdjacency import *
import LpSolve.Lp  # 需 import 到模块

'''
# 产生的新list 是否与 已存在的list 重复
def IsCoincide(list_all, list_new):
    flag = False
    for old in list_all:
        if old == list_new:
            flag = True
            break
    return flag
'''


# params 文件所在的路径，文件名，基因名
def MDS_Nodes(genefile_path, genefile, output_genename):
    # print('genefile_path:', genefile_path)
    MatrixAdjacency_Net, SumNodeNum, List_Node = MatrixAdjacency.Init(genefile_path)

    startTime = time.process_time()
    outputfile = './PPI_PCCS_edge/' + output_genename + '/res_' + genefile
    file = open(outputfile, 'w')

    # '''
    list_all = []
    time_count = 10
    for k in range(time_count):
    # '''
        prob = LpSolve.Lp.Solve(MatrixAdjacency_Net, SumNodeNum)
        # ##################LpSolve_output_start##################

        x_list = []
        for i, v in enumerate(prob.variables()):
            print(v,v.varValue)
            if v.varValue == 1.0:
                Index = int(v.name[10:])  # 通过 X？ 判断是第？个数据
                x_list.append(Index)  # 第几个节点
            elif v.varValue != 0.0:
                print('\tvalue：\t', int(v.name[10:]))
                raise ValueError("有值不为0或1")
        x_list.sort(reverse=False)
        # print('x_list : ', x_list)
        '''
        if not IsCoincide(list_all, x_list):
            list_all.append(x_list)
            file.write(str(x_list) + '\n')
        '''
        # 原节点ID
        res_list = []
        for i in x_list:
            res_node = MatrixAdjacency.FindObject(List_Node, i)
            res_list.append(res_node)
        print('res_list : ', res_list)
        print('-----------------------------------------------------------')
    '''
    print('MDS_num : {}'.format(len(list_all)))
    '''
    file.write(str(res_list) + '\n')
    file.close()
    # ##################LpSolve_output_end##################
    endTime = time.process_time()
    print(genefile.split('.')[0], '- Cost time : ', endTime - startTime)
