# Trabalho-LTP-2-Bimestre
Trabalho LTP: Front-end; Back-end; Artefatos;


Tabela de Endpoints: .\artefatos\TabelasEndpoints.pdf

Mantenham as pastas organizadas:
Cada classe tem seus próprios arquivos dentro dos escopos MVC-DAO
Cada componente deve ter sua classe
Organizar possíveis anexos em pastas diferentes dividas por grupos; Isso dentro da pasta anexos

---

## Implantação na Nuvem (Aula 15)

A API já está preparada para o deploy no **Render** (PaaS) com banco **MySQL Aiven**:

| Arquivo | Função |
| --- | --- |
| `Procfile` (raiz e `back-end/codigo`) | Start command: `gunicorn app:app` |
| `back-end/codigo/requirements.txt` | Dependências congeladas (Flask, flask-cors, PyMySQL, gunicorn...) |
| `back-end/codigo/testes.http` | Testes REST Client com `@baseUrl` da nuvem |
| `back-end/codigo/.env.example` | Modelo das variáveis de ambiente (copie para `.env`) |
| `.gitignore` | Garante que o `.env` NUNCA vá para o GitHub |

Guia passo a passo completo: **Guia_Deploy_Render_SQLINGO.pdf**.

### Resumo rápido do deploy

1. `git push` (com `.env` ignorado no `.gitignore`);
2. No Render: **Create new service > Web Service** > conectar o repositório;
3. Build Command: `pip install -r back-end/codigo/requirements.txt`;
4. O `Procfile` da raiz já define o Start Command (Gunicorn);
5. Cadastrar em **Environment** as variáveis `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_NAME` (serviço MySQL do Aiven) e `JWT_SECRET_KEY`;
6. Testar com a extensão REST Client (`testes.http`) usando a URL `https://<servico>.onrender.com`.

Sem `DB_PASSWORD` no ambiente, a API usa **SQLite automaticamente** (desenvolvimento local, comportamento original do projeto).

## Relacionamento Muitos-para-Muitos (Aula 14)

**Jogador N:N Atividade** — tabela intermediária `jogador_atividade`
(chave primária composta `jogador_id + atividade_id`, chaves estrangeiras com
`ON DELETE CASCADE`):

- `dao/jogador_atividade_dao.py`: DAO da tabela intermediária (vincula/desvincula/busca);
- `repository/jogador_repository.py`: orquestra jogador + vínculos N:N e monta o JSON aninhado;
- `POST /jogador` aceita `"atividades_ids": [1, 3]` (equivalente ao `grupos_ids` dos slides);
- `GET /jogador` devolve cada jogador com a lista `atividades_ids`.

## Rodando em desenvolvimento

**Back-end** (na pasta `back-end/codigo`):

```bash
python -m venv venv
venv\Scripts\Activate            # Windows (source venv/bin/activate no Linux/Mac)
pip install -r requirements.txt
python app.py                    # http://localhost:5000 (SQLite local)
```

**Front-end** (na pasta `front-end/codigo`):

```bash
npm install
npm run dev                      # http://localhost:5173 (Vite)
```

> Para apontar o front-end para a API na nuvem, crie `front-end/codigo/.env`
> com `VITE_API_URL=https://<servico>.onrender.com`.

## Endpoints principais

| Método | Rota | Descrição |
| --- | --- | --- |
| POST | `/jogador` | Cadastra jogador (aceita `atividades_ids` do N:N) |
| GET | `/jogador` | Lista jogadores com `atividades_ids` aninhados |
| GET | `/jogador/paginacao?pag=1&por_pagina=5` | Lista paginada (usada pelo front-end) |
| POST | `/login` | Autenticação com retorno de token JWT |
| GET | `/perfil/protegido` | Endpoint protegido por JWT |
| GET | `/modulo`, `/lista-atividade`, `/lista-atividade/<id>/atividades`, `/atividade` | Telas do jogo |
