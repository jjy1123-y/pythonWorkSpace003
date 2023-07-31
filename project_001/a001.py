import random

# with open('D:\pythonWorkSpace\project_001/article/a_001.txt'.strip(), encoding='utf-8', mode='w')as f:
#     f.write('文章创建成功'.strip() + '\n')
# print('文章创建成功！')
global status_dict
status_dict = {'username': 'a', 'status': True}

copyString=''

with open('D:\pythonWorkSpace\project_001/register.txt'.strip(), encoding='utf-8', mode='r')as f:
    # print(f.read())
    ccc = f.readlines()
    # print(ccc)

    for c in ccc:
        print(c)
        line_list=c.strip().split('|')
        print('====',line_list)
        if (status_dict['username'] == line_list[0]):
            print(line_list)
        else:
            copyString = copyString+c
    # for line in f:
    #     print(line)
    print("copyString=",copyString)
    # f.write(copyString + '\n')
    f.close()
    # red = random.randint(1,100)
    # r=str(red)+'|' + str(red)
    # f.write(r.strip() + '\n')
print('文章创建成功！')

with open('D:\pythonWorkSpace\project_001/register.txt'.strip(), encoding='utf-8', mode='w')as fw:

    fw.write(copyString + '\n')
    fw.close()
    # red = random.randint(1,100)
    # r=str(red)+'|' + str(red)
    # f.write(r.strip() + '\n')
print('文章创建成功！')
#
# result_dict = {}
# print(status_dict['username'])
# with open('D:\pythonWorkSpace\project_001/register.txt'.strip(), encoding='utf-8') as f:
#     for line in f:
#         line_list = line.strip().split('|')
#         result_dict[line_list[0].strip()] = line_list[1].strip()
# print(result_dict)
# if(status_dict['username']==result_dict['a']):
#     print('aaa')
#     del result_dict['a']
# print(result_dict)
# # with open('D:\pythonWorkSpace\project_001/register.txt'.strip(), encoding='utf-8',mode='w') as f1:
# #     for k in  result_dict:
# #         print('k=',k)
# #         f1.write(k)
#
# with open('D:\pythonWorkSpace\project_001/register.txt'.strip(), encoding='utf-8') as f:
#     for line in f:
#         line_list = line.strip().split('|')
#         result_dict[line_list[0].strip()] = line_list[1].strip()
# print(result_dict)