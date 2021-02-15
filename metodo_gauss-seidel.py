import numpy as np

arredondar = lambda num: float('%.6f' % num)  # função que arredonda o nº para 6 casas decimais


def isPossibleandDeterm(matrix): # função que determina se o sistema é possível ou não
    det = np.linalg.det(matrix)  # Cálculo do determinante
    
    if (det > 0) or (det < 0):  # Sistema possivel e determinado
        return True
    elif det == 0:  # Sistema possivel e indeterminado ou impossivel
        return False


def isConvergent(matrix_original):   # critério de convergência das linhas
    matrix = np.copy(matrix_original)
    diag = matrix.diagonal()
    copy = np.copy(diag)    # é preciso copiar pois o diag se perde depois do fill_diagonal
    np.fill_diagonal(matrix, 0)     # ESSA FUNÇÃO ALTERA A MATRIZ ORIGINAL, QUE _ É ESSA?
    # print('diag: ', diag) # diag some logo depois do fill_diagonal
    # print('copy: ', copy) # por isso, copia-se
    soma = np.sum(matrix, axis=1)
    for i in range(len(soma)):
        if soma[i] > copy[i]:
            return False    # O método não convergirá para uma solução; o usuário deve corrigir a ordem do sistema
    return True     # O método irá convergir para um resultado


def sciNotation(n, k):    # Notação científica -> n * 10^(k)
    a = '{}e{}'.format(n, k)
    a = float(a)
    return a


def list_to_comparate(tamanho):
    lista = [0]
    
    for i in range(0, tamanho):
        if i not in lista:
            lista.append(i)
    
    return lista


def main8():    # (14/04/2019)  # Gauss-Seidel
    contador = 1
    
    E = sciNotation(1, -1)
    
    A = np.array([[4, 2, 1],
                [1, 5, 2],
                [2, 1, 4]])
    dimAi, dimAj = A.shape  
    # print(dimAi, dimAj)
    
    B = [1, 3, -2]
    
    X = [0]*len(B)
    Xn = [0]*len(B)
    Xabs = [0]*len(B)
        
    if isPossibleandDeterm(A) == True:
        if isConvergent(A) == False:
            print('Não irá convergir; usuário, por favor altere a ordem do sistema')
            return False
        while True:
            for i in range(1, dimAi+1):
                Xn[i-1] = B[i-1]
                for j in range(1, dimAj+1):
                    # print(Xn)
                    # print(i, j)
                    if i != j:
                        if i != 0:
                            listtemp = list_to_comparate(i)
                            if j in listtemp:
                                Xn[i-1] = Xn[i-1] - (A[i-1][j-1] * Xn[j-1])
                            else:
                                Xn[i-1] = Xn[i-1] - (A[i-1][j-1] * X[j-1])
                Xn[i-1] = Xn[i-1]/A[i-1][i-1]
            
            print(Xn)
            
            for i in range(len(Xn)):
                Xabs[i] = np.abs(Xn[i] - X[i])
                if Xabs[i] > E:
                    break
            else:
                break
            
            for i in range(len(Xn)):
                X[i] = Xn[i]
            
            contador += 1
            # print('=================')
        
        
        for i in range(len(Xn)):
            Xn[i] = arredondar(Xn[i])
        
        print('final:', Xn)
        print('contador:', contador)
    
    else:
        print('O Sistema é possivel e indeterminado ou impossivel')


if __name__ == '__main__':
    main8()
