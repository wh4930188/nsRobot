#动作指令判断函数，在此函数内判断需要采取的动作并起调相关子处理函数
#输入-message: 收到的全文本信息
#输入-QQ: 发信息的QQ号，通过主程序传递即可
#输入-name: 发来信息的昵称，用于后续相关确认通知，虽然大概率新版本不需要这样了
#输入-group: 接收到信息的群聊ID，用于后续相关确认通知，虽然大概率新版本不需要这样了

def judge(message, QQ, name, group):
    if message[:2] == 'ns': #如果开头不是ns那么一切免谈，无事发生
        command = message[2:] #把ns去掉后面开始分割这个指令
        commandPart = command.split( ) #按照空格进行分割，但是后续要看看是不是加入更多的防傻判断
        if commandPart[0] == '开团':
            date = commandPart[1]
            time = commandPart[2]
            dungeon = commandPart[3]
            comment = commandPart[4]
            if commandPart[5] == '1': #这TM判断不了直接报索引溢出就尼玛离谱，垃圾python毁我青春
                useBlackList = 1
            else:
                useBlackList = 0
            temp='收到开团指令 日期：{} 时间：{} 副本名称：{} 注释：{} 是否启用黑名单：{}'.format(date,time,dungeon,comment,useBlackList)
            print(temp)