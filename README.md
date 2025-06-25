# Sistema de Cadastro e Autenticação de Jogadores

Este projeto é uma API RESTful desenvolvida com Flask, SQLAlchemy, JWT e RabbitMQ, voltada para o registro, autenticação e gestão de usuários (jogadores), incluindo permissões de administrador com capacidades especiais.

## 🎨 Design Patterns

Singleton:
Garantimos uma única instância do banco de dados compartilhada por todo o projeto, centralizando o acesso e otimizando recursos.

Builder:
A construção de objetos User é feita de forma flexível e controlada, com métodos como .with_password() e .with_dateofbirth() permitindo composições diferentes conforme a necessidade.

Fachada (Facade):
A TokenService atua como uma interface simplificada para operações com tokens, encapsulando internamente toda a lógica de criptografia JWT.

Decorator:
O decorator @admin_required estende funcionalidades de forma elegante, verificando se a chamada ao endpoint é feita por um administrador, sem modificar a função original.

## 🏛️ Padrão Arquitetural 

O sistema foi desenvolvido em cima do padrão arquitetural **SOA (Service Oriented Architecture)**. Por se tratar de um sistema que se baseia na autenticação de jogadores, as funcionalidades implementadas são feitas para atender outros serviços que vão precisar autenticar e gerenciar jogadores, e esses são registrados e consultados a partir de um banco de dados *(model)*. Ou seja, o principal uso da aplicação se dá por meio de outras aplicações através dos endpoints fornecidos *(controller)*, tornando-se adequado o uso do padrão SOA.

## ⛓️ Princípios Solid

S (Responsabilidade Única): Cada classe possui uma responsabilidade bem definida. O TokenService, por exemplo, é responsável exclusivamente pelo gerenciamento de tokens. Da mesma forma, o UserController atua apenas como orquestrador de requisições, enquanto a lógica de negócio fica no UserService.

O (Aberto/Fechado): O projeto permite extensão sem modificação. Isso é evidente no uso do UserBuilder, que permite adicionar novos campos por meio de métodos como .with_...(), sem alterar o código existente.

L (Substituição de Liskov): O princípio é respeitado. A classe AdministratorController herda de UserController e pode substituí-la sem comprometer o funcionamento do sistema, mantendo compatibilidade de comportamento.

D (Inversão de Dependência): O projeto utiliza abstrações para separar módulos de alto e baixo nível. Um exemplo é o uso do TokenService, que funciona como uma interface para encapsular e abstrair os métodos relacionados à manipulação de tokens, permitindo que outras classes dependam dessa abstração e não de implementações concretas.

## 🚀 Funcionalidades

* Registro de novos jogadores
* Autenticação com JWT
* Atualização e remoção de perfil
* Perfis com diferentes permissões (usuário e administrador)
* Envio de mensagens para o RabbitMQ ao criar novo usuário

## 🧱 Tecnologias Utilizadas

* Python 3
* Flask
* SQLAlchemy
* JWT (JSON Web Token)
* RabbitMQ (via Docker)
* Neon Database (PostgreSQL na nuvem)

## 📂 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/InatelS203-2025-1/SistemaDeJogador.git
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente no arquivo .env que deve ser criado:

```bash
# Chave secreta do Flask para sessões e segurança
SECRET_KEY='sua_chave_secreta_aqui'

# URL de conexão com o banco de dados
DATABASE_URL='postgresql://usuario:senha@host:porta/nome_do_banco'

# Chave secreta usada para assinar os tokens JWT
JWT_SECRET_KEY='sua_jwt_secret_key'

# Algoritmo usado para o JWT (padrão comum: HS256)
JWT_ALGORITHM='HS256'

# URL de conexão com o RabbitMQ
RABBITMQ_URL='amqp://usuario:senha@localhost:5672/'

# Nome da fila usada no RabbitMQ
QUEUE_NAME='notificacao_usuario'
```

4. Execute a aplicação:

```bash
flask run
```

5. Consuma a API em:

```
http://localhost:5000/api/ + <<endpoint>>
```

## 🚧 RabbitMQ com Docker

```bash
docker run -d --hostname rabbitmq-host --name rabbitmq \
  -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

A interface de gerenciamento está disponível em: `http://localhost:15672`
Usuário padrão: `guest`
Senha padrão: `guest`

## 🗓️ Endpoints

### 🔑 Autenticação

#### `POST /register`

Registra um novo jogador

**Body JSON:**

```json
{
  "name": "Jogador Nome",
  "email": "email@example.com",
  "password": "senha123",
  "dateofbirth": "2000-01-01"
}
```

#### `POST /login`

Realiza login e retorna JWT Token

**Body JSON:**

```json
{
  "email": "email@example.com",
  "password": "senha123"
}
```

### 👤 Usuário (Jogador)

#### `PUT /edit`

Atualiza os dados do jogador logado

#### `DELETE /delete`

Remove o jogador logado

#### `GET /details`

Retorna os dados do jogador autenticado

### 💪 Administrador

Rotas exclusivas para usuários com permissão de administrador.

#### `POST /create_user`

Cria um novo jogador

#### `GET /get_all_users`

Retorna todos os jogadores registrados

#### `PUT /edit_user/<user_id>`

Edita os dados de um jogador específico

#### `DELETE /delete_player/<user_id>`

Deleta um jogador específico

### 📉 Permissões

* **Usuário comum** pode:

  * Registrar-se
  * Fazer login
  * Atualizar/remover seu próprio perfil

* **Administrador** pode:

  * Tudo que um usuário pode
  * Gerenciar outros usuários (listar, editar, deletar, criar)

## 📢 RabbitMQ - Mensageria

Ao criar um novo usuário, uma mensagem é enviada para uma fila no RabbitMQ notificando o evento. Isso pode ser usado para:

* Enviar e-mail de boas-vindas
* Atualizar um painel de administração
* Avisar aos outros sistemas do projeto Pokémon


---



