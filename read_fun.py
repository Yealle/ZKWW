import sys
from GlobalDefine import global_define

def read_until_ok():
    # 接收标准输入K行工作台数据

    k = int(sys.stdin.readline())
    # 接收k行工作台数据
    for i in range(k):
        line = input()
        parts = line.split(' ')
        # 工作台类型 坐标_x 坐标_y 剩余生产时间 原材料格状态 产品格状态
        dic = {'type': int(parts[0]),
                'coordinate_x': float(parts[1]),
                'coordinate_y': float(parts[2]),
                'remain_time': int(parts[3]),
                'ingre_state': int(parts[4]),# 还要进行二进制位表转换
                'gene_state': int(parts[5])}
        global_define.set_workload_state(i, dic)# workload_state[i] = dic

    # 接收4行机器人数据和OK
    for i in range(4):
        line = input()
        parts = line.split(' ')
        # 所处工作台ID（与WorkloadState（字典）的key值对应） 携带物品类型 时间价值系数
        # 碰撞价值系数 角速度 线速度_x 线速度_y 朝向 坐标_x 坐标_y
        dic = {
            'workloadID': int(parts[0]),
            'subject_type': int(parts[1]),
            'time_value': float(parts[2]),
            'crash_value': float(parts[3]),
            'angle_speed': float(parts[4]),
            'line_speed_x': float(parts[5]),
            'line_speed_y': float(parts[6]),
            'towards': float(parts[7]),
            'coordinate_x': float(parts[8]),
            'coordinate_y': float(parts[9])}
        global_define.set_robot_state(i, dic)# robot_state[i] = dic
    # input()=="OK"
    if input() == "OK":
        return
