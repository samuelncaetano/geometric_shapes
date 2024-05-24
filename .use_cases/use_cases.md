# Casos de Uso do Projeto de Formas Geométricas

## 1. Criar Forma Geométrica

### Descrição

O usuário pode criar formas geométricas bidimensionais, como ponto, segmento de reta, círculo, retângulo e triângulo.

### Fluxo Principal

1. O usuário seleciona a opção de criar forma geométrica.
2. O sistema exibe as opções disponíveis de formas geométricas.
3. O usuário escolhe uma forma geométrica para criar.
4. O sistema solicita os parâmetros necessários para criar a forma geométrica (por exemplo, coordenadas para ponto, centro e raio para círculo, etc.).
5. O sistema cria a forma geométrica e a armazena temporariamente na memória.

### Pré-condições

- O sistema está em execução.

### Pós-condições

- A forma geométrica é criada e armazenada temporariamente na memória.

## 2. Listar Formas Geométricas Disponíveis

### Descrição

O usuário pode visualizar uma lista das formas geométricas disponíveis para criação.

### Fluxo Principal

1. Uma lista será retornada a cada forma criada.
<!-- 2. O sistema exibe a lista das formas geométricas disponíveis. -->

### Pré-condições

- O sistema está em execução.

### Pós-condições

- Nenhuma.

## 3. Calcular Área de Forma Geométrica

### Descrição

O usuário pode calcular a área de uma forma geométrica criada.

### Fluxo Principal

1. O usuário seleciona a opção de calcular área de forma geométrica.
2. O sistema exibe a lista das formas geométricas disponíveis.
3. O usuário escolhe uma forma geométrica da lista.
4. O sistema calcula a área da forma geométrica selecionada e a exibe.

### Pré-condições

- Pelo menos uma forma geométrica deve ser criada.

### Pós-condições

- A área da forma geométrica é exibida.

## 4. Verificar Distância Entre Pontos e Origem

### Descrição

O usuário pode definir pontos e verificar a distância entre eles e a origem (0, 0).

### Fluxo Principal

1. O usuário seleciona a opção de verificar distância entre pontos e origem.
2. O sistema solicita as coordenadas dos pontos.
3. O usuário fornece as coordenadas dos pontos.
4. O sistema calcula a distância entre os pontos fornecidos e a origem (0, 0).
5. O sistema exibe a distância calculada.

### Pré-condições

- Pelo menos um ponto deve ser definido.

### Pós-condições

- A distância entre os pontos e a origem é exibida.

## 5. Verificar Relação entre Ponto e Forma Geométrica

### Descrição

O usuário pode verificar se um ponto está dentro do domínio de uma forma geométrica específica.

### Fluxo Principal

1. O usuário seleciona a opção de verificar relação entre ponto e forma geométrica.
2. O sistema solicita as coordenadas do ponto e a forma geométrica.
3. O usuário fornece as coordenadas do ponto e a forma geométrica.
4. O sistema verifica se o ponto está dentro da forma geométrica.
5. O sistema exibe o resultado da verificação.

### Pré-condições

- Um ponto e uma forma geométrica devem ser definidos.

### Pós-condições

- O sistema indica se o ponto está dentro da forma geométrica.

## 6. Verificar Relação entre Ponto e Reta

### Descrição

O usuário pode verificar se um ponto está próximo de um segmento de reta especificado.

### Fluxo Principal

1. O usuário seleciona a opção de verificar relação entre ponto e reta.
2. O sistema solicita as coordenadas do ponto e do segmento de reta.
3. O usuário fornece as coordenadas do ponto e do segmento de reta.
4. O sistema verifica se o ponto está próximo do segmento de reta.
5. O sistema exibe o resultado da verificação.

### Pré-condições

- Um ponto e um segmento de reta devem ser definidos.

### Pós-condições

- O sistema indica se o ponto está próximo do segmento de reta.
