#!/bin/bash
import sys
from GlobalDefine import global_define
import read_fun

def read_util_ok():
    while input() != "OK":
        pass


def finish():
    sys.stdout.write('OK\n')
    sys.stdout.flush()


if __name__ == '__main__':
    read_util_ok()
    finish()

    # 初始化全局属性表和状态表
    global_define._init()
    # global_define.get_subject_value(1, 'sold_price')

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        parts = line.split(' ')
        frame_id = int(parts[0])# 帧序号
        money = int(parts[1])# 当前帧的金币数

        # read_util_ok()
        # 换成重写的接收函数
        read_fun.read_until_ok()

        # 测试全局变量读写正常
        # print(global_define.get_workload_state(2, 'gene_state'))

        # print(frame_id)

        sys.stdout.write('%d\n' % frame_id)
        line_speed, angle_speed = 3, 1.5
        for robot_id in range(4):
            sys.stdout.write('forward %d %d\n' % (robot_id, line_speed))
            sys.stdout.write('rotate %d %f\n' % (robot_id, angle_speed))

        # 测试运动控制
        # angle_speed = global_define.get_robot_state(3, 'angle_speed')
        # if angle_speed == 0.0:
        #    angle_speed = float(1.5)
        # else:
        #    angle_speed += float(1)

        # sys.stdout.write('rotate %d %f\n' % (3, angle_speed))

        finish()
