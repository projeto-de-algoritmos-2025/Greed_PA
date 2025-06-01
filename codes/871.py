import heapq
from typing import List

class Solution:
    def minRefuelStops(self, destino: int, combustivel_inicial: int, postos: List[List[int]]) -> int:
        
        return self._algoritmo_trocador_paradas(destino, combustivel_inicial, postos)

    def _algoritmo_trocador_paradas(self, destino: int, combustivel_inicial: int, postos: List[List[int]]) -> int:
        
        postos.append([destino, 0])
        max_heap = []  
        combustivel = combustivel_inicial
        paradas = 0
        posicao_anterior = 0

        for posicao, gasolina in postos:
            
            combustivel -= (posicao - posicao_anterior)

            
            while combustivel < 0 and max_heap:
                combustivel += -heapq.heappop(max_heap)  
                paradas += 1

            
            if combustivel < 0:
                return -1

            
            heapq.heappush(max_heap, -gasolina)
            posicao_anterior = posicao

        return paradas


def executar_casos_de_teste():
    casos_de_teste = [
        {"destino": 1, "combustivel_inicial": 1, "postos": [], "esperado": 0},
        {"destino": 100, "combustivel_inicial": 1, "postos": [[10, 100]], "esperado": -1},
        {"destino": 100, "combustivel_inicial": 10, "postos": [[10, 60], [20, 30], [30, 30], [60, 40]], "esperado": 2},
    ]

    solucao = Solution()
    for i, caso in enumerate(casos_de_teste, start=1):
        resultado = solucao.minRefuelStops(
            caso["destino"],
            caso["combustivel_inicial"],
            caso["postos"]
        )
        if resultado == caso["esperado"]:
            print(f"Teste {i}: Deu certo!  (Esperado: {caso['esperado']}, Obtido: {resultado})")
        else:
            print(f"Teste {i}: Não deu certo :/ (Esperado: {caso['esperado']}, Obtido: {resultado})")


