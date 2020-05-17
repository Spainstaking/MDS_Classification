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
# --------------------------------------------------------------------------------------------------

# 产生的新list 是否与 已存在的list 重复（此代码存在问题）
def IsCoincide(list_old, list_new):
    list_old.sort()
    list_new.sort()
    if list_old == list_new:
        return True
    else:
        return False
# --------------------------------------------------------------------------------------------------

# for genename in os.listdir(file_path):
#     filepath_judge = os.path.join(file_path, genename)
#     if os.path.isdir(filepath_judge):
#         for genefile in os.listdir(filepath_judge):
#             genefile_path = os.path.join(filepath_judge, genefile)
#             outputfile = 'PPI_PCCS_res/' + genename + '/res_' + genefile
# genename = 'HNSC'
#-------------------------------------------------------------------------------------------------------

'''
    list_all = []
    time_count = 1
    count = 0
    startTime = time.process_time()
    for k in range(time_count):
        # 执行N次
        res_list, SumNodeNum, data_shape = MDS_Solution.MDS_Nodes(genefile_path)

        judgeExist = False
        for temp in list_all:
            if IsCoincide(temp, res_list):
                judgeExist = True
                break
        if not judgeExist:
            res_list.sort()
            print('len : {0} ,res_list : {1}'.format(len(res_list), res_list))
            file.write(str(res_list) + '\n')
            list_all.append(res_list)
        count += 1
        if count == time_count:
            print("结点的个数： {}".format(SumNodeNum))
            print("数据的行数： {}".format(data_shape))
        else:
            pass
    file.close()
    endTime = time.process_time()
    # print('MDS_num : {}'.format(len(list_all)))
    '''