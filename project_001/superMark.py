import os
import sys

# 将本地保存用户名和密码的文件转为字典
def get_user_dict(filename):
    result_dict = {}
    with open(filename, encoding='gbk') as f:
        for line in f:
            line_list = line.strip().split('|')
            result_dict[line_list[0].strip()] = line_list[1].strip()
    return result_dict

# 【登陆】无返回值，登陆成功后修改全局变量status_dict，输错三次后直接在函数中退出整个程序。
def login():
    user_dict = get_user_dict('register.txt')
    time_left = 3
    while time_left >= 1:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        if username in user_dict and password == user_dict[username]:
            print('登录成功！')
            global status_dict
            status_dict = {'username': username, 'status': True}
            return
        else:
            time_left = time_left - 1
            if time_left != 0:
                print('账号或者密码错误，您还剩{time_left}次机会')
    else:
        print('您已输错三次，无法继续登陆，程序退出！')
        sys.exit()

# 【注册】无返回值
def register():
    user_dict = get_user_dict('register.txt')
    while 1:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        if username.isalnum():
            if 6 <= len(password) <= 14:
                if username not in user_dict:
                    print('注册成功！')
                    with open('register.txt', encoding='gbk', mode='a')as f:
                        f.write(username + '|' + password + '\n')
                        return
                else:
                    print('注册失败，用户名已存在，请重新输入！')
            else:
                print('注册失败，密码长度应在6-14位之间，请重新输入！')
        else:
            print('注册失败，用户名只能是数字或字母，请重新输入！')

# 装饰器
def auth(f):
    def inner(*args, **kwargs):
        if status_dict['status']==False:
            print('您尚未登陆，无法进入相关页面！')
            login()     #登陆不成功系统将直接退出，因此只要能从这个函数出来，就一定是登陆成功
        r = f(*args, **kwargs)
        return r
    return inner

@auth
def article():
    while 1:
        article_choice=input('1.直接写入内容\n2.导入md文件\n欢迎%s进入文章页面，请选择：'%(status_dict['username'])).strip()
        if article_choice=='1':
            while 1:
                article_input=input('请按照"文件名|文件内容"格式书写，文件名应含扩展名".txt"：').strip()
                if article_input.count('|')!=1:
                    print('文章创建失败！请确保您输入的内容中有且只有一个分隔符"|"')
                else:
                    article_filename, article_content = article_input.split('|')
                    if article_filename.endswith('.txt')==False:
                        print('文章创建失败！请确保您输入的文件名以".txt"结尾')
                    else:
                        break
            print(os.path.dirname(__file__)+'/article/'+article_filename.strip())
            with open(os.path.dirname(__file__)+'/article/'+article_filename.strip(),encoding='utf-8',mode='a')as f:
                # content = f.read()
                # print(content)
                # content + '\n' +
                f.write(article_content.strip()+'\n')
            print('文章创建成功！')
            break
        elif article_choice=='2':
            while 1:
                article_input = input('请输入待导入文件的文件名，文件名应含扩展名".md"：').strip()
                if article_input.endswith('.md'):
                    break
                else:
                    print('文章创建失败！请确保您输入的文件名以".md"结尾')
            with open(article_input,encoding='utf-8')as f1, open(os.path.dirname(__file__)+'/article/'+article_input[:-3]+'.txt', encoding='gbk',mode='w')as f2:
                for line in f1:
                    f2.write(line)
            print('文章创建成功！')
            break
        else:
            print('您的输入有误，请重新输入！')

@auth
def comment():
    print('欢迎%s进入评论页面'%(status_dict['username']))
    article_list = os.listdir(os.path.dirname(__file__)+'/article')
    while 1:
        for article_num, article_filename in enumerate(article_list):
            print(article_num + 1, article_filename)
        comment_choice=input('请输入您要评论的文章序号：').strip()
        if comment_choice.isdecimal() and 1<=int(comment_choice)<=len(article_list):
            comment_choice=int(comment_choice)
            break
        else:
            print('您的输入有误，请检查输入的内容是否为纯数字，且范围在1到{len(article_list)}之间')
    comment_area_title ='''\n评论区：\n-----------------------------------------\n'''
    temp_mark=False
    comment_area_title_mark=False
    print(os.path.dirname(__file__) + '/article/' + article_list[comment_choice - 1])
    with open(os.path.dirname(__file__) + '/article/' + article_list[comment_choice - 1], encoding='utf-8', mode='r+')as f:
        for line in f:
            print(line,end="")
            if line=='评论区：\n':
                temp_mark = True
            elif temp_mark == True and line=='-----------------------------------------\n':
                comment_area_title_mark=True
                temp_mark=False
            elif temp_mark == True and line!='-----------------------------------------\n':
                temp_mark=False
        comment_input = input('请输入您的评论：').strip()
        sensitive_words_list=["苍老师", "东京热", "武藤兰", "波多野结衣"]
        comment_with_no_sensitive_words=remove_sensitive_words(comment_input,sensitive_words_list)
        if comment_area_title_mark==False:
            f.write(comment_area_title)
        f.write(status_dict['username']+':\n')
        f.write(comment_with_no_sensitive_words+'\n')
        print('评论成功！')

@auth
def diary():
    print('欢迎%s进入日记页面'%(status_dict['username']))

@auth
def favorite():
    print('欢迎%s进入收藏页面'%(status_dict['username']))

@auth
def logout():
    global status_dict
    status_dict = {'username': None, 'status': False}
    with open('register.txt'.strip(), encoding='utf-8', mode='r')as f:
        ccc = f.readlines()
        for c in ccc:
            line_list = c.strip().split('|')
            if (status_dict['username'] == line_list[0]):
                print(line_list)
            else:
                copyString = copyString + c
        f.close()
    print('注册信息读取成功！')

    with open('register.txt'.strip(), encoding='utf-8', mode='w')as fw:
        fw.write(copyString + '\n')
        fw.close()
    print('注册信息注销成功！')
    print('注销成功！')

#敏感词过滤
def remove_sensitive_words(user_comment,sensitive_words_list=[]):
    for sensitive_word in sensitive_words_list:
        if sensitive_word in user_comment:
            user_comment=user_comment.replace(sensitive_word,'*'*len(sensitive_word))
    return user_comment

# 主程序
status_dict = {'username': None, 'status': False}
while 1:
    if status_dict['username']==None:
        homepage_choice = input('1.登录\n2.注册\n3.进入文章页面\n4.进入评论页面\n5.进入日记页面\n6.进入收藏页面\n7.注销账号\n8.退出整个程序\n您好，欢迎访问博客园！请选择：').strip()
    else:
        homepage_choice = input('1.登录\n2.注册\n3.进入文章页面\n4.进入评论页面\n5.进入日记页面\n6.进入收藏页面\n7.注销账号\n8.退出整个程序\n%s您好，欢迎访问博客园！请选择：'%(status_dict['username'])).strip()

    if homepage_choice == '1':
        login()
    elif homepage_choice == '2':
        register()
    elif homepage_choice == '3':
        article()
    elif homepage_choice == '4':
        comment()
    elif homepage_choice == '5':
        diary()
    elif homepage_choice == '6':
        favorite()
    elif homepage_choice == '7':
        logout()
    elif homepage_choice == '8':
        print('程序退出')
        break
    else:
        print('您的输入有误，请重新输入！')
