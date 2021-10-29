# UrlShortener

Esse é um app simples de flask que pega a URL e encurta. 

Para cada URL longa fornecida pelo usuário, o app gera aleatoriamente uma combinação alfabétia que redireciona para a URL original.

# Arquitetura

Post: ler url > guardar url > pegar inicias de cada palavra da url > Salvar no banco url origial + url encurtada
GET: ler url encurtada > pegar original no banco > redirecionar

# Biblioteca e Requisitos
- aniso8601==8.0.0
- click==7.1.2
- Flask==1.1.2
- Flask-RESTful==0.3.8
- Flask-SQLAlchemy==2.4.4
- gunicorn==20.0.4
- itsdangerous==1.1.0
- Jinja2==2.11.2
- MarkupSafe==1.1.1
- pytz==2020.1
- six==1.15.0
- SQLAlchemy==1.3.19
- Werkzeug==1.0.1
- psycopg2
