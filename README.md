### Vector Multiplication

#### Overview
This project provides a Python script for performing vector and matrix multiplication operations. The main operations include:
1. **Inner Product Calculation**: Computes the inner product of two vectors.
2. **Column Extraction**: Extracts a specific column from a matrix.
3. **Matrix-Vector Multiplication**: Computes matrix-vector multiplication using the row-column rule and vector-stacking approach.

#### Requirements
- Python 3.x
- NumPy library

#### Files
1. **vector_mult.py**: Contains functions for vector and matrix operations.
2. **Makefile**: Provides a simple command to run the Python script.

#### Functions

1. **inner_product(u: np.array, v: np.array) -> float**
   - Computes the inner product of two 1D numpy arrays (vectors).
   - **Parameters**:
     - `u`: 1D numpy array of type `float64`
     - `v`: 1D numpy array of type `float64`
   - **Preconditions**:
     - Both `u` and `v` must be 1D arrays of the same size and of type `float64`.
   - **Returns**: The inner product of the two vectors if conditions are met; otherwise, returns `None`.

2. **column(a: np.array, i: int) -> np.array**
   - Returns the i-th column of a given 2D numpy array (matrix).
   - **Parameters**:
     - `a`: 2D numpy array
     - `i`: Index for the column to be extracted
   - **Preconditions**:
     - `a` must be a 2D array and `i` must be a valid column index.
   - **Returns**: The i-th column of the matrix.

3. **mat_vec_mult_ip(a: np.array, v: np.array) -> np.array**
   - Computes matrix-vector multiplication using the row-column rule.
   - **Parameters**:
     - `a`: 2D numpy array (matrix) of type `float64`
     - `v`: 1D numpy array (vector) of type `float64`
   - **Preconditions**:
     - `a` must be a 2D array and `v` must be a 1D array, both of type `float64`.
   - **Returns**: The resulting vector from the matrix-vector multiplication.

4. **mat_vec_mult_vs(a: np.array, v: np.array) -> np.array**
   - Computes matrix-vector multiplication using the vector-stacking approach.
   - **Parameters**:
     - `a`: 2D numpy array (matrix) of type `float64`
     - `v`: 1D numpy array (vector) of type `float64`
   - **Preconditions**:
     - `a` must be a 2D array and `v` must be a 1D array, both of type `float64`.
   - **Returns**: The resulting vector from the matrix-vector multiplication.

#### Usage

To run the script, simply use the provided `Makefile`. The `Makefile` contains a target to execute the Python script.

1. Open a terminal and navigate to the directory containing the files.
2. Run the following command:
   ```bash
   make run
   ```

This command will execute the `vector_mult.py` script using Python 3.

#### Examples

```
they are provided in the bottom section of vector_mult.py
```
