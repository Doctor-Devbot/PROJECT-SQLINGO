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
      <button className="btn-global" onClick={() => navigate('/jogadores')}>
        Jogadores
      </button>
      <button className="btn-global" onClick={() => navigate('/login')}>
        Login
      </button>
    </nav>
  );
}
