---PROJETO PRINCIPAL COM APLICAÇÃO DE LOGIN E REGISTRO---

## Estrutura
- `sistemaLogin/` → pasta principal do projeto
  - `settings.py` → configurações do Django
  - `urls.py` → rotas principais
  - `templates/base.html` → layout padrão
- `formulario/` → app de autenticação
  - `views.py` → funções de login, logout, registro, home
  - `urls.py` → rotas da app
  - `templates/formulario/` → páginas específicas (login, registro, home)

## Fluxo de autenticação
- `/login/` → página de login
- `/logout/` → encerra sessão
- `/registro/` → cadastro de novos usuários (opcional)
- `/home/` → página inicial protegida

## Templates
Todas as páginas herdam de `base.html` e usam `{% block content %}` para inserir conteúdo.

## Grupos e permissões
- Grupo "Administradores" → acesso especial
- Grupo "Visitantes" → acesso padrão

---APLICAÇÃO DE AGENDAMENTOS---

## Estrutura de agendamentos
- `models.py` → Classe com nome, data e hora do agendamento
- `forms.py` → Formulário do agendamento
- `views.py` → Funções de criar e listar agendamentos
- `urls.py` → Rotas da app

## Fluxo de agendamento
- `/criar_agendamentos/` → página de criação de agendamento
- `/listar_agendamentos/` → lista de agendamentos

## Administrador
- `admin.py` → Administração de agendamentos

---APLICAÇÃO DE FREQUÊNCIA---

## Templates
- `/registrar/` → formulário para registrar presença.
- `/listar/` → tabela com alunos, disciplinas, datas e ✔/❌.

## Grupos e permissões
- Grupo Administradores → acesso completo ao admin e às frequências
- Grupo de Usuários → acesso apenas às páginas de registrar e listar frequência

## Estrutura de frequência
- models.py → Aluno, Disciplina, Frequencia
- forms.py → FrequenciaForm → formulário para registrar presença, com campo de data em formato brasileiro
- views.py → registrar_frequencia, listar_frequencias
- urls.py → rotas para páginas de lista de frequências e registro

## Fluxo de frequência
- /frequencias/novo/ → página de criação de registro de presença.
- /frequencias/ → lista de frequências registradas, com ✔️ para presente e ❌ para ausente.

## Administrador
- admin.py → Administração de alunos, disciplinas e frequências; Permite filtros por disciplina, data e status de presença; Busca por nome de aluno ou disciplina.
