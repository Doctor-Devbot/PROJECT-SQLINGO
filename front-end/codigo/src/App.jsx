import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout/Layout';
import Home from './pages/Home/Home';
import Commands from './pages/Commands/Commands';
import Activity from './pages/Activity/Activity';
import Login from './pages/Login/Login';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Tela de login é uma rota isolada, sem a Sidebar/Layout */}
        <Route path="/login" element={<Login />} />

        {/* Rotas internas com a Sidebar */}
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="comandos" element={<Commands />} />
          <Route path="/atividade/:idLista" element={<Activity />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;