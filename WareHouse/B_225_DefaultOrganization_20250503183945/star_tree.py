'''
Module to determine if a tree is a star tree based on vertex degrees.
'''
def is_star_tree(degree):
    '''
    Function to check if the given tree is a star tree.
    A star tree has one center vertex with degree N-1 and N-2 leaf vertices with degree 1.
    Parameters:
    degree (list): List of degrees of vertices.
    Returns:
    str: "YES" if the tree is a star, otherwise "NO".
    '''
    N = len(degree) - 1  # Since degree[0] is unused
    center_count = degree.count(N - 1)
    leaf_count = degree.count(1)
    if center_count == 1 and leaf_count == N - 2:
        return "YES"
    else:
        return "NO"