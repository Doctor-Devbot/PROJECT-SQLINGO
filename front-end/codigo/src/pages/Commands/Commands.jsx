import { useEffect, useRef, useState } from 'react';
import { COMANDOS, SECOES_COMANDOS } from '../../data/comandos';
import './Commands.css';

// Palavras-chave para colorir os exemplos de SQL
const REGEX_SQL =
  /('(?:[^']*)')|\b(SELECT|FROM|WHERE|ORDER|BY|INSERT|INTO|VALUES|UPDATE|SET|DELETE|CREATE|TABLE|ALTER|ADD|COLUMN|DROP|PRIMARY|KEY|NOT|NULL|UNIQUE|INTEGER|TEXT|DATE|LIMIT)\b|\b(\d+)\b/g;

// Recebe um código SQL e devolve trechos coloridos (palavras-chave, textos e números)
function destacarSQL(codigo) {
  const partes = [];
  let posicaoFinal = 0;
  let correspondencia;

  REGEX_SQL.lastIndex = 0;
  while ((correspondencia = REGEX_SQL.exec(codigo)) !== null) {
    if (correspondencia.index > posicaoFinal) {
      partes.push(codigo.slice(posicaoFinal, correspondencia.index));
    }
    const [texto, textoString, palavraChave, numero] = correspondencia;
    if (textoString) {
      partes.push(
        <span key={`s-${correspondencia.index}`} className="sql-texto">
          {textoString}
        </span>
      );
    } else if (palavraChave) {
      partes.push(
        <span key={`k-${correspondencia.index}`} className="sql-palavra">
          {palavraChave}
        </span>
      );
    } else if (numero) {
      partes.push(
        <span key={`n-${correspondencia.index}`} className="sql-numero">
          {numero}
        </span>
      );
    }
    posicaoFinal = correspondencia.index + texto.length;
  }
  if (posicaoFinal < codigo.length) {
    partes.push(codigo.slice(posicaoFinal));
  }
  return partes;
}

// Ícone de lâmpada usado na dica do modal
const IconeLampada = (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    <path d="M9 18h6M10 21h4" />
    <path d="M12 3a6 6 0 0 0-4 10.5c.6.6 1 1.4 1 2.5h6c0-1.1.4-1.9 1-2.5A6 6 0 0 0 12 3z" />
  </svg>
);

// Ícone de alerta usado nos comandos perigosos
const IconeAlerta = (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    <path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z" />
    <path d="M12 9v4M12 17h.01" />
  </svg>
);

export default function Commands() {
  const [comandoAberto, setComandoAberto] = useState(null);
  const botaoOrigemRef = useRef(null);
  const modalRef = useRef(null);

  const abrirComando = (comando, evento) => {
    botaoOrigemRef.current = evento.currentTarget;
    setComandoAberto(comando);
  };

  const fecharComando = () => {
    setComandoAberto(null);
    botaoOrigemRef.current?.focus(); // devolve o foco ao cartão que abriu o modal
  };

  // Fecha com Escape, trava a rolagem do fundo e move o foco para o modal
  useEffect(() => {
    if (!comandoAberto) return;

    const aoPressionarTecla = (evento) => {
      if (evento.key === 'Escape') fecharComando();
    };

    document.addEventListener('keydown', aoPressionarTecla);
    document.body.style.overflow = 'hidden';
    modalRef.current?.querySelector('button')?.focus();

    return () => {
      document.removeEventListener('keydown', aoPressionarTecla);
      document.body.style.overflow = '';
    };
  }, [comandoAberto]);

  const renderSecao = (secao) => {
    const comandosDaSecao = COMANDOS.filter(
      (comando) => comando.categoria === secao.categoria
    );

    return (
      <div className="secao-comandos" key={secao.categoria}>
        <header className="secao-cabecalho">
          <h1>{secao.titulo}</h1>
          <p>{secao.subtitulo}</p>
        </header>

        <ul className="secao-lista">
          {comandosDaSecao.map((comando, indice) => (
            <li key={comando.id} style={{ animationDelay: `${0.07 * indice}s` }}>
              <button
                className={`btn-comando categoria-${comando.categoria.toLowerCase()} ${
                  comando.perigo ? 'perigoso' : ''
                }`}
                onClick={(evento) => abrirComando(comando, evento)}
                aria-haspopup="dialog"
              >
                <span className="btn-comando-categoria">{comando.categoria}</span>
                <span className="btn-comando-nome">{comando.nome}</span>
                <span className="btn-comando-resumo">{comando.resumo}</span>
                {comando.perigo && (
                  <span className="btn-comando-alerta" title="Comando destrutivo — use com cuidado">
                    {IconeAlerta}
                  </span>
                )}
                <span className="btn-comando-cta">Ver detalhes</span>
              </button>
            </li>
          ))}
        </ul>
      </div>
    );
  };

  return (
    <section id="comandos">
      <header className="comandos-cabecalho">
        <h1>Dicionário de comandos SQL</h1>
        <p>
          Clique em um comando para ver o que ele faz, como funciona e um
          exemplo pronto para praticar.
        </p>
      </header>

      {SECOES_COMANDOS.map(renderSecao)}

      {/* ---------------- Caixa de detalhes do comando ---------------- */}
      {comandoAberto && (
        <div
          className="modal-overlay"
          onClick={(evento) => {
            if (evento.target === evento.currentTarget) fecharComando();
          }}
          role="presentation"
        >
          <div
            className="modal-caixa"
            role="dialog"
            aria-modal="true"
            aria-label={`Detalhes do comando ${comandoAberto.nome}`}
            ref={modalRef}
          >
            <header className="modal-cabecalho">
              <span
                className={`modal-categoria categoria-${comandoAberto.categoria.toLowerCase()}`}
              >
                {comandoAberto.categoria}
              </span>
              <h2 className="modal-titulo">{comandoAberto.nome}</h2>
              <button
                className="modal-fechar"
                onClick={fecharComando}
                aria-label="Fechar detalhes do comando"
              >
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" aria-hidden="true">
                  <path d="M18 6 6 18M6 6l12 12" />
                </svg>
              </button>
            </header>

            <div className="modal-corpo">
              <section className="modal-bloco">
                <h3>O que faz</h3>
                <p>{comandoAberto.descricao}</p>
              </section>

              <section className="modal-bloco">
                <h3>Como funciona</h3>
                <p>{comandoAberto.comoFunciona}</p>
              </section>

              <section className="modal-bloco">
                <h3>Sintaxe</h3>
                <pre className="codigo-bloco">
                  <code>{destacarSQL(comandoAberto.sintaxe)}</code>
                </pre>
              </section>

              <section className="modal-bloco">
                <h3>Exemplo</h3>
                <pre className="codigo-bloco">
                  <code>{destacarSQL(comandoAberto.exemplo)}</code>
                </pre>
              </section>

              {comandoAberto.dica && (
                <p className={`modal-dica ${comandoAberto.perigo ? 'dica-alerta' : ''}`}>
                  <span className="modal-dica-icone">{comandoAberto.perigo ? IconeAlerta : IconeLampada}</span>
                  <span>{comandoAberto.dica}</span>
                </p>
              )}
            </div>
          </div>
        </div>
      )}
    </section>
  );
}
