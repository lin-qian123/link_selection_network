import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

# 创建一个空的无向图
G = nx.Graph()

# 添加初始节点
G.add_node(0)
G.add_node(1)
G.add_edge(0, 1)

nn = 1000
# 迭代nn步
for i in range(2, nn+1):
    # 随机选择一个原有的链接
    existing_link = random.choice(list(G.edges()))
    # 随机选择链接的一端
    existing_node = random.choice(existing_link)
    # 添加新节点
    G.add_node(i)
    # 将新节点连接到选择的一端                                                       
    G.add_edge(i, existing_node)

# # 打印节点序号和度
# print(G.degree())

# # 绘制网络图
# # 初始化节点颜色列表
# node_colors = []

# # 遍历所有节点，根据度设置颜色
# for node in G.nodes():
#     if G.degree(node) > 10:
#         node_colors.append('red')  # 度大于10的节点为红色
#     else:
#         node_colors.append('green')  # 其他节点为蓝色

# # 绘制网络图，指定节点颜色
# nx.draw(G, node_color=node_colors, node_size=5)
# plt.show()

# # 绘制度分布图
# degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
# degree_sequence = np.array(degree_sequence)
# unique_values, counts = np.unique(degree_sequence, return_counts=True)

# # 作截断并拟合
# uni = unique_values[0:-5]
# cou = counts[0:-5]
# x = np.log(uni)
# y = np.log(cou/nn)
# k, b = np.polyfit(x, y, 1)
# print(k, b)
# yy = np.exp(b) * uni**k 

# # 作图
# plt.loglog(unique_values, counts/nn, marker='.', linestyle='none')
# plt.loglog(uni, yy, color='r')
# plt.title("Degree Distribution")
# plt.xlabel("Degree")
# plt.ylabel("P_k")
# plt.show()

