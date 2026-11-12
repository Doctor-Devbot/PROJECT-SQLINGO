<<<<<<< HEAD
import { useEffect, useRef, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import './Sidebar.css';
import logo from '../../assets/images/logoSQLingo2.png';

// Paletas disponíveis para o usuário alternar
const PALETAS = [
  { id: 'original', nome: 'Original', descricao: 'Azul clássico', cores: ['#00b7ff', '#004fa8'] },
  { id: 'verde', nome: 'Terminal', descricao: 'Verde, preto e vermelho', cores: ['#2ee06f', '#0c1210', '#ff5c5c'] },
  { id: 'roxo', nome: 'Aurora', descricao: 'Roxo, laranja e amarelo', cores: ['#8b5cf6', '#ff8a2a', '#ffc93f'] },
];

const ABAS = [
  {
    caminho: '/',
    rotulo: 'Início',
    icone: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
        <path d="M3 10.5 12 3l9 7.5" />
        <path d="M5 9.5V21h5v-6h4v6h5V9.5" />
      </svg>
    ),
  },
  {
    caminho: '/comandos',
    rotulo: 'Comandos',
    icone: (
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
        <path d="m5 7 4 4.2L5 15.5" />
        <path d="M12 16h7" />
        <rect x="2" y="3.5" width="20" height="17" rx="3" />
      </svg>
    ),
  },
];

export default function Sidebar() {
  const navigate = useNavigate();
  const location = useLocation();
  const navRef = useRef(null);

  const [tema, setTema] = useState(() => localStorage.getItem('sqlingo-tema') || 'original');
  const [indicador, setIndicador] = useState({ topo: 0, altura: 0, visivel: false });

  // Aplica e salva o tema escolhido no documento inteiro
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', tema);
    localStorage.setItem('sqlingo-tema', tema);
  }, [tema]);

  // Reposiciona a "pílula" indicadora sobre a aba ativa
  useEffect(() => {
    const posicionarIndicador = () => {
      const botaoAtivo = navRef.current?.querySelector('.btn-global.ativo');
      if (!botaoAtivo || !navRef.current) return;
      const nav = navRef.current.getBoundingClientRect();
      const botao = botaoAtivo.getBoundingClientRect();
      setIndicador({ topo: botao.top - nav.top, altura: botao.height, visivel: true });
    };

    posicionarIndicador();
    window.addEventListener('resize', posicionarIndicador);
    return () => window.removeEventListener('resize', posicionarIndicador);
  }, [location.pathname]);

  return (
    <nav id="menuLateral">
      <a className="logo-chip" href="/" onClick={(e) => { e.preventDefault(); navigate('/'); }} aria-label="SQLingo - página inicial">
        <img src={logo} id="logo" alt="Logo SQLingo" />
      </a>

      <div className="menu-nav" ref={navRef}>
        {/* Pílula deslizante que marca a aba ativa */}
        <span
          className={`indicador-aba ${indicador.visivel ? 'visivel' : ''}`}
          style={{ top: indicador.topo, height: indicador.altura }}
          aria-hidden="true"
        />

        {ABAS.map((aba) => {
          const ativo = location.pathname === aba.caminho;
          return (
            <button
              key={aba.caminho}
              className={`btn-global ${ativo ? 'ativo' : ''}`}
              onClick={() => navigate(aba.caminho)}
              aria-current={ativo ? 'page' : undefined}
            >
              <span className="aba-icone" aria-hidden="true">{aba.icone}</span>
              <span className="aba-rotulo">{aba.rotulo}</span>
            </button>
          );
        })}
      </div>

      <div className="seletor-paleta">
        <p className="seletor-titulo">Tema</p>
        <div className="seletor-opcoes" role="radiogroup" aria-label="Escolher paleta de cores">
          {PALETAS.map((paleta) => (
            <button
              key={paleta.id}
              className={`swatch ${tema === paleta.id ? 'ativo' : ''}`}
              onClick={() => setTema(paleta.id)}
              role="radio"
              aria-checked={tema === paleta.id}
              title={`${paleta.nome} — ${paleta.descricao}`}
              aria-label={`Paleta ${paleta.nome}: ${paleta.descricao}`}
            >
              {paleta.cores.map((cor) => (
                <span key={cor} className="swatch-cor" style={{ background: cor }} />
              ))}
            </button>
          ))}
        </div>
        <p className="seletor-nome">
          {PALETAS.find((p) => p.id === tema)?.nome}
        </p>
      </div>
    </nav>
  );
}
=======
import { useNavigate } from 'react-router-dom';
import './Sidebar.css';
import logo from '../../assets/images/logoSQLingo2.png';

export default function Sidebar() {
  const navigate = useNavigate();

  return (
    <nav id="menuLateral">
      <img src={logo} id="logo" alt="Logo SQLingo" />
      <button className="btn-global" onClick={() => navigate('/')}>
        Início
      </button>
      <button className="btn-global" onClick={() => navigate('/comandos')}>
        Comandos
      </button>
    </nav>
  );
}
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
