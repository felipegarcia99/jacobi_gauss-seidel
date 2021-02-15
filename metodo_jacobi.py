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


def main6():  # código principal: Método de Jacobi
    contador = 1
    
    E = sciNotation(1, -4)  # definição do erro E = 0.0001
    
    A = np.array([[4, 2, 1],  # matriz dos coeficientes
                [1, 5, 2],
                [2, 1, 4]])
    dimAi, dimAj = A.shape    # nº de linha e colunas da matriz A
    
    B = [1, 3, -2]  # matriz dos termos independentes
    
    # Criação das matrizes (zeradas com o tamanho do vetor B)
    X = [0]*len(B)  # matriz solução (k)
    Xn = [0]*len(B)  # matriz auxiliar (k+1)
    Xabs = [0]*len(B) # matriz que armazena o resultado do módulo da subtração de xi(k+1) - xi(k)
        
    if isPossibleandDeterm(A) == True: # Cálculo do sistema
        if isConvergent(A) == False:
            print('Não irá convergir; usuário, por favor altere a ordem do sistema')
            return False
        #  Enquanto o módulo da subtração de xi(k+1) - xi(k) < E, continua o cálculo
        while True:
            for i in range(1, dimAi+1):
                Xn[i-1] = B[i-1]
                for j in range(1, dimAj+1):
                    if i != j:
                        Xn[i-1] = Xn[i-1] - (A[i-1][j-1] * X[j-1])
                Xn[i-1] = Xn[i-1]/A[i-1][i-1]    
                
            print(Xn)
            
            # Cálculo de max|xi(k+1) - xi(k)|
            for i in range(len(Xn)):
                Xabs[i] = np.abs(Xn[i] - X[i]) # Cálculo do módulo
                if Xabs[i] > E:
                    break
            else:  # Se todas as subtrações passarem pelo critério, logo essa é a solução, e quebra-se o laço
                break
            
            for i in range(len(Xn)): # matriz solução recebe novos valores para nova iteração
                X[i] = Xn[i]
            
            contador += 1
			# fim do laço
			
        for i in range(len(Xn)):
            Xn[i] = arredondar(Xn[i]) # arredonda os valores
        
        print('final:', Xn)  # solução final
        print('contador:', contador)  # contador: nº de iterações
    
    else:
        print('O Sistema é possivel e indeterminado ou impossivel')


if __name__ == '__main__':
    main6()
