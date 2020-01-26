'''
@File    : Initialize.py
@Time    : 2019/12/15 
@Author  : SureY
'''
import os
import sys
import MDS_Solution

'''
???判断当前路径是文件还是文件夹？？？
# 判断输入路径下  是文件or文件夹
def JudgeIsFile(path):
    lists = os.listdir(path)
    for pa in lists:
        filepath = os.path.join(path, pa)
        if os.path.isfile(filepath):
            return True
        elif os.path.isdir(filepath):
            return False
        else:
            raise TypeError('is not file or dir')
            break
'''

file_path = 'PPI_PCCS_edge'

'''
for genename in os.listdir(file_path):
    filepath_judge = os.path.join(file_path, genename)
    if os.path.isfile(filepath_judge):
        print(genename, 'is file.\tPASS', file=sys.stderr)
        continue
    elif os.path.isdir(filepath_judge):
        genename_path = filepath_judge
        for genefile in os.listdir(genename_path):
            genefile_path = os.path.join(genename_path, genefile)
            MDS_Solution.MDS_Nodes(genefile_path, genefile, genename)
    else:
        raise TypeError('is not file or dir')
        break
'''
genename = 'test'
genefile = 'PPI_PCC_of_Qualified(0.8)_BRCA_Stage_1_Tumor_RNASeqV2_edge.txt'
genefile_path = os.path.join(file_path, genename, genefile)

MDS_Solution.MDS_Nodes(genefile_path, genefile, genename)

