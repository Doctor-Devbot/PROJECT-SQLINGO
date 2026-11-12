import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import './Activity.css';
<<<<<<< HEAD
import Mascote from '../../components/Mascote/Mascote';
import dicaImg from '../../assets/images/dica.png';
import dicaDisableImg from '../../assets/images/dicaDisableTransparente.png';

// Confete da tela final: posições fixas (sem aleatoriedade no render)
const CONFETES = Array.from({ length: 18 }, (_, i) => ({
  esquerda: (i * 53) % 100,
  atraso: (i % 6) * 0.35,
  duracao: 2.6 + (i % 4) * 0.45,
  cor: ['var(--corPrimaria)', 'var(--corSecundaria)', 'var(--corDestaque)'][i % 3],
  rotacao: (i * 47) % 360,
}));

=======
import dicaImg from '../../assets/images/dica.png';
import dicaDisableImg from '../../assets/images/dicaDisableTransparente.png';

>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
export default function Activity() {
  const { idLista } = useParams();
  const navigate = useNavigate();

  const [atividades, setAtividades] = useState([]);
  const [indiceAtual, setIndiceAtual] = useState(0);
<<<<<<< HEAD

=======
  
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
  const [selecionada, setSelecionada] = useState(null);
  const [verificado, setVerificado] = useState(false);
  const [usouDica, setUsouDica] = useState(false);
  const [opcoesAtuais, setOpcoesAtuais] = useState([]);
  const [erro, setErro] = useState(null);

  const [acertos, setAcertos] = useState(0);
  const [finalizado, setFinalizado] = useState(false);

  useEffect(() => {
    fetch(`http://localhost:5000/lista-atividade/${idLista}/atividades`)
      .then((res) => {
        if (!res.ok) throw new Error('Erro ao carregar as questões');
        return res.json();
      })
      .then((data) => {
        setAtividades(data);
        if (data.length > 0) {
          setOpcoesAtuais(data[0].alternativas);
        }
      })
      .catch((err) => {
        console.error(err);
        setErro('Não foi possível carregar as atividades desta lista.');
      });
  }, [idLista]);

  useEffect(() => {
    if (atividades.length > 0 && atividades[indiceAtual]) {
      setOpcoesAtuais(atividades[indiceAtual].alternativas);
      setSelecionada(null);
      setVerificado(false);
      setUsouDica(false);
    }
  }, [indiceAtual, atividades]);

<<<<<<< HEAD
  if (erro) return <p className="activity-erro">{erro}</p>;
  if (atividades.length === 0) return <p className="activity-carregando">Carregando atividades...</p>;

  // TELA DE FINALIZAÇÃO comemorativa (mascote + confete)
=======
  if (erro) return <p style={{ color: 'red', textAlign: 'center', marginTop: '50px' }}>{erro}</p>;
  if (atividades.length === 0) return <p style={{ textAlign: 'center', marginTop: '50px' }}>Carregando atividades...</p>;

  // TELA DE FINALIZAÇÃO REESTRUTURADA COM O MESMO DESIGN DOS CARDS
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
  if (finalizado) {
    const percentualAcertos = Math.round((acertos / atividades.length) * 100);
    const totalPontos = acertos * 10;

    return (
      <div id="containerPrincipal">
<<<<<<< HEAD
        <div className="confete-container" aria-hidden="true">
          {CONFETES.map((confete, i) => (
            <span
              key={i}
              style={{
                left: `${confete.esquerda}%`,
                background: confete.cor,
                animationDelay: `${confete.atraso}s`,
                animationDuration: `${confete.duracao}s`,
                '--rotacao-confete': `${confete.rotacao}deg`,
              }}
            />
          ))}
        </div>

        <section id="menuPrincipal" className="card-finalizacao-conteudo">
          <div className="finalizacao-mascote">
            <Mascote />
          </div>
          <h1>Parabéns!</h1>
          <h2>Atividade chegou ao fim!</h2>

=======
        <section id="menuPrincipal" className="card-finalizacao-conteudo">
          <h1>Parabéns!</h1>
          <h2>Atividade chegou ao fim!</h2>
          
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
          <div className="finalizacao-stats-container">
            <div className="stat-box">
              <p>Acertos:</p>
              <div className="stat-value">{percentualAcertos}%</div>
            </div>
            <div className="stat-box">
              <p>Pontos:</p>
              <div className="stat-value">{totalPontos}</div>
            </div>
          </div>
<<<<<<< HEAD

          <div className="finalizacao-botoes">
            <button
              className="btn-3d"
              onClick={() => {
                setIndiceAtual(0);
                setAcertos(0);
                setFinalizado(false);
              }}
            >
              Praticar de novo
            </button>
            <button className="btn-3d" onClick={() => navigate('/')}>
              Sair
            </button>
          </div>
        </section>
=======
        </section>

        <button 
          id="verificarBotao" 
          onClick={() => navigate('/')}
        >
          Sair
        </button>

>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
      </div>
    );
  }

  const atividadeAtual = atividades[indiceAtual];
  const respostaCorreta = atividadeAtual.alternativas[0];
<<<<<<< HEAD
  const questoesRespondidas = verificado ? indiceAtual + 1 : indiceAtual;
  const progresso = Math.round((questoesRespondidas / atividades.length) * 100);

  const handleDica = () => {
    if (usouDica || verificado) return;

=======

  const handleDica = () => {
    if (usouDica || verificado) return;
    
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
    const erradas = atividadeAtual.alternativas.filter(alt => alt !== respostaCorreta);
    const dicaOpcoes = [respostaCorreta, erradas[0]].sort(() => Math.random() - 0.5);

    setOpcoesAtuais(dicaOpcoes);
    setUsouDica(true);
    if (selecionada && !dicaOpcoes.includes(selecionada)) {
      setSelecionada(null);
    }
  };

  const handleVerificar = () => {
    if (!selecionada) return;
    setVerificado(true);
<<<<<<< HEAD

=======
    
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
    if (selecionada === respostaCorreta) {
      setAcertos((prev) => prev + 1);
    }
  };

  const handleProxima = () => {
    if (indiceAtual + 1 < atividades.length) {
      setIndiceAtual(indiceAtual + 1);
    } else {
      setFinalizado(true);
    }
  };

  const getEstiloBotao = (opcao) => {
    if (verificado) {
      if (opcao === respostaCorreta) return "botao-correto";
      if (opcao === selecionada) return "botao-errado";
      return "botao-desabilitado";
    }
    return opcao === selecionada ? "botao-selecionado" : "botao-opcao";
  };

  return (
    <div id="containerPrincipal">
      <section id="menuPrincipal">
<<<<<<< HEAD
        {/* Barra de progresso da lista */}
        <div className="progresso-cabecalho">
          <span className="progresso-texto">
            Questão {indiceAtual + 1} de {atividades.length}
          </span>
          <div
            className="barra-progresso"
            role="progressbar"
            aria-valuenow={progresso}
            aria-valuemin={0}
            aria-valuemax={100}
            aria-label="Progresso da lista de atividades"
          >
            <div className="barra-progresso-preenchimento" style={{ width: `${progresso}%` }} />
          </div>
        </div>

        <h1>Selecione a alternativa correta</h1>
        <h2>
          {atividadeAtual.enunciado}
          <button
            id="dicaBotao"
            onClick={handleDica}
            disabled={usouDica || verificado}
            className={usouDica || verificado ? 'dica-disable' : ''}
            title={usouDica || verificado ? 'Dica já utilizada' : 'Usar dica (remove duas alternativas)'}
=======
        <span style={{ fontSize: '0.9rem', color: '#666', fontWeight: 'bold' }}>
          Questão {indiceAtual + 1} de {atividades.length}
        </span>
        <h1>Selecione a alternativa correta</h1>
        <h2>
          {atividadeAtual.enunciado}
          <button 
            id="dicaBotao" 
            onClick={handleDica} 
            disabled={usouDica || verificado}
            className={usouDica || verificado ? 'dica-disable' : ''}
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
          >
            <img src={(usouDica || verificado) ? dicaDisableImg : dicaImg} alt="Dica" />
          </button>
        </h2>

        <ul>
          {opcoesAtuais.map((opcao) => (
            <li key={opcao}>
              <button
                className={getEstiloBotao(opcao)}
                onClick={() => !verificado && setSelecionada(opcao)}
                disabled={verificado}
              >
                {opcao}
              </button>
            </li>
          ))}
        </ul>
      </section>

      {!verificado ? (
<<<<<<< HEAD
        <button
          id="verificarBotao"
          className="btn-verificar"
=======
        <button 
          id="verificarBotao" 
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
          onClick={handleVerificar}
          disabled={!selecionada}
        >
          Verificar
        </button>
      ) : (
<<<<<<< HEAD
        <button
          id="verificarBotao"
          className={`btn-verificar ${selecionada === respostaCorreta ? 'btn-proxima-acerto' : 'btn-proxima-erro'}`}
          onClick={handleProxima}
=======
        <button 
          id="verificarBotao" 
          onClick={handleProxima}
          style={{ backgroundColor: '#28a745', color: '#fff' }}
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
        >
          {indiceAtual + 1 === atividades.length ? 'Finalizar' : 'Próxima'}
        </button>
      )}
    </div>
  );
<<<<<<< HEAD
}
=======
}
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
