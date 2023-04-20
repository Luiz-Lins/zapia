# Zapia
Bot para Whatsapp com python pra fazer vendas e atendimento
[![Languages](https://img.shields.io/github/languages/count/GermanUngo/Curso_Django_2.0)]()
[![Repo Size](https://img.shields.io/github/repo-size/GermanUngo/Curso_Django_2.0)]()


Abordado a construção de projetos utilizando o Framework [Django](https://www.djangoproject.com/) para python no back-end e front-end.

## Requerimentos:
- Ter a versão 3.11.3 do python instalada no notebook ou pc.
- Ter o [pipenv](https://pipenv.pypa.io/en/latest/) instalado.

```python {data-filename="requirements.txt"}
pip install pipenv
```

Criar o ambiente virtual na pasta do projeto e instalar os requirements:
- Criar o .venv, instalar as dependências e ativar o shell do ambiente virtual:

```python {data-filename="requirements.txt"}
pipenv sync
pipenv shell
```

- Instalar somente as dependências de desenvolvimento:

```python {data-filename="requirements.txt"}
pipenv sync -d
```

## Verificar qualidade de código:
- [flake8](https://flake8.pycqa.org/en/latest/)

## Ferramentas utilizadas:
- Ambiente virtual:
  - [Pipenv](https://pipenv.pypa.io/en/latest/)
- Frameworks:
  - [Django](https://www.djangoproject.com/)
  - [Bootstrap](https://getbootstrap.com/)
- Deploy:
  - [Git](https://git-scm.com/)
  - [Fly.io](https://fly.io)
  - [AWS](https://aws.amazon.com/)
  - [django-s3-folder-storage](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#module-django_storages.backends.s3boto3)
  - [Collectfast](https://github.com/antonagestam/collectfast)
- Testes e qualidade do código:
  - [PyTest](https://pytest.org/)
  - [PyTest-Cov](https://pytest-cov.readthedocs.io/en/latest/)
  - [Pytest-Mock](https://pypi.org/project/pytest-mock/)
  - [Pytest-Django](https://pytest-django.readthedocs.io/en/latest/)
  - [Django-Debug-Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
- Gestão da atualização de dependências:
  - [PyUp](https://pyup.io/)
- Monitoramento de erros:
  - [Sentry](https://sentry.io/welcome/)
- Envio de emails:
  - [Mailchimp](https://mailchimp.com/)

## Licença

Este projeto é licenciado sobre a licença MIT veja [LICENSE](LICENSE) para mais informações.

## Acknowledgments


