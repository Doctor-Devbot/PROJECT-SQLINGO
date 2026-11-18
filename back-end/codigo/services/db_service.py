from flask_sqlalchemy import SQLAlchemy

# Instância compartilhada pelas camadas de acesso a dados
db = SQLAlchemy()


# ---------------------------------------------------------------------------
# Helpers de compatibilidade SQLite (dev. local) x MySQL (nuvem Aiven/Render)
# Seguem a tabela de migração da Aula 14:
#   SQLite: INTEGER PRIMARY KEY AUTOINCREMENT | TEXT | INSERT OR IGNORE
#   MySQL : INTEGER PRIMARY KEY AUTO_INCREMENT | VARCHAR(N) | INSERT IGNORE
# ---------------------------------------------------------------------------


def dialeto_atual():
    """Retorna o nome do dialeto do banco em uso ('sqlite' ou 'mysql')."""
    return db.session.get_bind().dialect.name


def eh_mysql():
    """True quando a API está conectada ao MySQL da nuvem (Aiven)."""
    return dialeto_atual() == "mysql"


def chave_autoincremento():
    """Cláusula de geração automática da chave primária (AUTO_INCREMENT)."""
    return "AUTO_INCREMENT" if eh_mysql() else "AUTOINCREMENT"


def tipo_texto(tamanho=None):
    """
    Tipo de dado para colunas de texto.
    - MySQL: VARCHAR(N) exige tamanho máximo (Aula 14).
    - SQLite: TEXT tem comprimento dinâmico.
    Sem tamanho informado, usa TEXT nos dois bancos (textos longos/JSON).
    """
    if eh_mysql():
        return f"VARCHAR({tamanho})" if tamanho else "TEXT"
    return "TEXT"


def prefixo_insert_ignorado():
    """INSERT que ignora duplicidades: INSERT IGNORE (MySQL) / INSERT OR IGNORE (SQLite)."""
    return "INSERT IGNORE" if eh_mysql() else "INSERT OR IGNORE"
