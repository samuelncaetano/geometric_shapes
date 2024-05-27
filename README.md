# Geometric Shapes

## Diretórios

``` bash
src/
├── domain/
│   ├── entities/
│   │   ├── geometric_shape.py
│   │   ├── point.py
│   │   ├── line_segment.py
│   │   ├── circle.py
│   │   ├── rectangle.py
│   │   └── triangle.py
│   ├── repositories/
│   │   └── irepository.py
│   └── services/
│       └── geometric_shape_service.py
├── application/
│   ├── use_cases/
│   │   ├── create_shape.py
│   │   ├── move_shape.py
│   │   └── calculate_metrics.py
│   └── factories/
│       └── shape_factory.py
├── infrastructure/
│   └── repositories/
│       └── in_memory_repository.py
└── adapters/
    ├── controllers/
    │   └── geometric_shape_controller.py
    └── views/
        ├── geometric_shape_app.py
        └── geometric_shape_view.py
```

## Como usar este repositório

### Baixar o repositório

```bash
git clone https://github.com/samuelncaetano/geometric_shapes.git
cd geometric_shapes
```

### Baixar o ambiente virtual

```bash
pip3 install virtualenv
```

### Inicializar o ambiente virtual

```bash
virtualenv -p python3 venv
```

### Ativar o ambiente virtual

```bash
source venv/bin/activate
```

### Baixar todos os pacotes necessários

```bash
venv/bin/pip3 install -r requirements.txt
```

## Como executar os testes

Para executar os testes, basta navegar até o diretório raiz do projeto e executar o pytest:

```bash
pytest
```

Isso executará todos os testes no diretório de testes padrão. Se você quiser executar testes específicos ou de um determinado arquivo, pode passar o caminho para o arquivo como um argumento para o pytest.

Para executar os testes de forma mais detalhada, basta navegar até o diretório raiz do projeto e executar o pytest com a opção -v:

```bash
pytest -v
```

### Verificar Cobertura de Código

Além de executar os testes, é útil verificar a cobertura de código para garantir que todos os aspectos do código estejam sendo testados adequadamente. Certifique-se de ter executado os testes primeiro para que o coverage possa analisar os resultados dos testes.

```bash
coverage run -m pytest
```

Depois de executar o coverage, você pode gerar um relatório de cobertura para visualizar a porcentagem de código testada e identificar áreas que precisam de mais testes.

```bash
coverage report
```

Isso exibirá um relatório detalhado mostrando a cobertura de cada arquivo do projeto. Além de verificar a cobertura de código através do relatório textual, você também pode gerar um relatório HTML mais detalhado para uma análise mais aprofundada.

### Gerar Relatório HTML

```bash
coverage html
```

Isso criará um diretório chamado `htmlcov` contendo arquivos HTML que representam a cobertura de código do seu projeto.

### Visualizar Relatório HTML

Você pode visualizar o relatório HTML abrindo o arquivo `index.html` no diretório `htmlcov` em seu navegador da web. Isso fornecerá uma visualização mais detalhada da cobertura de código, incluindo métricas específicas e uma representação gráfica da cobertura por arquivo. Com o relatório HTML, você pode identificar áreas específicas do código que precisam de mais testes e tomar medidas para melhorar a cobertura de código do seu projeto.

## Aviso

Novas atualizações do código estarão disponíveis na branch `arch`.
