from itertools import combinations
import random


def is_equal_array(array1, array2):
    if sorted(array1) == sorted(array2):
        return True
    else:
        return False


def exist_array(array, matrix):
    for arr in matrix:

        if is_equal_array(arr, array):
            return True
    return False


def get_another_node(node, edge):
    if node == edge[0]:
        return edge[1]
    else:
        return edge[0]


def get_rest_of_array(sub_array, array):
    rest_array = []
    for element in array:
        if element not in sub_array:
            rest_array.append(element)

    return rest_array


def get_added_nodes(now_node, new_edge_list):
    added_nodes = [now_node]

    for edge in new_edge_list:
        if now_node == edge[0]:
            added_nodes.append(edge[1])

    for now_node in added_nodes:
        for edge in new_edge_list:
            if now_node == edge[0]:
                another_node = edge[1]
                if not another_node in added_nodes:
                    added_nodes.append(another_node)

    return added_nodes


class Graph:

    def __init__(self, adj_list, weights_list):
        self.adj_list = adj_list
        self.edge_list = self.get_edge_list()
        self.weight_list = weights_list
        self.start = 0
        self.finish = len(self.adj_list) - 1

    def get_random_weight_list(self):
        weight_list = []
        for _ in range(len(self.edge_list)):
            weight_list.append(random.randint(0, 10))
        return weight_list

    def get_edge_list(self):
        edge_list = []

        for index in range(len(self.adj_list)):
            for node in self.adj_list[index]:

                if not exist_array([index, node], edge_list):
                    edge_list.append([index, node])

        return edge_list

    def get_new_edges_list(self, count):
        changed_edge_lists = [comb for comb in combinations(self.edge_list, count)]
        return changed_edge_lists

    def is_cutted(self, new_edge_list):
        addes_nodes = get_added_nodes(0, new_edge_list)

        # print(addes_nodes)
        if not self.finish in addes_nodes or not self.start in addes_nodes:
            rest_node_list = []

            for node in range(len(self.adj_list)):
                if node not in addes_nodes:
                    rest_node_list.append(node)

            rest_graph_edge_list = []
            for edge in new_edge_list:
                if edge[0] in rest_node_list and edge[1] in rest_node_list:
                    rest_graph_edge_list.append(edge)

            rest_added_node_list = get_added_nodes(rest_node_list[0], rest_graph_edge_list)

            if len(rest_added_node_list) == len(rest_node_list):
                return True
            else:
                return False
        else:
            return False

    def check_is_cut(self, count):
        changed_edged_lists = self.get_new_edges_list(count)

        for changed_edged_list in changed_edged_lists:
            print(changed_edged_list)
            print(self.is_cutted(changed_edged_list))

    def get_min_cut_path(self):
        minCut_list = []
        min_cat_weight = sum(self.weight_list)

        for count in range(len(self.edge_list), 0, -1):
            changed_edged_lists = self.get_new_edges_list(count)
            for changed_edged_list in changed_edged_lists:

                if self.is_cutted(changed_edged_list):
                    cut = get_rest_of_array(changed_edged_list, self.edge_list)
                    cut_weight = self.get_weight_of_cut(cut)

                    if cut_weight == min_cat_weight:
                        minCut_list.append(cut)
                        min_cat_weight = cut_weight
                    elif cut_weight < min_cat_weight:
                        minCut_list = [cut]
                        min_cat_weight = cut_weight

        print('Значение минимального разреза: {}'.format(min_cat_weight))
        return minCut_list

    def get_index_of_edge(self, edge):
        for index in range(len(self.edge_list)):
            if edge == self.edge_list[index]:
                return index

    def get_weight_of_cut(self, cut_list):
        weight = 0
        for edge in cut_list:
            weight += self.weight_list[self.get_index_of_edge(edge)]

        return weight
