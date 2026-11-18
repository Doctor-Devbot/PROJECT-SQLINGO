import { useEffect, useState } from 'react';
import './Jogadores.css';
import { buscarJogadoresPaginacao } from '../../services/api';

const OPCOES_POR_PAGINA = [5, 10, 20];

export default function Jogadores() {
  const [pag, setPag] = useState(1);
  const [porPagina, setPorPagina] = useState(5);

  const [dados, setDados] = useState(null);
  const [erro, setErro] = useState(null);
  const [carregando, setCarregando] = useState(true);

  useEffect(() => {
    // Integração com o back-end: GET /jogador/paginacao?pag=X&por_pagina=Y
    setCarregando(true);
    setErro(null);

    buscarJogadoresPaginacao(pag, porPagina)
      .then((resultado) => {
        setDados(resultado);
      })
      .catch((errApi) => {
        setErro(errApi.message || 'Não foi possível carregar os jogadores.');
      })
      .finally(() => {
        setCarregando(false);
      });
  }, [pag, porPagina]);

  const irParaPagina = (novaPagina) => {
    if (novaPagina < 1) return;
    setPag(novaPagina);
  };

  const trocarPorPagina = (e) => {
    setPorPagina(Number(e.target.value));
    setPag(1); // ao mudar o tamanho da página, volta para a primeira
  };

  return (
    <div className="jogadores-container">
      <h1>Jogadores</h1>

      <section className="jogadores-conteudo">
        {erro && <p className="jogadores-erro">{erro}</p>}

        {carregando && !erro && (
          <p className="jogadores-status">Carregando jogadores...</p>
        )}

        {!carregando && !erro && dados && (
          <>
            <table className="jogadores-tabela">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Nome</th>
                  <th>E-mail</th>
                  <th>Atividades resolvidas (N:N)</th>
                </tr>
              </thead>
              <tbody>
                {dados.items.length > 0 ? (
                  dados.items.map((jogador) => (
                    <tr key={jogador.id}>
                      <td>{jogador.id}</td>
                      <td>{jogador.nome}</td>
                      <td>{jogador.email}</td>
                      <td>
                        {jogador.atividades_ids &&
                        jogador.atividades_ids.length > 0 ? (
                          <span className="jogadores-badges">
                            {jogador.atividades_ids.map((idAtividade) => (
                              <span key={idAtividade} className="jogadores-badge">
                                #{idAtividade}
                              </span>
                            ))}
                          </span>
                        ) : (
                          <span className="jogadores-sem-vinculo">
                            Nenhuma ainda
                          </span>
                        )}
                      </td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={4} className="jogadores-vazio">
                      Nenhum jogador cadastrado.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>

            <div className="jogadores-controles">
              <label className="jogadores-label-por-pagina">
                Por página:{' '}
                <select
                  value={porPagina}
                  onChange={trocarPorPagina}
                  className="jogadores-select"
                >
                  {OPCOES_POR_PAGINA.map((opcao) => (
                    <option key={opcao} value={opcao}>
                      {opcao}
                    </option>
                  ))}
                </select>
              </label>

              <div className="jogadores-navegacao">
                <button
                  type="button"
                  className="btn-global"
                  disabled={!dados.has_prev}
                  onClick={() => irParaPagina(dados.prev_num)}
                >
                  Anterior
                </button>

                <span className="jogadores-info-pagina">
                  Página {dados.page} de {dados.total_pages}
                </span>

                <button
                  type="button"
                  className="btn-global"
                  disabled={!dados.has_next}
                  onClick={() => irParaPagina(dados.next_num)}
                >
                  Próxima
                </button>
              </div>
            </div>
          </>
        )}
      </section>
    </div>
  );
}
