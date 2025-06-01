# Greed_PA

**Número da Lista**: 3<br>
**Conteúdo da Disciplina**: Greed<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/2015868 |  Alexandre Lema Xavier Júnior |
| 21/1039671  |  Pedro Lopes da Cunha |

## Sobre 
Resolução de questões do LeetCode (2 difíceis e 2 médias) pelos integrantes do grupo com o objetivo de demonstrar o conhecimento adquirido nesse módulo (Greed) da disciplina.

## Questões

|Questão | Dificuldade |
| -- | -- |
| [871. Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/description/) |   Difícil |
| [2406. Divide Intervals Into Minimum Numbers of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/)  |  Média |

## Screenshots

### [871](https://leetcode.com/problems/minimum-number-of-refueling-stops/description/) - Difícil:

O problema pede o número mínimo de paradas para um carro chegar ao destino, podendo reabastecer completamente em cada posto de combustível encontrado ao longo do caminho. Para resolver, utilizei o algoritmo ganancioso conhecido como “algoritmo do caminhoneiro”, onde sempre que o carro precisa reabastecer, ele escolhe o posto que oferece o maior combustível disponível entre todos os que já passou. Comecei adicionando o destino como um último posto com zero combustível e percorri cada posto, subtraindo o combustível necessário para chegar até ele e armazenando o combustível de cada posto em uma heap máxima. Quando o combustível não é suficiente para avançar, o carro reabastece usando o maior combustível disponível da heap, aumentando a autonomia e o número de paradas. Esse processo se repete até o carro chegar ao destino ou se tornar impossível continuar, retornando o mínimo de paradas necessárias para completar o percurso.

![Print da Resolução 871](/assets/871.png)


### [2406](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/) - Média:

O problema pede para dividir uma lista de intervalos em grupos, de forma que dentro de cada grupo nenhum intervalo se sobreponha e que o número total de grupos seja o menor possível. Para resolver, utilizei o algoritmo de Interval Partitioning, que começa ordenando os intervalos pelo início e usa uma heap mínima para gerenciar os intervalos ativos. Percorri cada intervalo na ordem de início e, sempre que possível, removi da heap o intervalo que já terminou antes de começar o atual, pois eles não se sobrepõem. Em seguida, adicionei o final do intervalo atual à heap para indicar que agora faz parte de um grupo em andamento. O tamanho final da heap representa o número mínimo de grupos necessários para acomodar todos os intervalos sem sobreposição.

![Print da Resolução 871](/assets/2406.png)


## Instalação 
**Linguagem**: Python<br>




