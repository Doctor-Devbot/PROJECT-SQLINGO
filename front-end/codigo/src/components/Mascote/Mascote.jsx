import './Mascote.css';

/**
 * Mascote do SQLingo: um banco de dados animado.
 * Todas as cores vêm das variáveis CSS da paleta ativa,
 * então ele muda de roupa junto com o tema do site.
 */
export default function Mascote({ className = '' }) {
  return (
    <svg
      viewBox="0 0 240 260"
      className={`mascote ${className}`.trim()}
      role="img"
      aria-label="Mascote do SQLingo, um banco de dados sorridente"
    >
      {/* Sombra no chão */}
      <ellipse className="mascote-sombra" cx="120" cy="248" rx="62" ry="10" />

      {/* Pés */}
      <ellipse className="mascote-pe" cx="92" cy="233" rx="17" ry="9" />
      <ellipse className="mascote-pe" cx="148" cy="233" rx="17" ry="9" />

      {/* Braço direito acenando */}
      <g className="mascote-braco braco-acenando">
        <rect className="mascote-braco-forma" x="176" y="118" width="34" height="15" rx="7.5" />
        <circle className="mascote-mao" cx="212" cy="114" r="11" />
      </g>

      {/* Braço esquerdo */}
      <g className="mascote-braco">
        <rect className="mascote-braco-forma" x="30" y="140" width="32" height="15" rx="7.5" />
        <circle className="mascote-mao" cx="28" cy="147" r="10" />
      </g>

      {/* Corpo: cilindro de banco de dados */}
      <path
        className="mascote-corpo"
        d="M55 70 v118 c0 12.2 29.1 22 65 22 s65 -9.8 65 -22 V70 Z"
      />

      {/* Linhas das "pilhas" de dados */}
      <path
        className="mascote-linha"
        d="M55 118 c0 12.2 29.1 22 65 22 s65 -9.8 65 -22"
      />
      <path
        className="mascote-linha"
        d="M55 162 c0 12.2 29.1 22 65 22 s65 -9.8 65 -22"
      />

      {/* Tampa superior do cilindro */}
      <ellipse className="mascote-tampa" cx="120" cy="70" rx="65" ry="22" />

      {/* Rosto */}
      <g className="mascote-rosto">
        {/* Olhos */}
        <g className="mascote-olho olho-esquerdo">
          <circle className="olho-branco" cx="99" cy="108" r="13" />
          <circle className="olho-pupila" cx="102" cy="110" r="5.5" />
          <circle className="olho-brilho" cx="105.5" cy="106" r="2.2" />
        </g>
        <g className="mascote-olho olho-direito">
          <circle className="olho-branco" cx="141" cy="108" r="13" />
          <circle className="olho-pupila" cx="144" cy="110" r="5.5" />
          <circle className="olho-brilho" cx="147.5" cy="106" r="2.2" />
        </g>

        {/* Sorriso */}
        <path
          className="mascote-sorriso"
          d="M104 130 q16 14 32 0"
        />

        {/* Bochechas */}
        <ellipse className="mascote-bochecha" cx="86" cy="126" rx="7" ry="5" />
        <ellipse className="mascote-bochecha" cx="154" cy="126" rx="7" ry="5" />
      </g>

      {/* Brilho decorativo */}
      <g className="mascote-brilho" aria-hidden="true">
        <path className="estrela estrela-1" d="M28 52 l2.6 6.4 6.4 2.6 -6.4 2.6 -2.6 6.4 -2.6 -6.4 -6.4 -2.6 6.4 -2.6 Z" />
        <path className="estrela estrela-2" d="M212 66 l2 4.9 4.9 2 -4.9 2 -2 4.9 -2 -4.9 -4.9 -2 4.9 -2 Z" />
      </g>
    </svg>
  );
}
