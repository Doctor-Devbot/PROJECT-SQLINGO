<<<<<<< HEAD
import { useEffect, useRef, useState } from 'react';
import { Outlet, useLocation } from 'react-router-dom';
import Sidebar from '../Sidebar/Sidebar';
import './Layout.css';

// Ordem das abas: define a direção do slide na troca de tela
const ORDEM_ABAS = { '/': 0, '/comandos': 1 };

export default function Layout() {
  const location = useLocation();
  const caminhoAnterior = useRef(location.pathname);
  const [cortina, setCortina] = useState(false);
  const [direcao, setDirecao] = useState('direita');

  useEffect(() => {
    if (caminhoAnterior.current === location.pathname) return;

    const ordemAnterior = ORDEM_ABAS[caminhoAnterior.current] ?? 2;
    const ordemAtual = ORDEM_ABAS[location.pathname] ?? 2;
    setDirecao(ordemAtual >= ordemAnterior ? 'direita' : 'esquerda');
    caminhoAnterior.current = location.pathname;

    // Dispara a cortina de transição (decorativa, não bloqueia cliques)
    setCortina(true);
    const timer = setTimeout(() => setCortina(false), 950);
    return () => clearTimeout(timer);
  }, [location.pathname]);

  return (
    <div className="layout-container">
      <Sidebar />
      <main
        key={location.pathname}
        className={`conteudo-principal slide-${direcao}`}
      >
        <Outlet />
      </main>

      {cortina && (
        <div className="cortina-transicao" aria-hidden="true">
          <span />
          <span />
          <span />
        </div>
      )}
    </div>
  );
}
=======
import { Outlet } from 'react-router-dom';
import Sidebar from '../Sidebar/Sidebar';
import './Layout.css';

export default function Layout() {
  return (
    <div className="layout-container">
      <Sidebar />
      <main className="conteudo-principal">
        <Outlet />
      </main>
    </div>
  );
}
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
