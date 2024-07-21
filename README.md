# Geometric Shapes

## Sumário

1. [Introdução](#introdução)
2. [Uso do Repositório](#uso-do-repositório)
   1. [Clonar o Repositório](#clonar-o-repositório)
   2. [Configurar Ambiente Virtual](#configurar-ambiente-virtual)
   3. [Instalar Dependências](#instalar-dependências)
   4. [Configurar o PYTHONPATH](#configurar-o-pythonpath)
   5. [Executar o Script Principal](#executar-o-script-principal)
   6. [Executar Testes](#executar-testes)
      1. [Executar Todos os Testes](#executar-todos-os-testes)
      2. [Executar Testes Detalhados](#executar-testes-detalhados)
      3. [Verificar Cobertura do Código](#verificar-cobertura-do-código)
      4. [Gerar Relatório HTML](#gerar-relatório-html)
      5. [Visualizar Relatório HTML](#visualizar-relatório-html)
3. [Documentação](#documentação)
4. [Arquitetura](#arquitetura)
   1. [Componentes Principais](#componentes-principais)
   2. [Estrutura de Diretórios](#estrutura-de-diretórios)
5. [Princípios de Projeto](#princípios-de-projeto)
6. [Padrões de Projeto](#padrões-de-projeto)
7. [Detalhes das Implementações](#detalhes-das-implementações)

## Introdução

Este documento descreve o uso de uma ferramenta para criação e manipulação de formas geométricas bidimensionais no plano cartesiano. Além disso, oferece uma visão detalhada da arquitetura da ferramenta, abordando os princípios de design e os padrões de projeto empregados na sua implementação.

## Uso do Repositório

### Clonar o Repositório

Primeiro, você precisa clonar o repositório do GitHub para o seu ambiente local:

```bash
git clone https://github.com/samuelncaetano/geometric_shapes.git
cd geometric_shapes
```

### Configurar Ambiente Virtual

Para evitar conflitos de dependências e garantir que todas as bibliotecas necessárias estejam instaladas corretamente, configure um ambiente virtual:

1. Instalar o virtualenv se ainda não estiver instalado:

```bash
pip3 install virtualenv
```

2. Criar um novo ambiente virtual:

```bash
virtualenv -p python3 .venv
```

3. Ativar o ambiente virtual:

```bash
source .venv/bin/activate
```

### Instalar Dependências

Com o ambiente virtual ativado, instale todas as dependências necessárias para o projeto:

```bash
pip3 install -r requirements.txt
```

### Configurar o PYTHONPATH

Para garantir que o Python encontre todos os módulos do projeto, configure o PYTHONPATH. Execute o script `setup_env.sh`, que configurará o PYTHONPATH temporariamente para a sessão atual do terminal:

```bash
chmod +x setup_env.sh
./setup_env.sh
```

### Executar o Script Principal

Com o ambiente configurado, você pode executar o script principal que inicializa o programa:

```bash
python3 src/main.py
```

## Executar Testes

### Executar Todos os Testes

Para executar todos os testes, use o comando:

```bash
pytest
```

### Executar Testes Detalhados

Se você deseja executar os testes de maneira mais detalhada, use o comando:

```bash
python3 src/tests/nome_do_diretório/nome_do_teste.py
```

### Verificar Cobertura do Código

Para verificar a cobertura do código, siga os comandos abaixo:

1. Execute os testes com o coverage:

```bash
coverage run -m pytest
```

2. Gere um relatório de cobertura:

```bash
coverage report
```

### Gerar Relatório HTML

Para uma visualização mais detalhada da cobertura de código, você pode gerar um relatório HTML:

```bash
coverage html
```

### Visualizar Relatório HTML

Abra o arquivo `index.html` no diretório htmlcov em seu navegador para uma análise detalhada da cobertura de código.

## Documentação

Existem dois diagramas de classe, um relacionado às relações de classes e outro que apresenta os atributos e métodos de cada classe do projeto, e os casos de uso, ambos estão disponíveis na pasta. `doc`

## Arquitetura

O projeto segue os princípios da Arquitetura Hexagonal, também conhecida como Arquitetura de Ports and Adapters, sendo um estilo arquitetural que promove a separação de preocupações, facilitando a manutenção e evolução do sistema ao longo do tempo. Esse estilo visa criar um sistema altamente modular e desacoplado, onde as dependências são invertidas para isolar a lógica de negócios das interações externas, como interfaces de usuário, bancos de dados e serviços externos. Visualmente representada como um hexágono, a arquitetura simboliza a capacidade do sistema de ser interagido por vários lados, cada um representando uma interface ou "porta" de comunicação. Esse isolamento proporciona maior flexibilidade, testabilidade e manutenção do código.

### Componentes Principais

- **Domínio**: Contém as entidades e a lógica de negócios do sistema.
- **Aplicação**: Contém os casos de uso que coordenam a lógica de negócios.
- **Infraestrutura**: Contém a implementação de persistência de dados e outros detalhes técnicos.
- **Adapters**: Contém as interfaces de entrada e saída, como controladores e visualizações.

### Estrutura de Diretórios

Abaixo está a estrutura dos diretórios do projeto.

```bash
src/
├── domain/
│   ├── entities/
│   │   ├── geometric_shape.py        # Define a classe base para todas as formas geométricas
│   │   ├── point.py                  # Define a classe Point para representar um ponto no espaço
│   │   ├── line_segment.py           # Define a classe LineSegment para representar um segmento de linha
│   │   ├── circle.py                 # Define a classe Circle para representar um círculo
│   │   ├── rectangle.py              # Define a classe Rectangle para representar um retângulo
│   │   └── triangle.py               # Define a classe Triangle para representar um triângulo
│   ├── repositories/
│   │   └── irepository.py            # Interface para os repositórios de armazenamento das formas geométricas
├── application/
│   ├── use_cases/
│   │   ├── create_shape.py           # Caso de uso para criar uma nova forma geométrica
│   │   ├── move_shape.py             # Caso de uso para mover uma forma geométrica
│   │   └── calculate_metrics.py      # Caso de uso para calcular métricas (área, perímetro, etc.) das formas geométricas
│   └── factories/
│       └── shape_factory.py          # Fábrica para criar instâncias das formas geométricas
├── infrastructure/
│   └── repositories/
│       └── in_memory_repository.py   # Implementação de um repositório em memória para armazenar as formas geométricas
└── adapters/
    ├── controllers/
    │   └── geometric_shape_controller.py # Controlador para intermediar as interações entre a aplicação e a interface de usuário
    └── views/
        ├── geometric_shape_app.py    # Aplicação principal que inicializa e executa a interface de usuário
        └── geometric_shape_view.py   # Define a interface de usuário para interação com as formas geométricas
```

## Princípios de Projeto

### SOLID

1. **Single Responsibility Principle (SRP)**: Cada classe tem uma única responsabilidade. As classes de entidades cuidam das propriedades e comportamentos das formas geométricas, enquanto as classes de repositório lidam com a persistência dos dados.
2. **Open/Closed Principle (OCP)**: As classes estão abertas para extensão, mas fechadas para modificação. Novas formas geométricas podem ser adicionadas sem alterar o código existente.
3. **Liskov Substitution Principle (LSP)**: As subclasses podem ser usadas no lugar das suas classes base sem causar problemas. Todas as formas geométricas herdam de `GeometricShape` e implementam seus métodos.
4. **Interface Segregation Principle (ISP)**: As interfaces são pequenas e específicas. A interface `IRepository` define apenas os métodos necessários para a persistência.
5. **Dependency Inversion Principle (DIP)**: As classes de alto nível não dependem de classes de baixo nível; ambas dependem de abstrações. O controlador depende da abstração `IRepository`.

### DRY (Don't Repeat Yourself)

O código evita repetições desnecessárias. Funções e métodos reutilizáveis são extraídos e centralizados.

### KISS (Keep It Simple, Stupid)

O projeto mantém a simplicidade, evitando complexidade desnecessária. Cada componente tem um propósito claro e bem definido.

## Padrões de Projeto

### Factory Method

Utilizado para criar instâncias de formas geométricas. A fábrica (`shape_factory.py`) encapsula a lógica de criação de cada forma.

### Repository

O padrão Repository é usado para gerenciar a persistência das formas geométricas. A interface `IRepository` define os métodos necessários, e `InMemoryRepository` implementa a persistência em memória.

### Adapter

Os adaptadores são usados para conectar a lógica de negócios com a interface de usuário. O `GeometricShapeController` atua como um adaptador entre a visualização (`GeometricShapeView`) e os casos de uso (`CreateShape`, `MoveShape`, `CalculateMetrics`).

## Detalhes das Implementações

### Entidades

Cada forma geométrica é representada por uma classe que herda de `GeometricShape` e implementa métodos específicos como `calcular_area`, `calcular_perimetro`, `distancia_origem`, etc.

Métodos `to_dict` e `from_dict` são implementados para conversão para e a partir de dicionários.

### Repositório

`InMemoryRepository` implementa `IRepository` para gerenciar a persistência em memória. Métodos de manipulação de dados (`add`, `list_all`, `get`, `remove`, `update`) são fornecidos.

### Casos de Uso

Os casos de uso são definidos em `create_shape.py`, `move_shape.py` e `calculate_metrics.py`. Eles coordenam a lógica de negócios necessária para criar, mover e calcular métricas das formas geométricas.

### Controlador e Visualização

O `GeometricShapeController` manipula as interações do usuário e chama os casos de uso apropriados. O `GeometricShapeView` fornece a interface de usuário no terminal, exibindo menus e coletando entradas do usuário.
