import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import './Activity.css';
import dicaImg from '../../assets/images/dica.png';
import dicaDisableImg from '../../assets/images/dicaDisableTransparente.png';

export default function Activity() {
  const { idLista } = useParams();
  const navigate = useNavigate();

  const [atividades, setAtividades] = useState([]);
  const [indiceAtual, setIndiceAtual] = useState(0);
  
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

  if (erro) return <p style={{ color: 'red', textAlign: 'center', marginTop: '50px' }}>{erro}</p>;
  if (atividades.length === 0) return <p style={{ textAlign: 'center', marginTop: '50px' }}>Carregando atividades...</p>;

  // TELA DE FINALIZAÇÃO REESTRUTURADA COM O MESMO DESIGN DOS CARDS
  if (finalizado) {
    const percentualAcertos = Math.round((acertos / atividades.length) * 100);
    const totalPontos = acertos * 10;

    return (
      <div id="containerPrincipal">
        <section id="menuPrincipal" className="card-finalizacao-conteudo">
          <h1>Parabéns!</h1>
          <h2>Atividade chegou ao fim!</h2>
          
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
        </section>

        <button 
          id="verificarBotao" 
          onClick={() => navigate('/')}
        >
          Sair
        </button>

      </div>
    );
  }

  const atividadeAtual = atividades[indiceAtual];
  const respostaCorreta = atividadeAtual.alternativas[0];

  const handleDica = () => {
    if (usouDica || verificado) return;
    
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
        <button 
          id="verificarBotao" 
          onClick={handleVerificar}
          disabled={!selecionada}
        >
          Verificar
        </button>
      ) : (
        <button 
          id="verificarBotao" 
          onClick={handleProxima}
          style={{ backgroundColor: '#28a745', color: '#fff' }}
        >
          {indiceAtual + 1 === atividades.length ? 'Finalizar' : 'Próxima'}
        </button>
      )}
    </div>
  );
}