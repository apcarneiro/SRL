# SRL
Somatic Reinforcement Learning Experiences


Construiu-se três Agentes Q-learning com o objetivo de solucionar o jogo FrozenLake da biblioteca Gymnasium, utilizando os mesmos parâmetros. Os agentes são treinados usando a estratégia de exploração epsilon-greedy com decaimento. Os parâmetros utilizados são:

	*	Taxa de aprendizagem: 0,7
	*	Gamma: 0,95
	*	Número máximo de passos para conclusão: 200


No treinamento temos os parâmetros:
	*	Épsilon máximo: 1
	*	Épsilon mínimo: 0,05
	*	Decaimento: 0,0005
	*	Quantidade de episódios: 1000000


Para validação são utilizados:
    *	Quantidade de episódios: 100
	*	Número máximo de passos para conclusão: 200

Utilizou-se o FrozenLake-v1 com espaço de estados 4x4 e sempre o mesmo mapa:

Então, temos 16 estados possíveis (representados por um número inteiro de 0 a 15), com quatro ações possíveis:
	*	0 – esquerda
	*	1 – baixo
	*	2 - direta
	*	3 - cima

O episódio sempre começa do canto superior esquerdo (estado 0).

## Agente 1

O primeiro é um agente Q-learning clássico e utiliza os parâmetros de recompensa padrão do jogo FrozenLake da biblioteca:
	*	1 – para objetivo
	*	0 – para gelo
	*	0 – para buraco

## Agente 2

Esse também é um agente Q-learning clássico, porém, efetuamos ajustes nas recompensas de maneira a distinguir a queda no buraco (condição máxima de “perda”). Desta forma temos as recompensas:
	*	1 – para objetivo
	*	0 – para gelo
	*	-1 – para buraco

## Agente 3

Esse agente, além dos algoritmos clássicos do Q-learning, possui um conjunto de algoritmos que implementam o mecanismo de marcador somático proposto por Damásio (Q-Learning somático). Desta forma, durante o treinamento, além da “montagem” da tabela Q, os dados do estado original, ação tomada e a recompensa observada são enviados ao mecanismo de marcador somático, que os registra na memória somática caso ultrapassem os limites superior e inferior (nesse caso, configurados para inferior = -0,7 e superior = 0,7). Na tomada de decisão de qual ação tomar para dado estado, o agente consulta, além da tabela Q, a memória somática para o mesmo estado. Se existir uma ação marcada no marcador somático para o estado, o valor existente no marcador é considerado para a análise em detrimento do valor constante da tabela Q para a mesma ação.

Também efetuou-se ajustes nas recompensas (como no Agente 2):
	*	1 – para objetivo
	*	0 – para gelo
	*	-1 – para buraco

