# Imagem base
FROM python:3.8.5-alpine

# Descicao do mantenedor
LABEL ENV="Development" \
      MAINTAINER="David Ferreira Gonçalves" \
      EMAIL="davidgoncalves@cvccorp.com.br" \
      SLACK_CHANNEL="devops" \
      DESCRIPTION="Imagem Base para laboratorio"

# Diretorio base
WORKDIR /devops-lab

# Variaveis de Ambiente
ENV VAULT_SERVER None
ENV VAULT_TOKEN None
ENV CONSUL_SERVER None


# Copiando dados para dentro da image
COPY . .

# Instalando dependencias e libs
RUN pip install -r requirements.txt

# Comando principal da imagem
ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8080", "wsgi:flask_app"]