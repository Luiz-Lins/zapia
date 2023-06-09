# Zapia

Bot para Whatsapp com Python para vendas e atendimento.

[![Languages](https://img.shields.io/github/languages/count/GermanUngo/Curso_Django_2.0)]()
[![Repo Size](https://img.shields.io/github/repo-size/GermanUngo/Curso_Django_2.0)]()

Este projeto utiliza a API do OpenAI e a tecnologia do ChatGPT3 para comunicação.

## Requisitos

- Versão 3.11.3 do Python instalada no computador ou notebook.
- [pipenv](https://pipenv.pypa.io/en/latest/) instalado.


``` python
pip install pipenv
```
## Instalação

Clone o repositório para o seu computador:
```
git clone https://github.com/GermanUngo/Zapia.git
```

Criar o ambiente virtual na pasta do projeto e instalar os requirements:
- Criar o .venv, instalar as dependências e ativar o shell do ambiente virtual:

```python {data-filename="requirements.txt"}
pipenv sync
pipenv shell
```

- Instalar somente as dependências de desenvolvimento:

```python {data-filename="requirements.txt"}
pip install -r requirements.txt
```
-Criar um ".env" para guardar a key da [API]( https://platform.openai.com/account/api-keys/) fornecida pela Openai com o seguinte código:

```
OPENAI_ACCESS_KEY_ID='key da openai'
```

- Instalar O Auto-Py-to-Exe 
Para instalar o Auto-Py-to-Exe, é necessário ter o Python instalado em sua máquina. 
Depois, abra o terminal do seu sistema operacional e digite o seguinte comando:


```
pip install auto-py-to-exe
```

## Ferramentas utilizadas:


- Ambiente virtual:
  - [Pipenv](https://pipenv.pypa.io/en/latest/)
- API:
  - [Editacodigo](https://editacodigo.com.br)
  - [Openai](https://openai.com/blog/openai-api/)
- Frameworks:
  - [Django](https://www.djangoproject.com/) -------->Ainda em desenvolvimento
- Deploy:
  - [Git](https://git-scm.com/)
  - [Fly.io](https://fly.io) -------->Ainda em desenvolvimento
  - [AWS](https://aws.amazon.com/) -------->Ainda em desenvolvimento
  - [django-s3-folder-storage](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#module-django_storages.backends.s3boto3) -------->Ainda em desenvolvimento
  - [Collectfast](https://github.com/antonagestam/collectfast) -------->Ainda em desenvolvimento
- Testes e qualidade do código:
  - [flake8](https://flake8.pycqa.org/en/latest/)
  - [PyTest](https://pytest.org/) -------->Ainda em desenvolvimento
  - [PyTest-Cov](https://pytest-cov.readthedocs.io/en/latest/) -------->Ainda em desenvolvimento
  - [Pytest-Mock](https://pypi.org/project/pytest-mock/) -------->Ainda em desenvolvimento
  - [Pytest-Django](https://pytest-django.readthedocs.io/en/latest/) -------->Ainda em desenvolvimento
  - [Django-Debug-Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) -------->Ainda em desenvolvimento
- Conversor para executavel
  - [Auto-Py-to-Exe](https://pypi.org/project/auto-py-to-exe/)
- Monitoramento de erros:
  - [Sentry](https://sentry.io/welcome/) -------->Ainda em desenvolvimento


## Licença

Este projeto é licenciado sobre a licença  AGPL-3.0 veja [LICENSE](https://github.com/GermanUngo/Zapia/blob/main/LICENSE/) para mais informações.



# zapia1
