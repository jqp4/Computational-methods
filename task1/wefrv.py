from SLE import SLE
from Gauss import gauss
from DataSet import DataSet
from linalg import det, inverse, print_matrix, cond, norm


import numpy as np



def main():
    dataset = DataSet()
    for i in range(dataset.len):
        print("--------------------------------------------")
        print("СЛАУ № {}:\n".format(i + 1))
        dataset.sle[i].show()
        print("  1) Решение заданной СЛАУ методом Гаусса:", end = "\n      ")
        X = gauss(dataset.sle[i], mainElement=False)
        if (X is None):
            print("Матрица A вырождена!")
            print("      det(A) = {0:.2f}".format(det(dataset.sle[i].A)))
        else:
            print("\n      ".join("x{0} = {1:6.2f}".format(i + 1, x) for i, x in enumerate(X)))
            print("     Решение заданной СЛАУ методом Гаусса с выбором главного элемента:", end = "\n      ")
            X = gauss(dataset.sle[i])
            print("\n      ".join("x{0} = {1:6.2f}".format(i + 1, x) for i, x in enumerate(X)))
        
            print("  2) Определитель матрицы det(A):")
            print("      det(A) = {0:.2f}".format(det(dataset.sle[i].A)))

            print("  3) Обратная матрица A^-1:")
            print_matrix(inverse(dataset.sle[i].A), shift="      ")

            print("  4) Число обусловленности МA = ||A||×||A^-1||:")
            print("     norm(A) = {0:.2f}".format(norm(dataset.sle[i].A)))
            print("     norm(A^-1) = {0:.2f}".format(norm(inverse(dataset.sle[i].A))))
            print("     cond(A) = {0:.2f}".format(cond(dataset.sle[i].A)))
            print("     np.norm(A) = {0:.2f}".format(np.linalg.norm(dataset.sle[i].A)))
            print("     np.norm(A^-1) = {0:.2f}".format(np.linalg.norm(inverse(dataset.sle[i].A))))
            print("     np.cond(A) = {0:.2f}".format(np.linalg.cond(dataset.sle[i].A)))
            

    print("--------------------------------------------")


main()