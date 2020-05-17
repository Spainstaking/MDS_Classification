import os
import ast
import collections

path = os.path.join('PPI_PCCS_res', 'BRCA')

for txt in os.listdir(path):
    if txt.startswith('res_'):
        count_to_file = 'count_'+txt
        count_to_file_path = os.path.join(path, count_to_file)
        fwrite = open(count_to_file_path, 'w')
        file = open(os.path.join(path, txt), 'r')
        d = {}
        for i in file.readlines():
            temp = i.strip('\n')
            list5 = ast.literal_eval(temp)
            for x in list5:
                if x not in d:  # 这里是整数，不是字符串
                    d[x] = 1
                else:
                    d[x] = d[x] + 1
        d_order = sorted(d.items(), key=lambda x: x[1], reverse=True)  # 排序
        sorted_dict = dict(collections.OrderedDict(d_order))  # 转化为ordereddict再转化为dict
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        count7 = 0
        for key, value in sorted_dict.items():
            if value == 20:
                count1 += 1
            elif value == 19:
                count2 += 1
            elif value == 18:
                count3 += 1
            elif value == 17:
                count4 += 1
            elif value ==16:
                count5 += 1
            elif value == 15:
                count6 += 1
            elif value == 14:
                count7 += 1

            fwrite.write(str(key))
            fwrite.write(' ')
            fwrite.write(str(value))
            fwrite.write('\n')
        fwrite.close()
        break

print('count = 20: ',count1)
print('count = 19: ',count2)
print('count = 18: ',count3)
print('count = 17: ',count4)
print('count = 16: ',count5)
print('count = 15: ',count6)
print('count = 14: ',count7)
print('最大连通子图的最小控制集有1555个点，以上共{}个点'.format(count1+count2+count3+count4+count5+count6+count7))
# print(sorted_dict)