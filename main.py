from hashlib import sha256
import time

def aplicar_sha256(texto):
    return sha256(texto.encode('ascii')).hexdigest()

def minerar(num_bloco, transacoes, hash_anterior, qtde_zeros):
    nonce = 0
    while True:
        texto = str(num_bloco) + transacoes + hash_anterior + str(nonce)
        novo_hash = aplicar_sha256(texto)
        if  novo_hash.startswith('0' * qtde_zeros):
            return nonce, novo_hash
        nonce += 1

if __name__ == '__main__':
    num_bloco = 15
    transacoes = '''
    Junior -> Pedro -> 20
    Junior -> Maria -> 30
    Maria -> Pedro -> 40
    '''
    qtde_zeros = 5
    hash_anterior = 'abc'
    inicio = time.time()
    resultado = minerar(num_bloco, transacoes, hash_anterior, qtde_zeros)
    print(f'Resultado: {resultado}')
    print(f'Tempo: {time.time() - inicio}')