# Sharding-SD-2022-1

### MongoDB com Sharding

O MongoDB fornece a funcionalidade de sharding, que é um método para distribuir dados entre várias máquinas. Ele utiliza o sharding para dar suporte a implantações com conjuntos grandes de dados e operações de alto rendimento.

### Preparando o ambiente

#### Ferramentas necessárias:

* [Docker](https://www.docker.com/)
* [MongoDB](https://www.mongodb.com/)

#### Servidores de configuração

Inicialmente acesse o diretório "config-server", e execute o seguinte comando:

```bash
sudo docker-compose up -d
```

Em seguida, acesse o mongo na porta 40001 com o seu endereço ipv4, com o seguinte comando:

```bash
mongo mongodb://<seu_endereco_ipv4>:40001
```

Com o acesso no mongo, vamos inicializar o "replica_set" com o seguinte comando (lembre de trocar pelo seu endereço ipv4 também):

```bash
rs.initiate(
  {
    _id: "cfgrs",
    configsvr: true,
    members: [
      { _id : 0, host : "<seu_endereco_ipv4>:40001" },
      { _id : 1, host : "<seu_endereco_ipv4>:40002" },
      { _id : 2, host : "<seu_endereco_ipv4>:40003" }
    ]
  }
)
```

#### Sharding 1

Inicialmente acesse o diretório "shard", e execute o seguinte comando:

```bash
sudo docker-compose up -d
```

Em seguida, acesse o mongo na porta 50001 com o seu endereço ipv4, com o seguinte comando:

```bash
mongo mongodb://<seu_endereco_ipv4>:50001
```

Com o acesso no mongo, vamos inicializar o "replica_set" com o seguinte comando (lembre de trocar pelo seu endereço ipv4 também):

```bash
rs.initiate(
  {
    _id: "shard1rs",
    members: [
      { _id : 0, host : "<seu_endereco_ipv4>:50001" },
      { _id : 1, host : "<seu_endereco_ipv4>:50002" },
      { _id : 2, host : "<seu_endereco_ipv4>:50003" }
    ]
  }
)
```

#### Sharding 2

Inicialmente acesse o diretório "shard2", e execute o seguinte comando:

```bash
sudo docker-compose up -d
```

Em seguida, acesse o mongo na porta 50004 com o seu endereço ipv4, com o seguinte comando:

```bash
mongo mongodb://<seu_endereco_ipv4>:50004
```

Com o acesso no mongo, vamos inicializar o "replica_set" com o seguinte comando (lembre de trocar pelo seu endereço ipv4 também):

```bash
rs.initiate(
  {
    _id: "shard2rs",
    members: [
      { _id : 0, host : "<seu_endereco_ipv4>:50004" },
      { _id : 1, host : "<seu_endereco_ipv4>:50005" },
      { _id : 2, host : "<seu_endereco_ipv4>:50006" }
    ]
  }
)
```

#### Mongos router

Inicialmente acesse o diretório "mongos", e altere o arquivo "docker-compose.yaml", adicionando o seu endereço ipv4 antes das portas:

```bash
version: '3'

services:

  mongos:
    container_name: mongosrouter
    image: mongo
    command: mongos --configdb cfgrs/<seu_endereco_ipv4>:40001,<seu_endereco_ipv4>:40002,<seu_endereco_ipv4>:40003 --bind_ip 0.0.0.0 --port 27017
    ports:
      - 60000:27017
```

E então, execute o seguinte comando:

```bash
sudo docker-compose up -d
```

Em seguida, acesse o mongo na porta 60000 com o seu endereço ipv4, com o seguinte comando:

```bash
mongo mongodb://<seu_endereco_ipv4>:60000
```

Com o acesso no mongo, vamos adicionar os dois shards com os seguintes comandos (lembre de trocar pelo seu endereço ipv4 também):

```bash
sh.addShard("shard1rs/<seu_endereco_ipv4>:50001,<seu_endereco_ipv4>:50002,<seu_endereco_ipv4>:50003")
```

```bash
sh.addShard("shard2rs/<seu_endereco_ipv4>:50004,<seu_endereco_ipv4>:50005,<seu_endereco_ipv4>:50006")
```

### Arquitetura

###  ![image-20220704005029175](images/arquitetura.png)

