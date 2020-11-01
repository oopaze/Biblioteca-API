# BIBLIOTECA-API
## Sobre

O Biblioteca-Fácil é uma API que permitirá auxiliar na gerência de pequenas bibliotecas diminuindo a utilização e preenchimento de protocolos de empréstimos, facilitando a gestão e melhorando a rotina diária com seus usuários. A idéia do  projeto é poder proporcionar aos usuários uma maior interação com o conteúdo disponível na biblioteca através de vários mecanismos de busca. 

Essa API foi construida usando Flask no seu backend, SQLAlchemy na configuração do banco de dados, Marshmallow nas serialização dos models e Flask-JWT para o controle de autenticação. A app conta com dois tipos de autenticação nas rotas, uma para administradores e outra para usuários, onde o administrador tem acesso a tudo. 

Esta usa por padrão SQLite3 como banco de dados, porém ela pode usar qualquer tipo de banco de dados relacional somente criando a variavel de ambiente DATABASE_URI com uma conexão válida: 
    ..*modelo: "tipo_de_db://username:senha@endereço:porta/nome_database";
    ..*exemplo: "postgresql://scott:tiger@localhost:5432/mydatabase";
    ..*linux script: `export DATABASE_URI="postgresql://scott:tiger@localhost:5432/mydatabase"`;
    ..*windows script: `set DATABASE_URI="postgresql://scott:tiger@localhost:5432/mydatabase"`

| Objetivos | Estado |
| ------------- |:-------------:|
| Controlar o empréstimos, renovações, reservas e pendências de livros | Concluído |
| Reduzir o tempo de atendimento nas transações | Concluído |
| Controlar o cadastro de usuários, livros e autores | Concluído |


## Desenvolvimento

Esse projeto foi criado e desenvolvimento pelos alunos [José Pedro da Silva Gomes(Eu)](https://github.com/oopaze), [Michael Pereira](https://github.com/MichaelPereira31) e [Alan Figueiredo]() do Instituto Federal do Ceará para ser apresentado na disciplina de Algoritimos e Programação 2 do professor Yuri Almeida Lacerda. 

## Instalação
```
    #Baixando proeto
    git clone https://github.com/oopaze/Biblioteca-API.git

    #Entrando na pasta do projeto
    cd Biblioteca-API

    
    #Instalando dependências e criando banco
    Linux: source initialize.sh
    Windows: initialize
```

## Routes

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

### Biblioteca