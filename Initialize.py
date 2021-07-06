'''
@File    : Initialize.py
@Time    : 2019/12/15 
@Author  : SureY
'''
import os
import sys
import time
import MDS_Solution

file_path = 'Data/TEST'
# genename = sys.argv[1]
genename = 'TEST'
testfile_path = os.path.join(file_path, genename)

for genefile in os.listdir(testfile_path):

    genefile_path = os.path.join(testfile_path, genefile)
    outputfile = 'PPI_PCCS_res/' + genename + '/result_' + genefile

    file = open(outputfile, 'w')

    startTime = time.process_time()

    res_list_critical, res_list_intermittent, res_list_redundant = MDS_Solution.MDS_Nodes(genefile_path)

    file.write(str(res_list_critical) + '\n')
    file.write(str(res_list_intermittent) + '\n')
    file.write(str(res_list_redundant) + '\n')
    print(res_list_critical)
    print(res_list_intermittent)
    print(res_list_redundant)
    file.close()


    endTime = time.process_time()

    print('circle over_cost time: ', endTime - startTime)


