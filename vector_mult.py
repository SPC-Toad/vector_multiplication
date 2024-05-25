import numpy as np

def inner_product(u: np.array, v: np.array) -> float:
    """computes the inner product of two vectors

    Paramters:

    u: 1D numpy array
    v: 1D numpy array

    Preconditions:

    u.ndim == 1                # u is a 1D array
    v.ndim == 1                # v is a 1D array
    str(u.dtype) == 'float64'  # u is a vector of floats
    str(v.dtype) == 'float64'  # v is a vector of floats
    u.shape[0] == v.shape[0]   # the vectors are the same size

    Returns:

    u1 * v1 + u2 * v2 + ... + un * vn

    Example:

    >>> inner_product(np.array([1., 2, 0]), np.array([3., 1, 0]))
    5.0

    """
    # TODO: fill in this function and change the return value
    # Corner Case, checks if 1D and float64 type.
    if (u.ndim == v.ndim and str(u.dtype) == 'float64' and str(v.dtype) == 'float64') : 
        vec = 0.0;
        x = u.shape[0]
        y = v.shape[0]
    # If the size of the array are equal, then perform operation.
    if (x == y) : 
        for i in range(x) : 
            vec += u[i] * v[i];
        return vec;
    else :
        return None;

def column(a: np.array, i: int) -> np.array:
    """returns the column of a matrix at a given index

    Parameters:

    a: 2D numpy array
    i: index for a column of a

    Preconditions:

    a.ndim == 2                # a is 2 dimensional
    0 <= i and i < a.shape[1]  # i is a valid index

    Returns:

    the i-th column of a

    Example:

    >>> column(np.array([[0., 1], [1, 0]]), 1)
    array([1., 0.])

    """
    # Note this for future reference
    # Make sure you understand how it works
    return a[:, i]

def mat_vec_mult_ip(a: np.array, v: np.array) -> np.array:
    """computes matrix-vector multiplication via the row-column rule

    Parameters:

    a: 2D numpy array
    v: 1D numpy array

    Preconditions:

    str(a.dtype) == 'float64'
    str(v.dtype) == 'float64'
    a.ndim == 2
    v.ndim == 1
    a.shape[1] == v.shape[0] # num of cols of a == num of rows of v

    Returns:

    a * v (computed via the row-column rule)

    Example:

    >>> mat_vec_mult_ip(np.array([[2., 0], [0, 3]]), np.array([1., 1]))
    array([2., 3.])

    """
    # TODO: fill in this function and change the return value
    # Corner Case, checks if 2D and 1D and float64 type.
    if (a.ndim == 2 and v.ndim == 1 and str(a.dtype) == 'float64' and str(v.dtype) == 'float64' and a.shape[0] != 0 and  a.shape[1] != 0 and v.shape[0] != 0) :
        m = a.shape[0]
        n = a.shape[1]
        y = v.shape[0]
        if (n == y) :                                   # if the number of column for matrix A is equal to size of column vector of v, and they are not empty
            arr = np.zeros(m);                          # initialize the 1D array to zero vector.
            for i in range(m) : 
                arr[i] = inner_product(a[i], v);        # Each arr index will the sum of vector multiplication.
            return arr
        else : 
            return None;    
    else : 
        return None;                                    # Return null

def mat_vec_mult_vs(a: np.array, v: np.array) -> np.array:
    """computes matrix-vector multiplication via the linear combination of columns

    Parameters:

    a: 2D numpy array
    v: 1D numpy array

    Preconditions:

    str(dtype(a)) == 'float64'
    str(dtype(v)) == 'float64'
    a.ndim == 2
    v.ndim == 1
    a.shape[1] == v.shape[0]

    Returns:

    a * v (computed as v1 * a1 + v2 * a2 + ... + vn * an)

    Example:
    >>> mat_vec_mult_vs(np.array([[2., 0], [0, 3]]), np.array([1., 1]))
    array([2., 3.])

    """
    # TODO: fill in this function and change the return value
    # Corner Case, checks if 2D and 1D and float64 type.
    if (a.ndim == 2 and v.ndim == 1 and str(a.dtype) == 'float64' and str(v.dtype) == 'float64' and a.shape[1] != 0 and v.shape[0] != 0) :
        n = a.shape[1]
        y = v.shape[0]
        if (n == y and n != 0 and y != 0) :         # if the number of column for matrix A is equal to size of column vector of v, and they are not empty
            arr = np.zeros(n);                      # initialize the 1D array to zero vector.
            for i in range(n) :
                arr += column(a, i) * v[i]          # Every iteration, add the v_i * (ith column of 'a') to arr
            return arr                              # return the arr
        else : 
            return None;    
    else : 
        return None;                                # Else return null.


# Test Cases

n = np.array([1., 2, 3, 4])
m = np.array([1., 2, 3, 4])
x = np.array([1., 2, 3])
y = np.array([1., 2, 3, 4, 5])
z = np.array([0., 0, 0, 0])
f = np.array([0., 0, 0, 1])

a = np.array(
    [[1., 2, 3, 4],
     [1, 2, 3, 4],
     [1, 2, 3, 4],
     [1, 2, 3, 4]]
)

b = np.array(
    [[1., 1, 1, 1],
     [0, 1, 1, 1],
     [0, 0, 1, 1],
     [0, 0, 0, 1]]
)

testing_1 = np.array(
    [[1., 1, 1],
     [0, 1, 1],
     [0, 0, 1],
     [0, 0, 0]]
)

testing_2= np.array(
    [[1., 1, 1, 1],
     [0, 1, 1, 1],
     [0, 0, 1, 1],
     [0, 0, 0, 1]]
) 

testing_3= np.array(
    [[]]
) 

testing_4= np.array(
    [[1.]]
) 

testing_5= np.array(
    [2.]
) 

testing_6= np.array(
    []
) 

print("Test 1:")
print("Expected:")
print("4.0")
print()
print("Got: ")
print(inner_product(f, n))
print("----------------------------------")

print("Test 2:")
print("Expected:")
print("0.0")
print()
print("Got: ")
print(inner_product(n, z))
print("----------------------------------")

print("Test 3:")
print("Expected:")
print("None or False")
print()
print("Got: ")
print(inner_product(x, y))
print("----------------------------------")

print("Test 4:")
print("Expected:")
print("None or False")
print()
print("Got: ")
print(mat_vec_mult_ip(testing_1, n))
print(mat_vec_mult_vs(testing_1, n))
print("----------------------------------")

print("Test 5:")
print("Expected:")
print("[10.  9.  7.  4.]")
print()
print("Got: ")
print(mat_vec_mult_ip(testing_2, n))
print(mat_vec_mult_vs(testing_2, n))
print("----------------------------------")

print("Test 6:")
print("Expected:")
print("[30. 30. 30. 30.]")
print()
print("Got: ")
print(mat_vec_mult_ip(a, n))
print(mat_vec_mult_vs(a, n))
print("----------------------------------")

print("Test 7:")
print("Expected:")
print("None or False")
print()
print("Got: ")
print(mat_vec_mult_ip(testing_3, testing_6))
print(mat_vec_mult_vs(testing_3, testing_6))
print("----------------------------------")

print("Test 8:")
print("Expected:")
print("None or False")
print()
print("Got: ")
print(mat_vec_mult_ip(n, m))
print(mat_vec_mult_vs(n, m))
print("----------------------------------")

print("Test 9:")
print("Expected:")
print("[2.]")
print()
print("Got: ")
print(mat_vec_mult_ip(testing_4, testing_5))
print(mat_vec_mult_vs(testing_4, testing_5))
print("----------------------------------")
