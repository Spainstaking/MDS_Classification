'''
@File    : Lp.py
@Time    : 2019/12/15 
@Author  : SureY
'''
from pulp import *
import numpy as np
import time


def First(MatrixAdjacency_Net, SumNodeNum, list_critical, list_redundant):
    # ##################LpSolve_Start##################
    prepare_start = time.process_time()

    variables = []
    values = []
    for i in range(SumNodeNum):
        variables.append('x' + str(i))
        values.append(1)
    '''
    # func diction   
    # 映射函数方式来构造字典 x0:1  但因为系数全是1，所以不使用func变量
    func = dict(zip(variables, values))
    '''
    # 创建LP problem  构造函数，用来构造一个LP问题实例，其中name指定问题名（输出信息用)，
    prob = LpProblem("MDS_problem", LpMinimize)
    # var "x1":"variable_x1"存储变量名
    var = LpVariable.dicts("variable", variables, 0, 1, LpInteger)
    # func       prob += lpSum([func[i] * var[i] for i in variables])


    # constraints
    # prepare_start = time.process_time()


    # '''方法一开始
    prob += lpSum([var[i] for i in variables])

    # prepare11_start = time.process_time()

    M_value = MatrixAdjacency_Net.toarray()  # 此处代码优化
    nonzero_variables_indexs = [np.nonzero(row)[0] for row in M_value]

    # prepare11_end = time.process_time()
    # print('执行"1. "的时间为: ', prepare11_end - prepare11_start)

    for nonzero_variables_index in nonzero_variables_indexs:
        new_variables = [variables[k] for k in nonzero_variables_index]
        temp_list = [-1 * var[j] for j in new_variables]
        prob += lpSum(temp_list) <= -1

    for i in list_critical:
        prob += var[variables[i]] == 1.0

    for i in list_redundant:
        prob += var[variables[i]] == 0.0

    # print('list_critical: ', list_critical)
    # print('len_critical: ', len(list_critical))

    # prepare12_end = time.process_time()
    # print('执行"2. prob<=-1"的时间为: ', prepare12_end - prepare11_end)
    # '''


    '''方法二开始
    for i in range(SumNodeNum):

        M_value = list(MatrixAdjacency_Net[i])  # 邻接矩阵的行   系数
        # M_value = MatrixAdjacency_Net.toarray()[i] # 此处代码优化
        # nonzero_variables_index = np.nonzero(M_value)[0]
        M = dict(zip(variables, M_value))
        temp_list = [M[j] * var[j] for j in variables]
        prob += lpSum(temp_list) <= -1
    '''

    # prepare_end = time.process_time()
    # print('"添加完约束"的时间为: ', prepare_end - prepare_start)
    return prob, var, variables
    # ##################LpSolve_End##################
def Mid(prob, var, variables, list_critical, list_redundant):



    for i in list_critical:
        prob += var[variables[i]] == 1.0
        print(type(var[variables[i]]))
    for i in list_redundant:
        prob += var[variables[i]] == 0.0

    return prob


def End(prob):

    # prob.writeLP("test.lp")

    # prob_start = time.process_time()
    prob.solve()
    # prob_end = time.process_time()
    # print('执行prob.solve的时间为: ', prob_end - prob_start)
    status = LpStatus[prob.status]

    objective = value(prob.objective)
    # print(type(prob.objective))
    # print('status : {}'.format(LpStatus[prob.status]))  # str
    # print('objective : {}'.format(value(prob.objective)))  # float
    return prob, status, objective