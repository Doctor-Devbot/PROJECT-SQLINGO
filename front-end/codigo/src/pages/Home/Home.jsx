import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css';

export default function Home() {
  const navigate = useNavigate();
  const [atividades, setAtividades] = useState([]);
  const [erro, setErro] = useState(null);

  useEffect(() => {
    // Faz a requisição para o back-end Flask para buscar as atividades cadastradas
    // Lembre-se de ajustar a URL conforme o prefixo da sua rota no Flask
    fetch('http://localhost:5000/atividade') // ou '/api/atividades' dependendo do seu blueprint
      .then((res) => {
        if (!res.ok) throw new Error('Erro ao carregar as atividades');
        return res.json();
      })
      .then((data) => {
        console.log("DADOS RECEBIDOS DO FLASK:", data); // <--- OLHE ISSO AQUI NO CONSOLE
        setAtividades(data);
      })
      .catch((err) => {
        console.error(err);
        setErro('Não foi possível carregar os módulos.');
      });
  }, []);

  return (
    <section id="caminhoPrincipal">
      <h1>1- Introdução</h1>
      
      {erro && <p style={{ color: 'red' }}>{erro}</p>}

      {/* Renderiza os botões dinamicamente com base no banco de dados */}
      <div className="botoes-container">
        {atividades.length > 0 ? (
          atividades.map((atividade, index) => (
            <button 
              key={atividade.id || index} 
              className="btn-circulo" 
              onClick={() => navigate(`/atividade`)} // Você pode passar o ID se precisar: `/atividade/${atividade.id}`
            >
              {index + 1}
            </button>
          ))
        ) : (
          // Caso a API demore ou não retorne nada, mantém um comportamento padrão
          <>
            <button className="btn-circulo" onClick={() => navigate('/atividade')}>
              1
            </button>
            <button className="btn-circulo" onClick={() => navigate('/atividade')}>
              2
            </button>
          </>
        )}
      </div>
    </section>
  );
}