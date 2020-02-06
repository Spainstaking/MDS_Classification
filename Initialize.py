'''
@File    : Initialize.py
@Time    : 2019/12/15 
@Author  : SureY
'''
import os
import sys
import time
import MDS_Solution

'''
? ? ?判断当前路径是文件还是文件夹？？？
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



'''
for genename in os.listdir(file_path):
    filepath_judge = os.path.join(file_path, genename)
    if os.path.isfile(filepath_judge):
        print(genename, 'is file.\tPASS', file=sys.stderr)
        continue
    elif os.path.isdir(filepath_judge):
        for genefile in os.listdir(filepath_judge):
            genefile_path = os.path.join(filepath_judge, genefile)
            MDS_Solution.MDS_Nodes(genefile_path, genefile, genename)
    else:
        raise TypeError('is not file or dir')
        break
'''



# 产生的新list 是否与 已存在的list 重复（此代码存在问题）
def IsCoincide(list_old, list_new):
    list_old.sort()
    list_new.sort()
    if list_old == list_new:
        return True
    else:
        return False


file_path = 'PPI_PCCS_edge_maxconn'
# for genename in os.listdir(file_path):
#     filepath_judge = os.path.join(file_path, genename)
#     if os.path.isdir(filepath_judge):
#         for genefile in os.listdir(filepath_judge):
#             genefile_path = os.path.join(filepath_judge, genefile)
#             outputfile = 'PPI_PCCS_res/' + genename + '/res_' + genefile
genename = 'BRCA'
testfile_path = os.path.join(file_path, genename)
for genefile in os.listdir(testfile_path):
    startTime = time.process_time()
    genefile_path = os.path.join(testfile_path, genefile)
    outputfile = 'PPI_PCCS_res/' + genename + '/res_' + genefile

    file = open(outputfile, 'w')
    list_all = []
    time_count = 15
    for k in range(time_count):
        # 执行N次
        res_list = MDS_Solution.MDS_Nodes(genefile_path)
        judgeExist = False
        for temp in list_all:
            if IsCoincide(temp, res_list):
                judgeExist = True
                break
            else:
                continue
        if not judgeExist:
            res_list.sort()
            print('res_list : {0}'.format(res_list))
            file.write(str(res_list)+'\n')
            list_all.append(res_list)
    file.close()
    print('MDS_num : {}'.format(len(list_all)))
    endTime = time.process_time()
    print('cost time: ',endTime-startTime)
    print('---------------------------')
