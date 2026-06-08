# Local AI CLI Launcher 🚀

O **Local AI CLI Launcher** é um orquestrador leve e universal projetado para quem trabalha com múltiplos LLMs locais. Ele detecta seu sistema operacional automaticamente e oferece um menu interativo para lançar o **Claude Code**, **Codex**, **Gemini** ou **LM Studio** com um único comando.

---

## 📋 Pré-requisitos

Antes de começar, você precisará de:
1. **Python 3.8+** instalado.
2. As ferramentas de CLI que deseja usar já instaladas no seu sistema:
   - [Claude Code](https://github.com/anthropics/claude-code) (`npm install -g @anthropic-ai/claude-code`)
   - [LM Studio](https://lmstudio.ai/) (com o CLI `lms` habilitado)
   - [Ollama](https://ollama.com/) (opcional, para modelos locais)

---

## 🚀 Instalação Rápida

### 1. Preparar o Repositório
```bash
git clone https://github.com/seu-usuario/cli-ai-local.git
cd cli-ai-local
```

### 2. Configuração Automática
Execute o script de setup para configurar dependências, arquivo `.env` e permissões:
```bash
python setup.py
```
*(No Linux/macOS, use `python3 setup.py`)*

### 3. Execução
Após o setup, basta iniciar o orquestrador:
```bash
python launcher.py
```

### 2. O que acontece em cada opção?

#### 🟦 Opção 1: Claude Code
Lança o CLI do Claude configurado para usar o seu provedor local (LM Studio ou Ollama).
- **Exemplo de uso interno:** Ele define automaticamente `ANTHROPIC_BASE_URL` para o seu servidor local antes de abrir o Claude.

#### 🟩 Opção 2: Codex OpenAI
Lança a interface do Codex. Ideal para quem usa modelos focados em código que seguem o padrão OpenAI.

#### 🟨 Opção 3: Gemini CLI
Abre o terminal do Gemini. Se você passar argumentos extras, eles serão repassados:
```bash
# O launcher permite selecionar e rodar:
python launcher.py  -> Escolha [3]
```

#### ⬜ Opção 4: LM Studio (Direct)
Esta opção é um atalho completo. Ela:
1. Descarrega qualquer modelo anterior do LM Studio.
2. Carrega o modelo especificado (ex: Qwen 2.5) com 32k de contexto.
3. Inicia o servidor e abre o Claude Code apontando para ele.

---

## ⚙️ Customização (.env)

Você pode mudar o comportamento e configurar os **modelos de IA** sem mexer no código editando o arquivo `.env`:

```ini
# --- Claude Code / LM Studio ---
# Define o modelo local/remoto que o Claude Code irá carregar/consumir
CLAUDE_MODEL=gpt-oss:20b
# URL base para a API (ex: http://localhost:11434 para usar com Ollama)
ANTHROPIC_BASE_URL=http://localhost:1234
# Token de autorização fictício para o provedor local
ANTHROPIC_AUTH_TOKEN=lmstudio

# --- Gemini CLI ---
# Define o modelo usado pelo Gemini CLI
GEMINI_MODEL=gemini-2.0-flash

# --- Codex ---
# Define o modelo usado pelo Codex CLI
CODEX_MODEL=gpt-oss:20b
```

---

## 🛠️ Solução de Problemas

- **"Comando não encontrado"**: Certifique-se de que o `claude` ou `lms` está no seu PATH (consegue rodar eles sozinhos no terminal?).
- **Erro de Permissão (Linux/macOS)**: Lembre-se de rodar `chmod +x scripts/*.sh`.
- **PowerShell (Erro de Execução)**: Se o Windows bloquear os scripts, rode: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.

## 🐧 Linux & 🍎 macOS

As versões para **Linux** e **macOS** foram estruturadas no código, mas **ainda não foram testadas**. Se você utiliza um desses sistemas operacionais, testar o launcher e puder contribuir com feedbacks ou correções, por favor entre em contato ou abra uma issue/pull request!

---
Desenvolvido por Douglas Feltrim para simplificar sua jornada com IA Local.

