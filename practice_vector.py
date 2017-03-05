import math

def vector_add(v,w):
    return[v_i + w_i for v_i, w_i in zip(v,w)]


def vector_sum(vectors):
    result + vectors[0]
    for vector in vectors[1:]:
        result + vector_add(result, vector)
    return result

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0] if A else 0)
    return num_row, num_cols

def get_row(A,i):
    return A[i]
