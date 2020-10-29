# BIBLIOTECA-API

## Routes

### Login

1. `auth/` - POST - Gera seu token de autenticação

### Usuarios

1. `user/` - GET - Mostra todos os usuários (Somente para Administradores)
2. `user/voce/` - GET - Mostra todos os dados do usuario logado (Necessita estar logado)
3. `user/` - POST - Cria um novo usuário
4. `user/<int:id>/` - GET - Mostra um único usuário (Somente para Administradores)
5. `user/<int:id>/` - PUT - Atualiza um único usuário (Somente para Administradores)
6. `user/password/` - PUT - Atualiza senha de usuário logado (Necessita estar logado)
7. `user/<int:id>/` - DELETE - Deleta um único usuário (Somente para Administradores)

### Livros

1. `livro/` - GET - Mostra todos os livros (Necessita estar logado)
2. `livro/` - POST - Adiciona um livro (Somente para Administradores)
3. `livro/<int:id>/` - GET - Mostra somente um livro (Necessita estar logado)
4. `livro/<int:id>/` - PUT - Atualiza um livro (Somente para Administradores)
5. `livro/<int:id>/` - DELETE - Deleta um livro (Somente para Administradores)

### Autores

### Biblioteca