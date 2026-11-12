import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout/Layout';
import Home from './pages/Home/Home';
import Commands from './pages/Commands/Commands';
import Activity from './pages/Activity/Activity';

function App() {
  return (
    <BrowserRouter>
      <Routes>
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