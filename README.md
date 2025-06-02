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
| [630. Course Schedule III](https://leetcode.com/problems/course-schedule-iii/description/)  | Dificil|
| [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/description/)  | Médio|
## Screenshots

### [871](https://leetcode.com/problems/minimum-number-of-refueling-stops/description/) - Difícil:

O problema pede o número mínimo de paradas para um carro chegar ao destino, podendo reabastecer completamente em cada posto de combustível encontrado ao longo do caminho. Para resolver, utilizei o algoritmo ganancioso conhecido como “algoritmo do caminhoneiro”, onde sempre que o carro precisa reabastecer, ele escolhe o posto que oferece a maior quantidade combustível disponível entre todos os que já passou. Comecei adicionando o destino como um último posto com zero combustível e percorri cada posto, subtraindo o combustível necessário para chegar até ele e armazenando o combustível de cada posto em uma heap máxima. Quando o combustível não é suficiente para avançar, o carro reabastece usando o maior combustível disponível da heap, aumentando a autonomia e o número de paradas. Esse processo se repete até o carro chegar ao destino ou se tornar impossível continuar, retornando o mínimo de paradas necessárias para completar o percurso.

![Print da Resolução 871](/assets/871.png)


### [2406](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/) - Média:

O problema pede para dividir uma lista de intervalos em grupos, de forma que dentro de cada grupo nenhum intervalo se sobreponha e que o número total de grupos seja o menor possível. Para resolver, utilizei o algoritmo de Interval Partitioning, que começa ordenando os intervalos pelo início e usa uma heap mínima para gerenciar os intervalos ativos. Percorri cada intervalo na ordem de início e, sempre que possível, removi da heap o intervalo que já terminou antes de começar o atual, pois eles não se sobrepõem. Em seguida, adicionei o final do intervalo atual à heap para indicar que agora faz parte de um grupo em andamento. O tamanho final da heap representa o número mínimo de grupos necessários para acomodar todos os intervalos sem sobreposição.

![Print da Resolução 871](/assets/2406.png)

### [630. Course Schedule III](https://leetcode.com/problems/course-schedule-iii/description/) - Difícil:

Dado um conjunto de cursos, cada um com uma duração e um prazo final (lastDay), o objetivo é determinar quantos cursos no máximo é possível fazer. Você começa no dia 1 e não pode fazer dois cursos ao mesmo tempo.
A tarefa é escolher uma sequência de cursos (possivelmente reorganizando a ordem original) para maximizar o número de cursos completados sem ultrapassar os prazos de nenhum. Na solução que encontrei utilizei uma abordagem gananciosa com heap (fila de prioridade). Dessa forma, ordenei os cursos por lastDay(prazo mais próximo), percorri os cursos na ordem ordenada, verifiquei se o tempo total ultrapassou o prazo e por fim o resultado é a quantidade de cursos que foram mantidos no cronograma.

![Print da Resolução 630](/assets/630.jpg)

### [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/description/) - Média:

O problema pede para você encontrar o menor número de saltos necessários para ir do início de um array (índice 0) até o final do array (índice n-1). Em vez de tentar todas as possibilidade, o algoritmo sempre escolhe o melhor alcance no momento atual, confiando que essa escolha levará ao mínimo de pulos no final.

![Print da Resolução 45](/assets/45.jpg)

## Video de explicação

https://github.com/user-attachments/assets/22bfec19-d6be-47ab-aaba-2a418677683d




## Instalação 
**Linguagem**: Python<br>




