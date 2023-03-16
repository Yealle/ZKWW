# 用于管理全局表 并实现全域访问
def _init():

    # SubjectDic = {'num': 1, 'generate': 'None', 'buy_price': 3000, 'sold_price': 6000}
    # 表3-2物品价格表
    global SubjectDefine
    # 物品类型为字典索引:{ 生产配方 购买价 原始出售价}
    SubjectDefine = {
        1: {'formula': 'null', 'buy_price': 3000, 'sold_price': 6000},
        2: {'formula': 'null', 'buy_price': 4400, 'sold_price': 7600},
        3: {'formula': 'null', 'buy_price': 5800, 'sold_price': 9200},
        4: {'formula': '1+2', 'buy_price': 15400, 'sold_price': 22500},
        5: {'formula': '1+3', 'buy_price': 17200, 'sold_price': 25000},
        6: {'formula': '2+3', 'buy_price': 19200, 'sold_price': 27500},
        7: {'formula': '4+5+6', 'buy_price': 76000, 'sold_price': 105000}
    }

    # 表3-3 工作台类型
    global WorkloadDefine
    # 工作台类型为为字典索引:{ 收购的原材料编号 工作周期 生产物品}
    WorkloadDefine = {
        1: {'ingredient': 'null', 'cycle': 50, 'generate': 1},
        2: {'ingredient': 'null', 'cycle': 50, 'generate': 2},
        3: {'ingredient': 'null', 'cycle': 50, 'generate': 3},
        4: {'ingredient': '1+2', 'cycle': 500, 'generate': 4},
        5: {'ingredient': '1+3', 'cycle': 500, 'generate': 5},
        6: {'ingredient': '2+3', 'cycle': 500, 'generate': 6},
        7: {'ingredient': '4+5+6', 'cycle': 1000, 'generate': 7},
        8: {'ingredient': '7', 'cycle': 1, 'generate': 0},
        9: {'ingredient': '1+2+3+4+5+6+7', 'cycle': 1, 'generate': 0}
    }

    # 工作台<=50,数量可变，同一类型工作台可能出现多次
    global workload_state
    workload_state = {
    }

    global robot_state
    # 接收4行机器人数据
    robot_state = {
    }


# 获取物品表值
def get_subject_value(subject_type, key):
    try:
        return SubjectDefine[subject_type][key]
    except KeyError:
        return None


# 获取工作台表值
def get_workload_value(workload_type, key):
    try:
        return WorkloadDefine[workload_type][key]
    except KeyError:
        return None


# 设置工作台状态值 state是一个字典
# state = {工作台类型 坐标_x 坐标_y 剩余生产时间 原材料格状态 产品格状态}
def set_workload_state(workloadID, state):
    workload_state[workloadID] = state


# 获取工作台状态值
def get_workload_state(workloadID, key):
    try:
        return workload_state[workloadID][key]
    except KeyError:
        return None


# 设置机器人状态值 state是一个字典
# state = {所处工作台ID（与WorkloadState（字典）的key值对应） 携带物品类型 时间价值系数
#          碰撞价值系数 角速度 线速度_x 线速度_y 朝向 坐标_x 坐标_y}
def set_robot_state(robotID, state):
    robot_state[robotID] = state


# 获取机器人状态值
def get_robot_state(robotID, key):
    try:
        return robot_state[robotID][key]
    except KeyError:
        return None

