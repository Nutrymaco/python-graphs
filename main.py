from mygraph import Graph


def main():
    adj_nodes = [
        [1, 2, 3],
        [4, 5],
        [4, 5, 6],
        [5, 6],
        [7],
        [7],
        [7],
        []
    ]
    weights = [3, 4, 5, 2, 1, 1, 2, 2, 1, 1, 3, 1, 4]

    graph = Graph(adj_nodes, weights)
    print('Список ребер: {}'.format(graph.edge_list))
    print('Веса ребер: {}'.format(graph.weight_list))
    edge_lists = graph.get_min_cut_path()

    print('Минимальные разрезы:')
    for edge_list in edge_lists:
        print(edge_list)


if __name__ == "__main__":
    main()
