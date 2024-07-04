# Geometric Shapes

## Estrutura de Diretórios

Abaixo está a estrutura de diretórios do projeto.

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

## Uso do Repositório

### Clonar o Repositório

Primeiro, você precisa clonar o repositório do GitHub para o seu ambiente local:

```bash
git clone https://github.com/samuelncaetano/geometric_shapes.git
cd geometric_shapes
```

### Configurar Ambiente Virtual

Para evitar conflitos de dependências e garantir que todas as bibliotecas necessárias estejam instaladas corretamente, vamos configurar um ambiente virtual:

1. Instalar o virtualenv se ainda não estiver instalado:

```bash
pip3 install virtualenv
```

2. Criar um novo ambiente virtual:

```bash
virtualenv -p python3 venv
```

3. Ativar o ambiente virtual:

```bash
source venv/bin/activate
```

### Instalar Dependências

Com o ambiente virtual ativado, instale todas as dependências necessárias para o projeto:

```bash
venv/bin/pip3 install -r requirements.txt
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
python src/main.py
```

## Executar Testes

### Executar Todos os Testes

Para executar todos os testes, use o comando:

```bash
pytest
```

#### Executar Testes Detalhados

Se você deseja executar os testes de maneira mais detalhada, use o comando:

```bash
pytest src/tests/diretório/nome_do_teste -v
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
