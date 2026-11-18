// =============================================================================
// services/api.js - Camada de acesso à API Flask do SQLINGO
//
// Em desenvolvimento local a API roda em http://localhost:5000 (Flask dev).
// Quando a API for publicada na nuvem (Render), crie um arquivo .env na pasta
// front-end/codigo com a variável:
//   VITE_API_URL=https://sqlingo.onrender.com
// Assim o front-end passa a consumir a API na nuvem sem alterar o código.
// =============================================================================

export const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

// ---------------------------------------------------------------------------
// Autenticação (POST /login) - retorna { message, access_token }
// ---------------------------------------------------------------------------
export async function login(email, senha) {
  const resposta = await fetch(`${API_BASE_URL}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, senha }),
  });

  if (!resposta.ok) {
    let mensagem = 'Falha ao comunicar com o servidor.';
    try {
      const dados = await resposta.json();
      mensagem = dados.erro || mensagem;
    } catch {
      // resposta sem corpo JSON
    }
    const erro = new Error(mensagem);
    erro.status = resposta.status;
    throw erro;
  }

  return resposta.json();
}

// ---------------------------------------------------------------------------
// Paginação de jogadores (GET /jogador/paginacao?pag=X&por_pagina=Y)
// Retorna { items, page, total_pages, has_prev, has_next, prev_num, next_num }
// Cada item inclui a lista "atividades_ids" do relacionamento N:N.
// ---------------------------------------------------------------------------
export async function buscarJogadoresPaginacao(pag, porPagina) {
  const resposta = await fetch(
    `${API_BASE_URL}/jogador/paginacao?pag=${pag}&por_pagina=${porPagina}`
  );

  if (!resposta.ok) {
    let mensagem = 'Falha ao carregar os jogadores.';
    try {
      const dados = await resposta.json();
      mensagem = dados.erro || mensagem;
    } catch {
      // resposta sem corpo JSON
    }
    const erro = new Error(mensagem);
    erro.status = resposta.status;
    throw erro;
  }

  return resposta.json();
}

// ---------------------------------------------------------------------------
// Utilitários
// ---------------------------------------------------------------------------
export function obterToken() {
  return localStorage.getItem('access_token');
}

export function salvarToken(token) {
  localStorage.setItem('access_token', token);
}

export function limparToken() {
  localStorage.removeItem('access_token');
}

export function urlApi(caminho) {
  // Monta a URL completa de um endpoint da API (usado pelas demais telas)
  return `${API_BASE_URL}${caminho}`;
}
