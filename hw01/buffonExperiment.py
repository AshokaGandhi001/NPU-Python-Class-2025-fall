import random
import math

def buffon_needle_simulation(num_throws):
    """
    模拟蒲丰投针实验来估算圆周率 Pi。

    参数:
        num_throws (int): 投掷针的次数。

    返回:
        float 或 str: Pi 的估算值，如果相交次数为0则返回提示信息。
    """
    # 根据文档描述设置参数:
    # 平行线之间的距离 'a'
    # 针的长度 'b'
    # 条件是 b = 1/2 * a
    # 为了简化计算，我们可以设定 a = 1，那么 b = 0.5。
    # 在这种设定下，针与线相交的概率 P = (2 * b) / (π * a) = (2 * 0.5) / (π * 1) = 1 / π。
    # 因此，Pi 的估算值为 (投掷总次数) / (相交次数)。

    line_distance = 1.0  # 平行线之间的距离，对应文档中的 'a'
    needle_length = line_distance / 2.0  # 针的长度，对应文档中的 'b'，满足 b = a/2

    intersections = 0  # 记录相交的次数

    for _ in range(num_throws):
        # 1. 生成针中心的 y 坐标
        # 我们可以假设针中心在 [0, line_distance] 之间均匀分布。
        # 这样，我们只需要考虑针是否跨越 y=0 或 y=line_distance 这两条线。
        y_center = random.uniform(0, line_distance)

        # 2. 生成针与平行线（x 轴）的夹角 theta
        # theta 在 [0, π] 之间均匀分布 (弧度)。
        theta = random.uniform(0, math.pi)

        # 计算针的垂直投影的一半长度
        # 这是 (needle_length / 2) * sin(theta)
        vertical_half_projection = (needle_length / 2) * math.sin(theta)

        # 判断针是否与任何一条平行线相交：
        # 如果针的下端 (y_center - vertical_half_projection) 跨越了 y=0，则相交。
        # 如果针的上端 (y_center + vertical_half_projection) 跨越了 y=line_distance，则相交。
        
        # 检查是否跨越下界线 (y=0)
        crosses_lower_line = y_center <= vertical_half_projection
        
        # 检查是否跨越上界线 (y=line_distance)
        # 这等价于 (line_distance - y_center) <= vertical_half_projection
        crosses_upper_line = (line_distance - y_center) <= vertical_half_projection

        if crosses_lower_line or crosses_upper_line:
            intersections += 1

    if intersections == 0:
        return "相交次数不足以估算 Pi (请尝试增加投掷次数)"
    
    # 根据数学原理，Pi 的估算值为 (投掷总次数) / (相交次数)
    estimated_pi = num_throws / intersections
    return estimated_pi

# --- 运行示例 ---
if __name__ == "__main__":
    print("--- 蒲丰投针实验估算 Pi ---")
    
    throws_list = [1000, 10000, 100000, 1000000, 10000000] # 不同投掷次数进行测试

    for num_throws in throws_list:
        estimated_pi = buffon_needle_simulation(num_throws)
        print(f"\n投掷次数: {num_throws}")
        print(f"估算 Pi: {estimated_pi}")
        print(f"Python 内置 Pi: {math.pi}")
        if isinstance(estimated_pi, float):
            print(f"误差: {abs(estimated_pi - math.pi):.6f}")
            print(f"相对误差: {abs((estimated_pi - math.pi) / math.pi) * 100:.4f}%")
        else:
            print(estimated_pi) # 打印错误信息
