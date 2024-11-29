import numpy as np 

matrix = np.array([[6,2,3],[2,7,4],[3,4,8]])
x_0 = np.array([1,1,1])
b =  np.array([1,2,3])





def gcc_iterate(k):
    r_k  = b - matrix.dot(x_0)
    d_k = r_k
    x_k = x_0
    dot_r_k = r_k.dot(r_k)
    dot_r_next = 0
    for i in range(k):
        matrixd_k = matrix.dot(d_k)
        alph_k = dot_r_k / d_k.dot(matrixd_k) 
        x_k = x_k + alph_k * d_k
        r_k = r_k - alph_k  * matrixd_k
        dot_r_next = r_k.dot(r_k)
        bet_k = dot_r_next / dot_r_k
        d_k = r_k + bet_k * d_k
        dot_r_k = dot_r_next
        print(x_k)
    return x_k


if __name__ == '__main__':
    print(matrix.dot(gcc_iterate(3)))   

