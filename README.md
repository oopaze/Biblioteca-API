# BIBLIOTECA-API

## Sumário

* [Sobre](https://github.com/oopaze/Biblioteca-API#sobre)
* [Instalação](https://github.com/oopaze/Biblioteca-API#instalação)
* [Rotas](https://github.com/oopaze/Biblioteca-API#rotas)
    * [Login](https://github.com/oopaze/Biblioteca-API#login)
    * [Usuarios](https://github.com/oopaze/Biblioteca-API#usuarios)
    * [Livros](https://github.com/oopaze/Biblioteca-API#livros)
    * [Autores](https://github.com/oopaze/Biblioteca-API#autores)
    * [Biblioteca](https://github.com/oopaze/Biblioteca-API#biblioteca)
* [Objetivos](https://github.com/oopaze/Biblioteca-API#objetivos)
* [Atividades](https://github.com/oopaze/Biblioteca-API#atividades)


## Sobre

Esse projeto foi criado e desenvolvimento pelos alunos [José Pedro](https://github.com/oopaze), [Michael Pereira](https://github.com/MichaelPereira31) e [Alan Figueiredo](https://github.com/aemmanuel138) do Instituto Federal do Ceará para ser apresentado na disciplina de Algoritimos e Programação 2 do professor Yuri Almeida Lacerda.

O Biblioteca-Fácil é uma API que permitirá auxiliar na gerência de pequenas bibliotecas diminuindo a utilização e preenchimento de protocolos de empréstimos, facilitando a gestão e melhorando a rotina diária com seus usuários. A idéia do  projeto é poder proporcionar aos usuários uma maior interação com o conteúdo disponível na biblioteca através de vários mecanismos de busca. 

Essa API foi construida usando Flask no seu backend, SQLAlchemy na configuração do banco de dados, Marshmallow nas serialização dos models e Flask-JWT para o controle de autenticação. A app conta com dois tipos de autenticação nas rotas, uma para administradores e outra para usuários, onde o administrador tem acesso a tudo. 

Por padrão a Biblioteca-Fácil usa SQLite3 como banco de dados, porém ela pode trabalhar com qualquer tipo de banco de dados relacional adicionando somente as variaveis de ambiente uma variavel chamada DATABASE_URI com uma conexão válida. Ex.: 

* modelo: "tipo_de_db://username:senha@endereço:porta/nome_database"
* exemplo: "postgresql://scott:tiger@localhost:5432/mydatabase"
* linux script: 
    ```bash
    export DATABASE_URI="postgresql://scott:tiger@localhost:5432/mydatabase"
    ```
* windows script: 
    ```shell 
    set DATABASE_URI="postgresql://scott:tiger@localhost:5432/mydatabase"
    ```


## Instalação
```shell
    #Baixando proeto
    git clone https://github.com/oopaze/Biblioteca-API.git

    #Entrando na pasta do projeto
    cd Biblioteca-API

    
    #Instalando dependências e criando banco
    Linux: source initialize.sh
    Windows: initialize
```


## Rotas

### Login

1. `/login` - POST - Gera seu token de autenticação

### Usuarios

1. `user/` - GET - Mostra todos os usuários (Somente para Administradores)
2. `user/voce/` - GET - Mostra todos os dados do usuario logado (Necessita estar logado)
3. `user/` - POST - Cria um novo usuário
4. `user/<int:id>/` - GET - Mostra um único usuário (Somente para Administradores)
5. `user/<int:id>/` - PUT - Atualiza um único usuário (Somente para Administradores)
6. `user/password/` - PUT - Atualiza senha do usuário logado (Necessita estar logado)
7. `user/<int:id>/` - DELETE - Deleta um único usuário (Somente para Administradores)

### Livros

1. `livro/` - GET - Mostra todos os livros (Necessita estar logado)
2. `livro/` - POST - Adiciona um livro (Somente para Administradores)
3. `livro/varios/` - POST - Adiciona vários livros (Somente para Administradores)
4. `livro/<int:id>/` - GET - Mostra somente um livro (Necessita estar logado)
5. `livro/<int:id>/` - PUT - Atualiza um livro (Somente para Administradores)
6. `livro/<int:id>/` - DELETE - Deleta um livro (Somente para Administradores)

### Autores

Todo autor é composto por um name e um ID, porém o campo ID não é necessário ser enviado. Para atualizar/deletar um autor, é necessário enviar o ID do autor na URL.

* `autor/` - GET - Mostra todos os autores (Somente para Administradores)
* `autor/` - POST - Adiciona um novo autor (Somente para Administradores)

Para adicionar um autor é necessário ser enviado um JSON contendo com um campo "name".

**como por exemplo:**
```
  {
    "name": nome do autor
  }
```
* `autor/:id/` - PUT - Atualizar um autor pelo ID (Somente para Administradores)
Para atualizar um autor é necessário passar o ID do autor na URL e enviar um JSON contendo o campo "name".

**como por exemplo:**
```
  {
    "name": nome do autor
  }
```
* `autor/:id/` - DELETE - Deletar um autor pelo ID (Somente para Administradores)

Para deletar um autor é necessário passar o ID do autor na URL.

### Biblioteca

Esta  aplicação engloba as funções principais da biblioteca. É aqui onde são feitos o controle dos livros, dos emprestimos, das devoluções, das disponibilidades e das pendências.

* `biblioteca/emprestar/` - POST - Realiza o emprestimos dos livros(Somente para Administradores)

Para adicionar um emprestimo é necessário ser enviado um JSON contendo com um campo opcional "usuario" com o ID do usuário e um campo "livros" com um Array com o ID de cada livro a ser emprestado. Se o campo "usuario" não for enviado o emprestimo sera feito com o usuário logado.

**como por exemplo:**
```
  {
    "usuario": id do usuario,
    "livros": [
        id do livro,
        id do livro,
        id do livro
    ]
  }
```
* `biblioteca/devolucao/` - POST - Realiza a devolução do livro(Somente para Administradores)

Para realizar uma devolução é necessário ser enviado um JSON com o campo "usuario" contendo o ID do usuário.

**como por exemplo:**
```
  {
    "usuario": id do usuario,
  }
```
* `biblioteca/pendencias/` - GET - Mostra as devoluções que estão pendentes(Somente para Administradores)
* `biblioteca/emprestimos/` - GET - Mostra todos os emprestomos (Somente para Administradores)
* `biblioteca/disponiveis/` - GET - Mostra todos os livros disponiveis (Somente para Administradores)
* `biblioteca/indisponivel/` - GET - Mostra todos os livros indisponivel(Necessita estar logado)


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


