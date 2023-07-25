# Pouorochinho
Pou, mas com o Orochinho.

![pouimg](https://github.com/athoskenew/pouorochinho/assets/33551922/db23e86b-99b1-448a-9532-30f9c523ce6b)

Você pode baixar e utilizar o App gratuitamente sem necessidade de instalação de pacotes adicionais, acessando a área [Releases](https://github.com/athoskenew/pouorochinho/releases) e baixando o arquivo 'Pouorochi.zip', um executável chamado 'Pouorochi.exe' está na pasta extraída, execute-o e tudo estará pronto!

# O que há no Pouorochi?

Você pode:


- Alimentar seu pou com algumas comidas pré-definidas: Cherry, Banana podre.
- Curar o Pou da calvície, durante o jogo seu Pouorochinho ficará calvo de 2 a 3 vezes.
- Comprar potions mágicos que alteram algo ao serem consumidos. clicando em "Shop" você acessa a loja onde compra os potions. Existem 5 potions, como o Potion da Calvície que cura a sua calvície, Potion da mitada, que faz seu Pou falar uma das 35 mitadas disponíveis, Potion da surpresa, que lhe dá de -100 a 200 moedas e o Potion da preguiça, que até o momento não faz nada.
- Jogar mini-jogos como o CLT Run, todos os jogos dão moedas para você comprar itens no Shop.

**__Shop:__** <br>
Contém itens que podem ser comprados para incrementar o seu Pou, no momento, apenas poções estão disponíveis.

**__Geladeira:__** <br>
Todos os itens comprados vão para a geladeira, ao clicar em um item na geladeira, ele desaparecerá de lá e irá para o final da lista de consumíveis, podendo ser encontrado clicando nas setas para esquerda e direita no centro inferior da tela.

**__Jogos e dinheiro:__** <br>
O Pouorochinho conta com 2 mini-jogos embutidos como o CLT Run. Ambos os jogos podem ser encontrados ao clicar na moeda brilhante no canto superior esquerdo da tela, um menu com os dois jogos aparecerá para que o usuário decida qual deseja jogar. <br>


**__ATENÇÃO:__** <br>
Não aperte a tecla 'esc' enquanto estiver na tela inicial do App, isso irá fechar a aplicação. Porém, apertar a tecla 'esc' enquanto estiver em um PopUp (por exemplo, ao clicar na loja) isso irá apenas fechar o PopUp.

# Para desenvolvedores:

O Pouorochinho é escrito em python com sua parte visual totalmente feita em Kivy, o arquivo 'main.py' neste repositório contém o código em python que gerencia as ações e implementações da parte gráfica do app, não há padrões definidos para a escrita do código, sendo assim, várias coisas estão bagunçadas e desorganizadas. <br>

O arquivo 'pourochi.kv' contém código escrito em kvlang que dita todas as telas e estilos visuais dos objetos no app, o código foi pensado para que a aplicação rode em dispositivos de qualquer tamanho de tela, porém, vários itens na tela tem um tamanho definido e não podem ser redimensionados para além disso. <br>

Todos os assets utilizados, como imagens e áudios estão no diretório 'source' e podem ser adicionados com facilidade no código principal. <br> 

É possível adicionar novos itens ao shop criando um ShopItem() e adicionando-o na 'box' da instância da classe Shop(). <br> Também é possível incrementar o level do Pou com ações específicas, o caminho para fazer o incremento do level já está pronto no código, mas sua implementação de mudança de nível não foi implementada.

Sinta-se livre para contribuir ou corrigir este projeto.

# Sobre

Este projeto foi criado puramente para fins de entretenimento, qualquer semelhança com a realidade é uma mera coincidência.

