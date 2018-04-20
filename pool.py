from layer_graph import LAYERS, Layer_graph
import matplotlib.pyplot as plt
import numpy as np
import copy
import math
from model_util import NetModel

class Pool(object):
    def __init__(self):
        self.models = []
        G = Layer_graph(57784)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.fc, 128)
        G.append(LAYERS.fc, 256)
        G.append(LAYERS.fc, 512)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.finish()
        self.models.append((G, -math.log(0.1)))
        G = Layer_graph(92111)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.fc, 128)
        G.append(LAYERS.fc, 256)
        G.append(LAYERS.fc, 512)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.finish()
        self.models.append((G, -math.log(0.3)))
        G = Layer_graph(126517)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.fc, 128)
        G.append(LAYERS.fc, 256)
        G.append(LAYERS.fc, 512)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.finish()
        self.models.append((G, -math.log(0.4)))
        G = Layer_graph(57735)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv7, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 64) #conv 3 / 2
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 128) #conv 3 / 2
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 256) #conv 3 / 2
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 512) #conv 3 / 2
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.avgpool)
        G.append(LAYERS.fc, 1024)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.finish()
        self.models.append((G, -math.log(0.6)))
        G = Layer_graph(92552)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv7, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 64) #conv 3 / 2
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 128) #conv 3 / 2
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 256) #conv 3 / 2
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 512) #conv 3 / 2
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.avgpool)
        G.append(LAYERS.fc, 1024)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.finish()
        self.models.append((G, -math.log(0.85)))
        G = Layer_graph(31659)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv7, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 64) #conv 3 / 2
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 128) #conv 3 / 2
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 256) #conv 3 / 2
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.avgpool)
        G.append(LAYERS.fc, 512)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.finish()
        self.models.append((G, -math.log(0.9)))
        G = Layer_graph(127367)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv7, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 64) #conv 3 / 2
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 128) #conv 3 / 2
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 256) #conv 3 / 2
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 512) #conv 3 / 2
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.avgpool)
        G.append(LAYERS.fc, 1024)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.finish()
        self.models.append((G, -math.log(0.95)))
        print(len(self.models))

    def get_layer_graph(self, graph_idx):
        return self.models[graph_idx][0]

    def get_layer_graph_acc(self, graph_idx):
        return self.models[graph_idx][1]

    def mutate_layer_graph(self, graph_idx):
        mut_graph = copy.deepcopy(self.get_layer_graph(graph_idx))
        mut_graph.mutate()
        self.models.append((mut_graph, None))



if __name__ == '__main__':
    '''
    G = Layer_graph(1)
    G.add_node(LAYERS.ip)
    G.append(LAYERS.fc, 1024)
    G.append(LAYERS.fc, 1024)
    G.append(LAYERS.fc, 1024)
    G.append(LAYERS.fc, 1024, append_to=0)
    G.append(LAYERS.fc, 1024)
    G.append(LAYERS.fc, 1024, append_to=0)
    G.add_edge(6, 3)
    G.add_edge(5, 3)
    G.show_graph()
    plt.show()
    for i in G.get_nodes():
        print(i)
    '''
    P = Pool()
    # P.mutate_layer_graph(0)
    mut_pool = P.get_layer_graph(6).copy()
    mut_pool.mutate()
    # print(netModel.K([P.get_layer_graph(1), P.get_layer_graph(0)], [P.get_layer_graph(1), P.get_layer_graph(0)]))
    # gt1 = P.get_layer_graph(3)
    # gt2 = P.get_layer_graph(4)
    # print(netModel.mean_cond([P.get_layer_graph(5)], [gt1,gt2], [0.1,0.2]))
    # print(netKernel.K([P.get_layer_graph(1), P.get_layer_graph(0)], [P.get_layer_graph(1), P.get_layer_graph(0)]))
    X = list(list(zip(*(P.models)))[0])
    Y = list(list(zip(*(P.models)))[1])
    netModel = NetModel(X)
    # for i in range(100):
    #     print(netModel.post_K(mut_pool, mut_pool, X))
    #     mut_pool.mutate()
    # print(netModel.post_K(mut_pool, mut_pool, X))
    # print(netModel.acquisition_func(mut_pool, X, Y, max(Y)))
    # print(netModel.post_dist(mut_pool, 0.9, X, Y))
    netModel.mcmc(Y)
    for x in range(10):
        pass
        print(netModel.marginal_acquisition_func(mut_pool, Y, min(Y), sample_time=100))
    # mut_pool.show_graph()
    # plt.show()
