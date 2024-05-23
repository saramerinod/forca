Relatório sobre o Código 
Alunos: Sara merino e José merino
Curso: Análise e desenvolvimento de sistemas 

1. A Importação de Módulos:
O código emprega módulos pathlib's_PATH para alterar caminhos de arquivos e gerar palavras aleatórias com uma distribuição específica.

2. Selecione uma palavra pela sua definição.
Abre o arquivo word.txt no modo de leitura.
- Leia todas as falas e escolha uma palavra aleatória para brincar.

3. Função start_game
Inicializa variáveis ​​como palavra, letras do usuário, chances, pontuação e ganho.
- Solicite o nome do jogador e atualize a pontuação no arquivo rank.txt.

4. Lógica do Jogo
Loop principal que imprime a palavra com as letras descobertas e sublinhado para as letras não descobertas.
- O usuário é solicitado a adivinhar uma letra, o que aumenta a probabilidade e verifica se a letra está na palavra.
- Avalia se o usuário ganhou ou perdeu o jogo.

5. O Sistema de Classificação:
Após a disputa, se o jogador vencer, a pontuação aumenta.
- Renova o arquivo rank.txt com a nova classificação do jogador ou adiciona uma nova entrada caso o jogador não estivesse na listagem.

6. A função que exibe os créditos é chamada show_credits.
- imprime os créditos do jogo, informando que ele foi criado por [ Merino].

7. * Função do menu:
- Mostra um menu com três opções: iniciar o jogo, ver os créditos e sair.
- Facilita a escolha do usuário e aciona o procedimento adequado ou conclui o programa.

8. Estrutura principal:
O código contém um bloco condicional if _name_ == "_main_": este bloco chama a função de menu, que inicia a execução do programa.

9. Manuseio de Arquivos:
- Lê e grava em arquivos word.txt, que são usados ​​para as palavras do jogo e no arquivo rank.txt mantido pelo jogador.
- Emprega métodos de leitura e escrita, como readlines,writelines e seek, para manipular o conteúdo dos arquivos.

10. Interação do usuário:
A interface do jogo interage com o usuário solicitando entrada por meio de entrada e exibindo mensagens na tela.
- Inclui instruções e feedback durante o jogo, bem como uma escolha no menu principal.

11. Gestão de tentativas
O jogador tem inicialmente 5 oportunidades. Cada tentativa malsucedida diminui o número de oportunidades restantes.
- O jogo termina se o jogador adivinhar corretamente a palavra inteira ou se as oportunidades se esgotarem.

12. Exame de letras:
A função que inicia o jogo inclui uma lógica que verifica se uma letra já foi adivinhada pelo jogador.
A palavra é demonstrada com as letras reveladas e o espaço em branco representado por sublinhados.

13. Persistência de dados:
O arquivo rank.txt é utilizado para manter as classificações dos jogadores, acompanhando os dados de consistência de pontuação entre as diferentes instâncias do programa.
- A lógica de atualização das classificações garante que os dados sejam lidos, alterados e gravados corretamente no arquivo.

14. Manipulação de arquivos sem itens:
O código contém procedimentos para lidar com arquivos vazios, como verificar o conteúdo do rank.txt na adição de uma nova pontuação.
- Isso evita erros de leitura e escrita e garante que o jogo funcionará corretamente mesmo na primeira execução.

15. estrutura modular:
O código é organizado em funções distintas que cada uma assume responsabilidade (choose_word, start_game, show_credits, menu).
Essa modularidade ajuda a facilitar a manutenção e expansão do código, ao mesmo tempo que permite adicionar novas funções sem a necessidade de grandes alterações no código existente.
