# Casos de Uso - Ferramenta de Formas Geométricas

## UC01 - Criar Ponto

### Descrição

Permitir ao usuário criar um ponto no primeiro quadrante do plano cartesiano.

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.

### Fluxo Principal

1. O usuário seleciona a opção para criar um ponto.
2. O sistema solicita as coordenadas x e y do ponto.
3. O usuário insere as coordenadas.
4. O sistema valida se as coordenadas são não-negativas.
5. O sistema cria o ponto e o armazena.

### Pós-condições

- O ponto é criado e armazenado na memória.

### Fluxo Alternativo

5a. Se as coordenadas forem negativas, o sistema exibe uma mensagem de erro.

---

## UC02 - Criar Segmento de Reta

### Descrição

Permitir ao usuário criar um segmento de reta no primeiro quadrante do plano cartesiano.

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.

### Fluxo Principal

1. O usuário seleciona a opção para criar um segmento de reta.
2. O sistema solicita as coordenadas x e y dos dois pontos que definem o segmento.
3. O usuário insere as coordenadas dos dois pontos.
4. O sistema valida se as coordenadas são não-negativas.
5. O sistema cria o segmento de reta e o armazena.

### Pós-condições

- O segmento de reta é criado e armazenado na memória.

### Fluxo Alternativo

5a. Se as coordenadas forem negativas, o sistema exibe uma mensagem de erro.

---

## UC03 - Criar Círculo

### Descrição

Permitir ao usuário criar um círculo no primeiro quadrante do plano cartesiano.

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.

### Fluxo Principal

1. O usuário seleciona a opção para criar um círculo.
2. O sistema solicita as coordenadas x e y do centro e o raio do círculo.
3. O usuário insere as coordenadas e o raio.
4. O sistema valida se as coordenadas são não-negativas e se o raio é positivo.
5. O sistema cria o círculo e o armazena.

### Pós-condições

- O círculo é criado e armazenado na memória.

### Fluxo Alternativo

5a. Se as coordenadas forem negativas ou o raio for não positivo, o sistema exibe uma mensagem de erro.

---

## UC04 - Criar Retângulo

### Descrição

Permitir ao usuário criar um retângulo no primeiro quadrante do plano cartesiano.

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.

### Fluxo Principal

1. O usuário seleciona a opção para criar um retângulo.
2. O sistema solicita as coordenadas x e y do centro, a largura e a altura do retângulo.
3. O usuário insere as coordenadas, a largura e a altura.
4. O sistema valida se as coordenadas são não-negativas e se a largura e a altura são positivas.
5. O sistema cria o retângulo e o armazena.

### Pós-condições

- O retângulo é criado e armazenado na memória.

### Fluxo Alternativo

5a. Se as coordenadas forem negativas ou a largura ou a altura forem não positivas, o sistema exibe uma mensagem de erro.

---

## UC05 - Criar Triângulo

### Descrição

Permitir ao usuário criar um triângulo no primeiro quadrante do plano cartesiano.

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.

### Fluxo Principal

1. O usuário seleciona a opção para criar um triângulo.
2. O sistema solicita as coordenadas x e y dos três pontos que definem o triângulo.
3. O usuário insere as coordenadas dos três pontos.
4. O sistema valida se as coordenadas são não-negativas e se os pontos formam um triângulo válido.
5. O sistema cria o triângulo e o armazena.

### Pós-condições

- O triângulo é criado e armazenado na memória.

### Fluxo Alternativo

5a. Se as coordenadas forem negativas ou os pontos não formarem um triângulo válido, o sistema exibe uma mensagem de erro.

---

## UC06 - Listar Formas Geométricas

### Descrição

Permitir ao usuário visualizar todas as formas geométricas criadas.

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.

### Fluxo Principal

<!-- 1. O usuário seleciona a opção para listar as formas geométricas. -->

1. O sistema exibe a lista de todas as formas geométricas armazenadas.

### Pós-condições

- As formas geométricas são exibidas na tela.

---

## UC07 - Calcular Área

### Descrição

Permitir ao usuário calcular a área de uma forma geométrica.

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.
- Deve haver pelo menos uma forma geométrica criada.

### Fluxo Principal

1. O usuário seleciona a opção para calcular a área.
2. O sistema solicita o índice da forma geométrica.
3. O usuário insere o índice.
4. O sistema calcula e exibe a área da forma geométrica selecionada.

### Pós-condições

- A área da forma geométrica é exibida na tela.

### Fluxo Alternativo

4a. Se o índice for inválido, o sistema exibe uma mensagem de erro.

---

## UC08 - Calcular Perímetro

### Descrição

Permitir ao usuário calcular o perímetro de uma forma geométrica.

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.
- Deve haver pelo menos uma forma geométrica criada.

### Fluxo Principal

1. O usuário seleciona a opção para calcular o perímetro.
2. O sistema solicita o índice da forma geométrica.
3. O usuário insere o índice.
4. O sistema calcula e exibe o perímetro da forma geométrica selecionada.

### Pós-condições

- O perímetro da forma geométrica é exibido na tela.

### Fluxo Alternativo

4a. Se o índice for inválido, o sistema exibe uma mensagem de erro.

---

## UC09 - Calcular Distância até a Origem

### Descrição

Permitir ao usuário calcular a distância entre uma forma geométrica e a origem (0,0).

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.
- Deve haver pelo menos uma forma geométrica criada.

### Fluxo Principal

1. O usuário seleciona a opção para calcular a distância até a origem.
2. O sistema solicita o índice da forma geométrica.
3. O usuário insere o índice.
4. O sistema calcula e exibe a distância entre a forma geométrica e a origem.

### Pós-condições

- A distância entre a forma geométrica e a origem é exibida na tela.

### Fluxo Alternativo

4a. Se o índice for inválido, o sistema exibe uma mensagem de erro.

---

## UC10 - Calcular Distância entre Formas Geométricas

### Descrição

Permitir ao usuário calcular a distância entre uma forma geométrica e um ponto.

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.
- Deve haver pelo menos uma forma geométrica criada.

### Fluxo Principal

1. O usuário seleciona a opção para calcular a distância entre formas geométricas.
2. O sistema solicita o índice da forma geométrica.
3. O usuário insere o índice.
4. O sistema solicita as coordenadas x e y do ponto.
5. O usuário insere as coordenadas.
6. O sistema calcula e exibe a distância entre a forma geométrica e o ponto.

### Pós-condições

- A distância entre a forma geométrica e o ponto é exibida na tela.

### Fluxo Alternativo

6a. Se as coordenadas forem negativas, o sistema exibe uma mensagem de erro.

---

## UC11 - Verificar Contenção de Ponto

### Descrição

Permitir ao usuário verificar se um ponto está contido em uma forma geométrica.

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.
- Deve haver pelo menos uma forma geométrica criada.

### Fluxo Principal

1. O usuário seleciona a opção para verificar a contenção de um ponto.
2. O sistema solicita o índice da forma geométrica.
3. O usuário insere o índice.
4. O sistema solicita as coordenadas x e y do ponto.
5. O usuário insere as coordenadas.
6. O sistema verifica e exibe se o ponto está contido na forma geométrica.

### Pós-condições

- O resultado da verificação é exibido na tela.

### Fluxo Alternativo

6a. Se as coordenadas forem negativas, o sistema exibe uma mensagem de erro.

---

## UC12 - Mover Forma Geométrica

### Descrição

Permitir ao usuário mover uma forma geométrica para uma nova posição.

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.
- Deve haver pelo menos uma forma geométrica criada.

### Fluxo Principal

1. O usuário seleciona a opção para mover uma forma geométrica.
2. O sistema solicita o índice da forma geométrica.
3. O usuário insere o índice.
4. O sistema solicita as coordenadas x e y do novo ponto.
5. O usuário insere as coordenadas.
6. O sistema move a forma geométrica para a nova posição.

### Pós-condições

- A forma geométrica é movida para a nova posição.

### Fluxo Alternativo

6a. Se as coordenadas forem negativas, o sistema exibe uma mensagem de erro.

---

## UC13 - Encerrar Programa

### Descrição

Permitir ao usuário encerrar a execução do programa.

### Ator

Usuário

### Pré-condições

- O sistema deve estar em execução.

### Fluxo Principal

1. O usuário seleciona a opção para encerrar o programa.
2. O sistema encerra a execução.
<!-- 2. O sistema exibe uma mensagem de confirmação.
3. O usuário confirma a intenção de encerrar. -->

### Pós-condições

- O sistema é encerrado.
