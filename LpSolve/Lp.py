'''
@File    : Lp.py
@Time    : 2019/12/15 
@Author  : SureY
'''
from pulp import *

def Solve(MatrixAdjacency_Net, SumNodeNum):
    # ##################LpSolve_Start##################
    variables = []
    values = []
    for i in range(1, SumNodeNum + 1):
        variables.append('x' + str(i))
        values.append(1)
    # func diction
    func = dict(zip(variables, values))
    # 创建LP problem  构造函数，用来构造一个LP问题实例，其中name指定问题名（输出信息用)，
    prob = LpProblem("MDS_problem", LpMinimize)
    # var
    var = LpVariable.dicts("variable", variables, 0, 1, LpBinary)
    # func
    prob += lpSum([func[i] * var[i] for i in variables])
    # constraints
    for i in range(SumNodeNum):
        M_value = list(MatrixAdjacency_Net[i])  # 邻接矩阵
        print(MatrixAdjacency_Net[i])
        M = dict(zip(variables, M_value))
        prob += lpSum([M[j] * var[j] for j in variables]) <= -1
    # prob.writeLP("problem1.lp")
    prob.solve()

    print('status : {}'.format(LpStatus[prob.status]))
    print('objective : {}'.format(value(prob.objective)))
    return prob
    # ##################LpSolve_End##################