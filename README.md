# Steamlit-test – Quick Start Guide

Transforme o repositório em um app local que usa llms via **Ollama** e ferramentas MCP.

---

## Pré‑requisitos

| Ferramenta          | Versão recomendada | Como instalar                                                                 |          |
| ------------------- | ------------------ | ----------------------------------------------------------------------------- | -------- |
| **Python**          | ≥ 3.10             | [https://python.org](https://python.org)                                      |          |
| **Git**             | qualquer           | [https://git-scm.com](https://git-scm.com)                                    |          |
| **Ollama**          | 0.1.32 ou maior    | \`\`\`curl -fsSL [https://ollama.ai/install.sh](https://ollama.ai/install.sh) | sh\`\`\` |
| **Poetry** ou `pip` | opcional           | para instalar dependências                                                    |          |

> **Windows** / **macOS**: baixe o instalador gráfico em [https://ollama.ai](https://ollama.ai).

# Tutorial Linux:
---

## 1 ▪ Baixe o modelo qwen3:1.7b

```bash
ollama pull qwen3:1.7b
```

Esperado: download de \~4 GB; uma vez concluído o modelo fica disponível localmente em `~/.ollama`.

---

## 2 ▪ Clone o repositório e instale dependências

```bash
git clone https://github.com/Hughboss432/automato-reactagent.git
cd seu‑repo
make install
```

---

## 3 ▪ Execute a aplicação Streamlit

Use o seguinte comando para rodar o server local:

```bash
make run
```

Streamlit imprimirá algo como:

```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
```

Acesse o link no navegador. Pronto! O chat usará o modelo escolhido local e chamará as ferramentas servidas pelo MCP.

---

## Licença

MIT License
