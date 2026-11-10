import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css';

export default function Home() {
  const navigate = useNavigate();
  const [modulos, setModulos] = useState([]);
  const [listasAtividade, setListasAtividade] = useState([]);
  const [erro, setErro] = useState(null);

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
        console.log("MÓDULOS RECEBIDOS:", dadosModulos);
        console.log("LISTAS RECEBIDAS:", dadosListas);
        setModulos(dadosModulos);
        setListasAtividade(dadosListas);
      })
      .catch((err) => {
        console.error(err);
        setErro('Não foi possível carregar os dados da página.');
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
                    <button
                      key={lista.id}
                      className="btn-circulo"
                      onClick={() => navigate(`/atividade`)} // Poderia ser `/atividade/${lista.id}` se quiser especificar
                      title={lista.titulo} // Mostra o título da lista ao passar o mouse
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