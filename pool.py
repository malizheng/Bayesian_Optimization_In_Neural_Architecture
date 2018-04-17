from layer_graph import layers, layer_graph

class pool(object):
    def __init__(self):
        self.pool = []
        G = layer_graph(57784)
        G.add_node(layers.ip)
        G.append(layers.conv3, 64)
        G.append(layers.conv3, 64)
        G.append(layers.maxpool)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.maxpool)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.maxpool)
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 256)
        G.append(layers.maxpool)
        G.append(layers.conv3, 512)
        G.append(layers.conv3, 512)
        G.append(layers.maxpool)
        G.append(layers.fc, 128)
        G.append(layers.fc, 256)
        G.append(layers.fc, 512)
        G.append(layers.softmax)
        G.append(layers.op)
        G.update_lm()
        self.pool.append(G)
        G = layer_graph(92111)
        G.add_node(layers.ip)
        G.append(layers.conv3, 64)
        G.append(layers.conv3, 64)
        G.append(layers.maxpool)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.maxpool)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.maxpool)
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 256)
        G.append(layers.maxpool)
        G.append(layers.conv3, 512)
        G.append(layers.conv3, 512)
        G.append(layers.conv3, 512)
        G.append(layers.maxpool)
        G.append(layers.fc, 128)
        G.append(layers.fc, 256)
        G.append(layers.fc, 512)
        G.append(layers.softmax)
        G.append(layers.op)
        G.update_lm()
        self.pool.append(G)
        G = layer_graph(126517)
        G.add_node(layers.ip)
        G.append(layers.conv3, 64)
        G.append(layers.conv3, 64)
        G.append(layers.maxpool)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.maxpool)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.maxpool)
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 256)
        G.append(layers.maxpool)
        G.append(layers.conv3, 512)
        G.append(layers.conv3, 512)
        G.append(layers.conv3, 512)
        G.append(layers.conv3, 512)
        G.append(layers.maxpool)
        G.append(layers.fc, 128)
        G.append(layers.fc, 256)
        G.append(layers.fc, 512)
        G.append(layers.softmax)
        G.append(layers.op)
        G.update_lm()
        self.pool.append(G)
        G = layer_graph(57735)
        G.add_node(layers.ip)
        G.append(layers.conv7, 64)
        G.append(layers.maxpool)
        G.append(layers.conv3, 64) #conv 3 / 2
        G.append(layers.conv3, 64)
        G.append(layers.conv3, 128) #conv 3 / 2
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 256) #conv 3 / 2
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 512) #conv 3 / 2
        G.append(layers.conv3, 512)
        G.append(layers.avgpool)
        G.append(layers.fc, 1024)
        G.append(layers.softmax)
        G.append(layers.op)
        G.update_lm()
        self.pool.append(G)
        G = layer_graph(92551)
        G.add_node(layers.ip)
        G.append(layers.conv7, 64)
        G.append(layers.maxpool)
        G.append(layers.conv3, 64) #conv 3 / 2
        G.append(layers.conv3, 64)
        G.append(layers.conv3, 64)
        G.append(layers.conv3, 128) #conv 3 / 2
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 256) #conv 3 / 2
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 512) #conv 3 / 2
        G.append(layers.conv3, 512)
        G.append(layers.conv3, 512)
        G.append(layers.avgpool)
        G.append(layers.fc, 1024)
        G.append(layers.softmax)
        G.append(layers.op)
        G.update_lm()
        self.pool.append(G)
        G = layer_graph(31659)
        G.add_node(layers.ip)
        G.append(layers.conv7, 64)
        G.append(layers.maxpool)
        G.append(layers.conv3, 64) #conv 3 / 2
        G.append(layers.conv3, 64)
        G.append(layers.conv3, 64)
        G.append(layers.conv3, 64)
        G.append(layers.conv3, 128) #conv 3 / 2
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 256) #conv 3 / 2
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 256)
        G.append(layers.avgpool)
        G.append(layers.fc, 512)
        G.append(layers.softmax)
        G.append(layers.op)
        G.update_lm()
        self.pool.append(G)
        G = layer_graph(127367)
        G.add_node(layers.ip)
        G.append(layers.conv7, 64)
        G.append(layers.maxpool)
        G.append(layers.conv3, 64) #conv 3 / 2
        G.append(layers.conv3, 64)
        G.append(layers.conv3, 64)
        G.append(layers.conv3, 64)
        G.append(layers.conv3, 128) #conv 3 / 2
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 128)
        G.append(layers.conv3, 256) #conv 3 / 2
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 256)
        G.append(layers.conv3, 512) #conv 3 / 2
        G.append(layers.conv3, 512)
        G.append(layers.conv3, 512)
        G.append(layers.conv3, 512)
        G.append(layers.avgpool)
        G.append(layers.fc, 1024)
        G.append(layers.softmax)
        G.append(layers.op)
        G.update_lm()
        self.pool.append(G)
        print(len(self.pool))

if __name__ == '__main__':
    P = pool()
