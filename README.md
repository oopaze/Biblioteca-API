# BIBLIOTECA-API

## Sumário

* [Sobre](https://github.com/oopaze/Biblioteca-API#sobre)
* [Instalação](https://github.com/oopaze/Biblioteca-API#instalação)
* [EndPoints](https://github.com/oopaze/Biblioteca-API#endpoints)
    * [Login](https://github.com/oopaze/Biblioteca-API#login)
    * [Usuarios](https://github.com/oopaze/Biblioteca-API#usuarios)
    * [Autores](https://github.com/oopaze/Biblioteca-API#autores)
    * [Livros](https://github.com/oopaze/Biblioteca-API#livros)
    * [Biblioteca](https://github.com/oopaze/Biblioteca-API#biblioteca)
* [Objetivos](https://github.com/oopaze/Biblioteca-API#objetivos)
* [Atividades](https://github.com/oopaze/Biblioteca-API#atividades)


## Sobre

Esse projeto foi criado e desenvolvimento pelos alunos [José Pedro](https://github.com/oopaze), [Michael Pereira](https://github.com/MichaelPereira31) e [Alan Figueiredo](https://github.com/aemmanuel138) do Instituto Federal do Ceará para ser apresentado na disciplina de Algoritimos e Programação II do professor [Yuri Lacerda](https://github.com/yurilacerda).

O Biblioteca-Fácil é uma API que permitirá auxiliar na gerência de pequenas bibliotecas diminuindo a utilização e preenchimento de protocolos de empréstimos, facilitando a gestão e melhorando a rotina diária com seus usuários. A idéia do  projeto é poder proporcionar aos usuários uma maior interação com o conteúdo disponível na biblioteca através de vários mecanismos de busca. 

Essa API foi construida usando Flask no seu backend, SQLAlchemy na configuração do banco de dados, Marshmallow nas serialização dos models e Flask-JWT para o controle de autenticação. A app conta com dois tipos de autenticação nas rotas, uma para administradores e outra para usuários, onde o administrador tem acesso a tudo. 

Por padrão a Biblioteca-Fácil usa SQLite3 como banco de dados, porém ela pode trabalhar com qualquer tipo de banco de dados relacional adicionando somente às variaveis de ambiente uma variavel chamada DATABASE_URL com uma conexão válida e instalar a biblioteca para conexão com o banco. Ex.: 

* modelo: "tipo_de_db://username:senha@endereço:porta/nome_database"
* exemplo: "postgresql://scott:tiger@localhost:5432/mydatabase"
* linux script: 
    ```bash
    > export DATABASE_URL="postgresql://scott:tiger@localhost:5432/mydatabase"
    > pip3 install psycopg2
    ```
* windows script: 
    ```shell 
    > set DATABASE_URL="postgresql://scott:tiger@localhost:5432/mydatabase"
    > pip3 install psycopg2
    ```


## Instalação

Para rodar essa API é necessário ter no seu computador instalado os seguintes Apps: Git, Python 3.7+ e se for usar um banco diferente do SQLite3, o seu driver para criação do DB.

```shell
    #Baixando projeto
    > git clone https://github.com/oopaze/Biblioteca-API.git

    #Entrando na pasta do projeto
    > cd Biblioteca-API

    #Instalando dependências e criando banco
    Linux:   > source initialize.sh
    Windows: > initialize.bat

    #Rodando API
    > flask run
```
Nesse momento a Biblioteca-API vai tá rodando na url `http://127.0.0.1:5000/` pronta para receber as requisições locais. Para fazer o deploy e colocá-la online, verifique a documentação do provedor desejado.

## EndPoints

### Login

1. `/login` - POST - Gera seu token de autenticação

> Para realizar o login é necessário ser enviado um JSON contendo os campos "username" e "password".

**como por exemplo:**
```py
  {
    "username": "username do usuário",
    "password": "senha do usuário"
  }
```

### Usuarios

Todo usuário é composto é por um ID, um name, um username, um password, um Admin e uma relação OneToOne com emprestimos.

1. `user/` - GET - Mostra todos os usuários (Somente para Administradores)
2. `user/voce/` - GET - Mostra todos os dados do usuario logado (Necessita estar logado)
3. `user/` - POST - Cria um novo usuário

> Para adicionar um usuário é necessário ser enviado um JSON contendo os campos "name","username","password" e "admin".

**como por exemplo:**
```py
  {
    "name": "nome completo do usuário",
    "username": "apelido do usuário",
    "password": "senha do usuário",
    "admin": True or False
  }
```

4. `user/:id/` - GET - Mostra um único usuário (Somente para Administradores)
5. `user/:id/` - PUT - Atualiza um único usuário (Somente para Administradores)

> Para atualizar um usuário é necessário enviar um JSON contendo os campos "name","username","password" e "admin".

**como por exemplo:**
```py
  {
    "name": "nome completo do usuário",
    "username": "apelido do usuário",
    "password": "senha do usuário",
    "admin": True or False
  }
```

6. `user/password/` - PUT - Atualiza senha do usuário logado (Necessita estar logado)

> Para atualizar a senha do usuário logado é necessário enviar um JSON contendo um campo "password".

**como por exemplo:**
```py
  {
    "password": "senha do usuário",
  }
```

7. `user/:id/` - DELETE - Deleta um único usuário (Somente para Administradores)

> Para deletar um usuário é necessário enviar o ID do usuário na URL.

### Autores

Todo autor é composto por um name e um ID, porém o campo ID não é necessário ser enviado. Para atualizar/deletar um autor, é necessário enviar o ID do autor na URL.

1. `autor/` - GET - Mostra todos os autores (Somente para Administradores)
2. `autor/` - POST - Adiciona um novo autor (Somente para Administradores)

> Para adicionar um autor é necessário ser enviado um JSON contendo um campo "name".

**como por exemplo:**
```py
  {
    "name": "nome do autor"
  }
```
3. `autor/:id/` - PUT - Atualizar um autor pelo ID (Somente para Administradores)

> Para atualizar um autor é necessário passar o ID do autor na URL e enviar um JSON contendo o campo "name".

**como por exemplo:**
```py
  {
    "name": "nome do autor"
  }
```
4. `autor/:id/` - DELETE - Deletar um autor pelo ID (Somente para Administradores)

> Para deletar um autor é necessário passar o ID do autor na URL.

### Livros

Todo livro é composto por um ID, um titulo, um volume, um disponivel, um autores, um adicionado em, um atualizado em e uma coluna de relação OneToMany com emprestimos.

1. `livro/` - GET - Mostra todos os livros (Necessita estar logado)
2. `livro/` - POST - Adiciona um livro (Somente para Administradores)

> Para adicionar um livro é necessário ser enviado um JSON contendo os campos "titulo","vol","disponivel" e um campo opcional "autores" que conterá um Array com os ID's dos autores do livro.

**como por exemplo:**
```py
{
  "titulo": "novo",
  "vol": 1,
  "disponivel": true,
  "autores": [
    id do livro
  ]
}
```

3. `livro/varios/` - POST - Adiciona vários livros (Somente para Administradores)

> Para adicionar vários livros é necessário ser enviado um JSON contendo um Array, onde cada objeto desse Array deverá ter os campos "titulo","vol","disponivel" e um campo opcional "autores" que conterá um Array com os ID's dos autores do livro.

**como por exemplo:**
```py
[
  {
    "titulo": "novo",
    "vol": 1,
    "disponivel": true,
    "autores": [
      id do autor
    ]
  },
  {
    "titulo": "novo2",
    "vol": 2,
    "disponivel": true,
    "autores": [
      id do autor,
      id do autor
    ]
  },
  
]
```

4. `livro/:id/` - GET - Mostra somente um livro (Necessita estar logado)
5. `livro/:id/` - PUT - Atualiza um livro (Somente para Administradores)

> Para atualizar um livro é necessário ser enviado um JSON contendo os campos "titulo","vol","disponivel" e um campo opcional "autores" que conterá um Array com os ID's dos autores do livro.

**como por exemplo:**
```py
{
  "titulo": "novo_atualizado",
  "vol": 1,
  "disponivel": true,
  "autores": [
    id do autor,
    id do autor,
  ]
}
```

6. `livro/:id/` - DELETE - Deleta um livro (Somente para Administradores)

> Para deletar um livro é necessário passar o ID do livro na URL.

### Biblioteca

Esta  aplicação engloba as funções principais da biblioteca. É aqui onde são feitos o controle dos livros, dos emprestimos, das devoluções, das disponibilidades e das pendências.

1. `biblioteca/emprestar/` - POST - Realiza o emprestimos dos livros(Somente para Administradores)

> Para adicionar um emprestimo é necessário ser enviado um JSON contendo com um campo opcional "usuario" com o ID do usuário e um campo "livros" com um Array com o ID de cada livro a ser emprestado. Se o campo "usuario" não for enviado o emprestimo sera feito com o usuário logado.

**como por exemplo:**
```py
  {
    "usuario": id do usuario,
    "livros": [
        id do livro,
        id do livro,
        id do livro
    ]
  }
```
2. `biblioteca/devolucao/` - POST - Realiza a devolução do livro(Somente para Administradores)

> Para realizar uma devolução é necessário ser enviado um JSON com o campo "usuario" contendo o ID do usuário.

**como por exemplo:**
```py
  {
    "usuario": id do usuario,
  }
```
3. `biblioteca/pendencias/` - GET - Mostra as devoluções que estão pendentes(Somente para Administradores)
4. `biblioteca/emprestimos/` - GET - Mostra todos os emprestomos (Somente para Administradores)
5. `biblioteca/disponiveis/` - GET - Mostra todos os livros disponiveis (Somente para Administradores)
6. `biblioteca/indisponivel/` - GET - Mostra todos os livros indisponivel(Necessita estar logado)


## Objetivos

Dos objetivos a serem atingidos, segue uma pequena tabela explanatória:

| Objetivos | Estado |
| ------------- |:-------------:|
| Controlar o empréstimos, renovações, reservas e pendências de livros | Concluído |
| Reduzir o tempo de atendimento nas transações | Concluído |
| Controlar o cadastro de usuários, livros e autores | Concluído |


## Atividades

As atividades a serem desenvolvidas foram dispostas da seguinte maneira:
| Atividade | Descrição |
| ------------- |:-------------:|
| 1 | Criação do esqueleto do Projeto e dos arquivos de configuração. |
| 2 | Configurar o banco de dados, a autenticação e os schemas. |
| 3 | Criação dos modelos das Apps: Autor, Livro, Usuário. |
| 4 | Criação dos schemas das Apps: Autor, Livro, Usuário. |
| 5 | Criação das rotas das Apps: Autor, Livro, Usuário. |
| 6 | Criação das rotas e regras de negócio da App: Biblioteca. |


