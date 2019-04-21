import numpy as np 

def audithours():
    x=np.array((input("Please enter first matrix:")))
    # Entering [[3,4],[6,9]] for this example
    print(type(x)) ##Evals to numpy.ndarray
    print(x) ##Evals to [[3,4],[6,9]]
    x=np.array([[3,4],[6,9]])
    print(type(x)) Also evals to numpy.ndarray
    print(x) #evals to [[3 4]
                        [6 9]]
    z=np.array([[4],[8]])
    # z=np.array(input("Please enter second matrix:"))
    # z=np.array(z)
  try:
       y = np.linalg.inv(x)
       answer = np.matmul(y, z)
       print(answer)
   except np.linalg.LinAlgError as e:
       if "Array must be at least two-dimensional" in str(e):
           print("The matrix provided is not two dimensional, please re-enter the matrix")
       elif "Singular matrix" in str(e):
           print("The matrix provided does not have an inverse")

audithours()