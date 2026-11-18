import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';
import logo from '../../assets/images/logoSQLingo2.png';
import { login, salvarToken } from '../../services/api';

export default function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [lembrar, setLembrar] = useState(false);
  const [mostrarSenha, setMostrarSenha] = useState(false);
  const [erro, setErro] = useState(null);
  const [carregando, setCarregando] = useState(false);

  const handleSubmit = async (e) => {
    // Integração com o back-end: POST /login da classe Jogador
    e.preventDefault();
    setErro(null);

    if (!email || !senha) {
      setErro('Preencha o e-mail e a senha para entrar.');
      return;
    }

    try {
      setCarregando(true);
      const dados = await login(email, senha);

      // Guarda o token JWT retornado pela API (Authorization: Bearer)
      salvarToken(dados.access_token);

      navigate('/');
    } catch (errApi) {
      // 401 -> e-mail ou senha inválidos (resposta da API)
      setErro(errApi.message || 'Não foi possível entrar. Tente novamente.');
    } finally {
      setCarregando(false);
    }
  };

  return (
    <div className="login-page">
      {/* Painel lateral com a marca */}
      <aside className="login-painel-lateral">
        <img src={logo} alt="Logo SQLingo" className="login-logo-grande" />
        <h2 className="login-painel-titulo">Aprenda SQL jogando</h2>
        <p className="login-painel-texto">
          Pratique comandos, avance nas listas de atividades e evolua suas
          habilidades em banco de dados de forma divertida.
        </p>
        <span className="login-painel-rodape">SQLingo · Plataforma educacional</span>
      </aside>

      {/* Formulário de login */}
      <main className="login-form-wrapper">
        <section className="login-card">
          <h1>Entrar</h1>

          {/* Mensagem de erro devolvida pela API (ex.: 401 e-mail/senha) */}
          {erro && <p className="login-erro">{erro}</p>}

          <form className="login-form" onSubmit={handleSubmit}>
            <label className="login-label" htmlFor="email">
              E-mail
            </label>
            <input
              id="email"
              className="login-input"
              type="email"
              placeholder="seu@email.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              autoComplete="email"
            />

            <label className="login-label" htmlFor="senha">
              Senha
            </label>
            <div className="login-senha-wrapper">
              <input
                id="senha"
                className="login-input"
                type={mostrarSenha ? 'text' : 'password'}
                placeholder="Digite sua senha"
                value={senha}
                onChange={(e) => setSenha(e.target.value)}
                autoComplete="current-password"
              />
              <button
                type="button"
                className="login-senha-toggle"
                onClick={() => setMostrarSenha((s) => !s)}
                aria-label={mostrarSenha ? 'Ocultar senha' : 'Mostrar senha'}
              >
                {mostrarSenha ? 'Ocultar' : 'Mostrar'}
              </button>
            </div>

            <div className="login-opcoes">
              <label className="login-checkbox">
                <input
                  type="checkbox"
                  checked={lembrar}
                  onChange={(e) => setLembrar(e.target.checked)}
                />
                <span>Lembrar minha senha</span>
              </label>

              <a href="#" className="login-link" onClick={(e) => e.preventDefault()}>
                Esqueci a senha
              </a>
            </div>

            <button
              type="submit"
              className="btn-global login-btn-entrar"
              disabled={carregando}
            >
              {carregando ? 'Entrando...' : 'Entrar'}
            </button>
          </form>

          <div className="login-divisor">
            <span>ou</span>
          </div>

          <p className="login-cadastro">
            Não tem conta?{' '}
            <a
              href="#"
              className="login-link login-link-destaque"
              onClick={(e) => e.preventDefault()}
            >
              Cadastre-se
            </a>
          </p>
        </section>
      </main>
    </div>
  );
}
