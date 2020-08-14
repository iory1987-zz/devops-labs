# Vault and Consul Labs

## Dependencias para o projeto.


- [Vagrant](https://www.vagrantup.com/downloads)

- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Comandos para subir o ambiente

#### Iniciando VM Linux
```
vagrant up
```

#### Logando no Linux
```
vagrant ssh
```

#### Entrando no diretorio do lab
```
cd /vagrant
```

#### Iniciar Serviços
```
docker-compose up -d
```

#### Listando Serviços
```
docker-compose ps
```

#### Exportando Variaveis de Ambiente
```
export VAULT_SERVER='x.x.x.x'
export VAULT_TOKEN='s.x3cBNKobC84wB82nvu09dIMI'
export CONSUL_SERVER='x.x.x.x'
```

#### Rodando a App de Exemplo
```
cd appV1

gunicorn --bind 0.0.0.0:8080 wsgi:flask_app
```

#### Parando Serviços
```
docker-compose down -v
```

#### Parando VM Linux
```
vagrant destroy -f
```

#

## Iniciando o Vault

### Vault Master Token
* Initial Root Token: s.x3cBNKobC84wB82nvu09dIMI

### Vault Unseal Tokens
* Unseal Key 1: w5ZCsKebxykgdzQS6paCeJGRyjWoRJCO+7fmQz92e/q7
* Unseal Key 2: rTAkLlI1Kpj+jRl1/P/tzciol8sP+5rmNrvJX780TPrl
* Unseal Key 3: bfYVirGrStsLN+pDyO1deXA2AE/MW7Qhla8yLzi3niXo
* Unseal Key 4: +VDmSbpDBMmxe8qGmiFEulw53h4zmoEwPiPPZQRf2g1y
* Unseal Key 5: VzCxc6xziTuaOxTXuFqbu72eFGRXhaWfUDsbCQOeP9Ih