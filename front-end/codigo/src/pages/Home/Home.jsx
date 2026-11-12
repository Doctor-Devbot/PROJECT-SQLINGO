<<<<<<< HEAD
import { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Mascote from '../../components/Mascote/Mascote';
import './Home.css';

// Mensagens que o mascote alterna na tela inicial
const MENSAGENS_MASCOTE = [
  'Vamos praticar SQL hoje?',
  'Sabia que o SELECT é o comando mais usado no mundo?',
  'Dica: um pouquinho de prática todo dia vale mais que uma maratona!',
  'Tem um dicionário de comandos esperando por você na aba Comandos!',
  'Erro é só um dado a mais na sua tabela de aprendizado.',
];

// Símbolos que flutuam no fundo da home
const SIMBOLOS_FUNDO = ['SELECT', 'JOIN', 'WHERE', 'GROUP BY', 'ORDER BY', 'INSERT'];

=======
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css';

>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
export default function Home() {
  const navigate = useNavigate();
  const [modulos, setModulos] = useState([]);
  const [listasAtividade, setListasAtividade] = useState([]);
  const [erro, setErro] = useState(null);
<<<<<<< HEAD
  const [carregando, setCarregando] = useState(true);
  const [moduloAberto, setModuloAberto] = useState(null);
  const [indiceMensagem, setIndiceMensagem] = useState(0);
  const inicioRef = useRef(null);
=======
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df

  useEffect(() => {
    // Busca os módulos e as listas de atividades simultaneamente do back-end Flask
    Promise.all([
      fetch('http://localhost:5000/modulo').then((res) => {
        if (!res.ok) throw new Error('Erro ao carregar os módulos');
        return res.json();
      }),
      fetch('http://localhost:5000/lista-atividade').then((res) => {
        if (!res.ok) throw new Error('Erro ao carregar as listas de atividades');
        return res.json();
      })
    ])
      .then(([dadosModulos, dadosListas]) => {
<<<<<<< HEAD
        setModulos(dadosModulos);
        setListasAtividade(dadosListas);
        // Abre o primeiro módulo por padrão para o usuário já ver as atividades
        setModuloAberto(dadosModulos.length > 0 ? dadosModulos[0].id : null);
        setCarregando(false);
=======
        console.log("MÓDULOS RECEBIDOS:", dadosModulos);
        console.log("LISTAS RECEBIDAS:", dadosListas);
        setModulos(dadosModulos);
        setListasAtividade(dadosListas);
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
      })
      .catch((err) => {
        console.error(err);
        setErro('Não foi possível carregar os dados da página.');
<<<<<<< HEAD
        setCarregando(false);
      });
  }, []);

  // Alterna as falas do mascote a cada 4 segundos
  useEffect(() => {
    const timer = setInterval(() => {
      setIndiceMensagem((atual) => (atual + 1) % MENSAGENS_MASCOTE.length);
    }, 4000);
    return () => clearInterval(timer);
  }, []);

  // Abre/fecha um módulo (só um aberto por vez, para a tela ficar enxuta)
  const alternarModulo = (idModulo) => {
    setModuloAberto((aberto) => (aberto === idModulo ? null : idModulo));
  };

  const comecarPratica = () => {
    if (modulos.length === 0) return;
    setModuloAberto(modulos[0].id);
    inicioRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  const totalAtividades = listasAtividade.length;

  return (
    <div className="home-container">
      {/* Símbolos de SQL flutuando ao fundo (decorativo) */}
      <div className="decor-fundo" aria-hidden="true">
        {SIMBOLOS_FUNDO.map((simbolo, i) => (
          <span key={simbolo} style={{ animationDelay: `${i * 0.9}s` }}>
            {simbolo}
          </span>
        ))}
      </div>

      {/* ---------------------- Boas-vindas ---------------------- */}
      <header className="hero">
        <div className="hero-texto">
          <span className="hero-selo">Aprenda SQL jogando</span>
          <h1>
            Olá! Pronto para a <em>jornada SQL</em>?
          </h1>
          <p className="hero-subtitulo">
            Avance pelos módulos, responda os quizzes e domine os comandos
            mais usados dos bancos de dados.
          </p>
          <div className="hero-acoes">
            <button className="btn-3d" onClick={comecarPratica}>
              Começar a praticar
            </button>
          </div>
          <ul className="hero-stats" aria-label="Resumo do conteúdo">
            <li>
              <strong>{carregando ? '–' : modulos.length}</strong>
              <span>módulos</span>
            </li>
            <li>
              <strong>{carregando ? '–' : totalAtividades}</strong>
              <span>listas de atividades</span>
            </li>
            <li>
              <strong>6</strong>
              <span>comandos para dominar</span>
            </li>
          </ul>
        </div>

        <div className="hero-mascote">
          <div className="hero-balao" aria-live="polite">
            {MENSAGENS_MASCOTE[indiceMensagem]}
          </div>
          <Mascote />
        </div>
      </header>

      {/* ---------------------- Módulos ---------------------- */}
      {erro && <p className="home-erro">{erro}</p>}

      <section className="lista-modulos" ref={inicioRef} aria-label="Módulos de estudo">
        <h2 className="lista-modulos-titulo">Trilha de aprendizado</h2>

        {carregando ? (
          // Skeletons enquanto o back-end responde
          <>
            <div className="skeleton skeleton-modulo" />
            <div className="skeleton skeleton-modulo" />
            <div className="skeleton skeleton-modulo" />
          </>
        ) : (
          modulos.map((modulo, indice) => {
            const listasDoModulo = listasAtividade.filter(
              (lista) => lista.modulo_id === modulo.id
            );
            const aberto = moduloAberto === modulo.id;

            return (
              <article
                key={modulo.id}
                className={`modulo-card ${aberto ? 'aberto' : ''}`}
              >
                {/* Cabeçalho clicável do acordeão */}
                <button
                  className="modulo-cabecalho"
                  onClick={() => alternarModulo(modulo.id)}
                  aria-expanded={aberto}
                  aria-controls={`modulo-corpo-${modulo.id}`}
                >
                  <span className="modulo-numero">{indice + 1}</span>
                  <span className="modulo-infos">
                    <span className="modulo-titulo">{modulo.titulo}</span>
                    <span className="modulo-descricao">{modulo.descricao}</span>
                  </span>
                  <span className="modulo-contador">
                    {listasDoModulo.length}{' '}
                    {listasDoModulo.length === 1 ? 'lista' : 'listas'}
                  </span>
                  <svg
                    className="modulo-chevron"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="3"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    aria-hidden="true"
                  >
                    <path d="m6 9 6 6 6-6" />
                  </svg>
                </button>

                {/* Corpo expansível com as atividades */}
                <div
                  className="modulo-corpo"
                  id={`modulo-corpo-${modulo.id}`}
                >
                  <div className="modulo-corpo-interno">
                    {listasDoModulo.length > 0 ? (
                      listasDoModulo.map((lista, i) => (
                        <button
                          key={lista.id}
                          className="atividade-card"
                          style={{ animationDelay: `${0.06 * i}s` }}
                          onClick={() => navigate(`/atividade/${lista.id}`)}
                        >
                          <span className="atividade-icone" aria-hidden="true">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                              <path d="M4 19.5V6a2 2 0 0 1 2-2h13v16H6.5A2.5 2.5 0 0 0 4 20.5z" />
                              <path d="M8 8h7M8 12h7" />
                            </svg>
                          </span>
                          <span className="atividade-infos">
                            <span className="atividade-titulo">{lista.titulo}</span>
                            <span className="atividade-descricao">
                              {lista.descricao}
                            </span>
                          </span>
                          <span className="atividade-cta">Praticar</span>
                        </button>
                      ))
                    ) : (
                      <p className="modulo-vazio">
                        Nenhuma lista cadastrada neste módulo.
                      </p>
                    )}
                  </div>
                </div>
              </article>
            );
          })
        )}
      </section>
    </div>
  );
}
=======
      });
  }, []);

  return (
    <div className="home-container">
      {erro && <p style={{ color: 'red', textAlign: 'center' }}>{erro}</p>}

      {/* Renderiza um bloco (caminhoPrincipal) para cada Módulo */}
      {modulos.length > 0 ? (
        modulos.map((modulo) => {
          // Filtra apenas as listas que pertencem a este módulo específico
          const listasDoModulo = listasAtividade.filter(
            (lista) => lista.modulo_id === modulo.id
          );

          return (
            <section key={modulo.id} id="caminhoPrincipal">
              <h1>{modulo.titulo}</h1>

              {/* Botões criados dinamicamente de acordo com a quantidade de listas do módulo */}
              <div className="botoes-container">
                {listasDoModulo.length > 0 ? (
                  listasDoModulo.map((lista, index) => (
                    // No map das listas dentro do seu Home.jsx:
                    <button
                      key={lista.id}
                      className="btn-circulo"
                      onClick={() => navigate(`/atividade/${lista.id}`)} // <-- Passa o ID da lista na rota!
                    >
                      {index + 1}
                    </button>
                  ))
                ) : (
                  <p style={{ fontSize: '0.9rem', color: '#666' }}>Nenhuma lista cadastrada neste módulo.</p>
                )}
              </div>
            </section>
          );
        })
      ) : (
        // Fallback caso os dados ainda estejam carregando ou ocorra algum atraso
        <section id="caminhoPrincipal">
          <h1>Carregando módulos...</h1>
        </section>
      )}
    </div>
  );
}
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
