# Sistema de cadastro e autenticação de jogadores

O código desenvolvido neste projeto contempla atividades de registro de jogadores e a autenticação dos usuários na plataforma.

## Funcionalidades

- Registro de novos jogadores
- Autenticação de jogadores existentes
- Atualização de perfil

## Tecnologias Utilizadas

- python
- Neon Database
- JWT (JSON Web Token)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/S203-L3/GPTNotFound.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd GPTNOTFOUND
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Inicie o servidor:
    ```
    python ~~
    ```
2. Acesse `http://localhost:3000` no seu navegador.


## Endpoints

Os seguintes endpoints estão disponíveis para interação com o sistema:

- **Criar um usuário**
    - **Endpoint:** `POST /api/v1/User`
    - **Descrição:** Cria um novo usuário.
    - **Parâmetros:**
        ```json
        {
            "name": "Nome do usuário",
            "email": "email@example.com",
            "password": "senha123"
        }
        ```

- **Listar todos os usuários**
    - **Endpoint:** `GET /api/v1/User`
    - **Descrição:** Retorna os dados de todos os usuários.

- **Editar um usuário específico**
    - **Endpoint:** `PUT /api/v1/User/{Id}`
    - **Descrição:** Edita os dados de um usuário específico.
    - **Parâmetros:** Campos flexíveis, podendo alterar qualquer um dos dados do usuário.

- **Obter dados de um usuário específico**
    - **Endpoint:** `GET /api/v1/User/{Id}`
    - **Descrição:** Retorna os dados de um usuário específico.

### Exemplo de Requisição para Criação de Usuário

Para criar um usuário, envie uma requisição `POST` com o seguinte corpo em formato JSON:

```json
{
    "name": "Nome do usuário",
    "email": "email@example.com",
    "password": "senha123"
}
```




