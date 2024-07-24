# Automação de tarefas com PyAutoGUI e OpenCV

O projeto foi desenvolvido para automatizar tarefas de forma geral, utilizando as bibliotecas `pyautogui` e `OpenCV`. Embora o exemplo fornecido se concentre na automação de interações com o navegador, a abordagem é flexível e pode ser adaptada para uma variedade de tarefas automatizadas, tanto dentro quanto fora do navegador.

## Ferramentas utilizadas

- **`pyautogui`**: Biblioteca que permite simular entradas de teclado e mouse, facilitando a automação de ações no computador.
- **`OpenCV`**: Biblioteca para processamento de imagens e reconhecimento de padrões. Utilizada para capturar e analisar imagens da tela.
- **`mss`**: Biblioteca para captura de tela eficiente. Usada para obter imagens da tela do computador.
- **`numpy`**: Biblioteca fundamental para a manipulação de arrays e matrizes. Utilizada para converter a imagem capturada em uma matriz que pode ser processada pelo OpenCV e facilitar operações aritméticas e de transformação na análise de imagens.

## Como a automação é feita

A automação é realizada através de um conjunto de funções que interagem com a interface do usuário. O processo inclui as seguintes etapas:

1. **Captura de tela**
   - **Função utilizada:** `capturar_tela()`
   - **Descrição:** Captura a tela do computador e converte a imagem para escala de cinza usando `mss` e `OpenCV`. Isso facilita a análise e o reconhecimento dos elementos da interface.

2. **Carregamento do template**
   - **Função utilizada:** `carregar_template(template_path)`
   - **Descrição:** Carrega imagens de templates que representam os elementos da interface com os quais você deseja interagir. As imagens são carregadas em escala de cinza para facilitar a comparação.

3. **Localização do template**
   - **Função utilizada:** `encontrar_template(gray_screenshot, template)`
   - **Descrição:** Compara a captura de tela com o template fornecido e encontra a localização do elemento desejado usando o método de correspondência de templates do `OpenCV`.

4. **Interação com o elemento**
   - **Função utilizada:** `clicar(top_left, largura, altura)`
   - **Descrição:** Calcula o centro do elemento localizado e realiza um clique nesse ponto usando `pyautogui`. Isso permite interagir com botões, campos de texto e outros elementos clicáveis da interface.

5. **Automação de tarefas**
   - **Comandos utilizados:** `pyautogui.hotkey()`, `pyautogui.write()`, `pyautogui.press()`
   - **Descrição:** Executa comandos para realizar tarefas específicas, como abrir novas abas, navegar para URLs e preencher campos de pesquisa.

## Flexibilidade da automação

O sistema de automação desenvolvido é altamente flexível e pode ser adaptado para uma ampla gama de tarefas. Aqui está como você pode personalizar o fluxo de automação para atender às suas necessidades específicas:

1. **Adicionar novos elementos**
   - Crie imagens dos elementos da interface que deseja automatizar e salve-as no diretório de templates. Atualize o código para carregar e utilizar essas novas imagens com a função `carregar_template()`.

2. **Modificar fluxos de trabalho**
   - Adapte o código para diferentes fluxos de trabalho alterando os templates e as ações realizadas. Você pode ajustar o código para realizar tarefas variadas, seja dentro do navegador ou em outras aplicações.

3. **Ajustar tempos de espera**
   - Utilize a função `sleep()` para ajustar os tempos de espera entre as ações, garantindo que a interface do usuário tenha tempo suficiente para responder às ações automatizadas.

4. **Personalização adicional**
   - Com as funções fornecidas, você pode criar fluxos complexos e personalizados. Modifique o código conforme necessário para refletir suas interações específicas e os elementos da interface com os quais deseja interagir.

## Conclusão

Este sistema de automação oferece uma base sólida para criar fluxos personalizados e automatizar uma ampla gama de tarefas. Com a flexibilidade das funções fornecidas e as ferramentas utilizadas, você pode adaptar o código para atender a diversas necessidades e otimizar suas tarefas automatizadas.
