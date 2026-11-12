// Dicionário de comandos SQL exibidos na aba "Comandos".
// Conteúdo está no front-end porque a API do back-end não possui
// endpoint de comandos — as demais integrações permanecem intactas.

export const COMANDOS = [
  {
    id: 'select',
    nome: 'SELECT',
    categoria: 'DML',
    resumo: 'Consulta e retorna dados de uma ou mais tabelas.',
    descricao:
      'O SELECT é o comando mais usado do SQL: ele consulta o banco e devolve exatamente os dados que você pedir. Você escolhe as colunas, indica a tabela de origem e ainda pode filtrar, ordenar e limitar os resultados.',
    comoFunciona:
      'Depois da palavra SELECT você lista as colunas desejadas (ou usa * para trazer todas). O FROM indica a tabela de onde os dados saem. A partir daí é possível filtrar linhas com WHERE e ordenar o resultado com ORDER BY.',
    sintaxe: 'SELECT coluna1, coluna2 FROM tabela WHERE condição ORDER BY coluna;',
    exemplo: "SELECT nome, email FROM clientes WHERE cidade = 'São Paulo' ORDER BY nome;",
    dica: 'Use LIMIT para testar consultas em tabelas grandes sem travar a tela.',
  },
  {
    id: 'insert',
    nome: 'INSERT',
    categoria: 'DML',
    resumo: 'Insere novos registros (linhas) em uma tabela.',
    descricao:
      'O INSERT adiciona linhas novas a uma tabela existente. Você informa a tabela, quais colunas serão preenchidas e os valores de cada uma — sempre na mesma ordem.',
    comoFunciona:
      'INTO indica a tabela; entre parênteses vêm as colunas; VALUES recebe os valores na mesma ordem. Textos vão entre aspas simples, números e datas no formato do banco ficam sem aspas.',
    sintaxe: "INSERT INTO tabela (coluna1, coluna2) VALUES (valor1, valor2);",
    exemplo: "INSERT INTO clientes (nome, email, cidade) VALUES ('Maria Silva', 'maria@email.com', 'Recife');",
    dica: 'Inserir várias linhas de uma vez? Basta repetir os parênteses separados por vírgula em VALUES.',
  },
  {
    id: 'update',
    nome: 'UPDATE',
    categoria: 'DML',
    resumo: 'Modifica dados de registros que já existem.',
    descricao:
      'O UPDATE altera valores de registros já gravados na tabela. Com SET você define qual coluna recebe qual valor e com WHERE escolhe exatamente quais linhas serão afetadas.',
    comoFunciona:
      'SET define os pares "coluna = valor" separados por vírgula. O WHERE é a sua rede de segurança: sem ele, o UPDATE altera TODAS as linhas da tabela de uma vez.',
    sintaxe: 'UPDATE tabela SET coluna = novo_valor WHERE condição;',
    exemplo: "UPDATE clientes SET cidade = 'Campinas' WHERE id = 7;",
    dica: 'Antes de rodar um UPDATE, teste o WHERE dentro de um SELECT para conferir quais linhas serão atingidas.',
    perigo: true,
  },
  {
    id: 'create',
    nome: 'CREATE',
    categoria: 'DDL',
    resumo: 'Cria estruturas no banco: tabelas, bancos e índices.',
    descricao:
      'O CREATE constrói objetos novos no banco de dados. O uso mais comum é criar tabelas, definindo o nome, as colunas, os tipos de dados e as restrições de integridade.',
    comoFunciona:
      'Cada coluna é declarada com "nome + tipo" (INTEGER, TEXT, DATE...) e pode receber restrições como PRIMARY KEY, NOT NULL e UNIQUE, que protegem a qualidade dos dados gravados.',
    sintaxe: 'CREATE TABLE tabela (coluna1 tipo restrição, coluna2 tipo restrição);',
    exemplo: 'CREATE TABLE clientes (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, email TEXT UNIQUE, cidade TEXT);',
    dica: 'Nome de tabela no plural e colunas no singular ajuda a manter o banco organizado.',
  },
  {
    id: 'alter',
    nome: 'ALTER',
    categoria: 'DDL',
    resumo: 'Modifica a estrutura de uma tabela existente.',
    descricao:
      'O ALTER muda a estrutura de uma tabela que já existe: adiciona, remove ou renomeia colunas e restrições — sem apagar os dados que já estão lá dentro.',
    comoFunciona:
      'Depois de ALTER TABLE vem a tabela e a ação: ADD COLUMN cria uma coluna nova, DROP COLUMN remove uma coluna, RENAME COLUMN troca o nome dela e RENAME TO renomeia a tabela inteira.',
    sintaxe: 'ALTER TABLE tabela ADD COLUMN coluna tipo;',
    exemplo: 'ALTER TABLE clientes ADD COLUMN telefone TEXT;',
    dica: 'Colunas adicionadas com ALTER já existem para todas as linhas — antigas e novas.',
  },
  {
    id: 'drop',
    nome: 'DROP',
    categoria: 'DDL',
    resumo: 'Remove completamente uma tabela ou banco do sistema.',
    descricao:
      'O DROP apaga o objeto inteiro do banco de dados: estrutura, dados, índices e tudo mais. É o comando mais destrutivo do SQL e não pede confirmação.',
    comoFunciona:
      'Basta indicar o tipo do objeto e o nome. A tabela some na hora, junto com todos os dados. Em bancos reais, só um backup traz o conteúdo de volta — por isso use DROP com muita consciência.',
    sintaxe: 'DROP TABLE tabela;',
    exemplo: 'DROP TABLE clientes_temporarios;',
    dica: 'Para esvaziar uma tabela mas manter a estrutura, prefira DELETE (remove as linhas) em vez de DROP.',
    perigo: true,
  },
];

// Seções exibidas na página, na mesma divisão do site original
export const SECOES_COMANDOS = [
  {
    titulo: 'Comandos de Manipulação de Dados',
    subtitulo: 'DML — escrevem e leem os dados dentro das tabelas',
    categoria: 'DML',
  },
  {
    titulo: 'Comandos de Definição de Dados',
    subtitulo: 'DDL — criam e modificam a estrutura do banco',
    categoria: 'DDL',
  },
];
