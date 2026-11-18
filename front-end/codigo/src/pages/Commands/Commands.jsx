import './Commands.css';

export default function Commands() {
  const comandosDML = ["SELECT", "INSERT", "UPDATE"];
  const comandosDDL = ["ALTER", "CREATE", "DROP"];

  const renderSection = (titulo, lista) => (
    <div className="secao-comandos">
      <h1>{titulo}</h1>
      <ul>
        {lista.map((comando, index) => (
          <li key={index}>
            <button className="btn-comando">{comando}</button>
          </li>
        ))}
      </ul>
    </div>
  );

  return (
    <section id="comandos">
      {renderSection("Comandos de Manipulação de Dados", comandosDML)}
      {renderSection("Comandos de Definição de Dados", comandosDDL)}
    </section>
  );
}