<div align="center">
  <h1>🚀 Local AI CLI Launcher</h1>
  
  <p><b>Um orquestrador que unifica suas ferramentas de IA em um menu interativo para facilitar o início de agentes de codificação usando suas LLMs locais.</b></p>

  <!-- Badges -->
  <p>
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python" alt="Python 3.8+">
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License MIT">
    <img src="https://img.shields.io/badge/Status-Beta-yellow?style=flat-square" alt="Status Beta">
    <img src="https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square" alt="Platforms">
  </p>

  <p>
    <a href="#-o-que-é">O que é</a> •
    <a href="#-por-que-usar">Por que usar</a> •
    <a href="#-pré-requisitos">Pré-requisitos</a> •
    <a href="#-instalação">Instalação</a> •
    <a href="#-como-usar">Como usar</a> •
    <a href="#-configuração-avançada">Configuração</a>
  </p>
</div>

---

## 🎯 O que é?

O **Local AI CLI Launcher** é uma aplicação projetada para centralizar e facilitar o lançamento de diversos agentes de codificação baseados em IA. Ele elimina a necessidade de configurações manuais repetitivas, oferecendo:

- 🎛️ **Menu unificado** para lançar Claude Code, Codex, Gemini, LM Studio e Hermes Agent.
- 🔄 **Configuração automática** de variáveis de ambiente.
- ⚙️ **Customização total** via arquivo `.env`.
- 🛡️ **Privacidade** – execute seus modelos e agentes totalmente de forma local.

---

## 💡 Por que usar?

### Antes (Sem o Launcher) 😫
Você precisa lembrar e digitar comandos manualmente toda vez:
```bash
export ANTHROPIC_BASE_URL=http://localhost:1234
export ANTHROPIC_AUTH_TOKEN=seu-token
lms start --port 1234
# ... aguardar o carregamento ...
claude code --base-url http://localhost:1234
```

### Depois (Com o Launcher) 🤩
Um único comando resolve tudo:
```bash
python launcher.py
```
*→ O menu interativo é aberto*  
*→ Você seleciona a ferramenta desejada*  
*→ Tudo é configurado e iniciado automaticamente! ✨*

> **Dica:** Aqui você pode adicionar um GIF ou screenshot do menu em funcionamento no futuro!  
> `![Demo do Launcher](caminho/para/o/gif.gif)`

---

## 🔧 Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

| Ferramenta | Status | Como Instalar / Obter |
|:---|:---:|:---|
| **Python 3.8+** | Obrigatório | [python.org](https://python.org) |
| **Claude Code** | Obrigatório | `npm install -g @anthropic-ai/claude-code` |
| **LM Studio** | Recomendado | [lmstudio.ai](https://lmstudio.ai) |
| **Hermes Agent** | Opcional | https://github.com/nousresearch/hermes-agent |
| **Gemini CLI** | Opcional | `npm install -g @google/gemini-cli` |
| **Ollama** | Opcional | [ollama.com](https://ollama.com) |

### 🔍 Verificar Instalação
```bash
python --version          # ✓ Python 3.8+
claude --version          # ✓ Claude Code
lms --version             # ✓ LM Studio (se usar)
gemini --version          # ✓ Gemini CLI (se usar)
hermes --version          # ✓ Hermes Agent (se usar)
```

---

## 📦 Instalação

**1. Clone o repositório:**
```bash
git clone https://github.com/dougfeltrim/cli-ai-local.git
cd cli-ai-local
```

**2. Execute o script de Setup:**  
Este script instalará dependências, criará seu arquivo `.env` padrão e ajustará permissões.
```bash
# No Windows
python setup.py

# No Linux/macOS
python3 setup.py
```

**3. Inicie o Launcher!**
```bash
python launcher.py
```

Você verá o menu interativo:
```text
╔═══════════════════════════════════╗
║  Local AI CLI Launcher v1.0       ║
╚═══════════════════════════════════╝

Escolha uma opção:
[1] Claude Code + LM Studio Local
[2] Codex OpenAI
[3] Gemini CLI
[4] LM Studio (Direct)
[5] Hermes Agent
[0] Sair

→ Digite a opção:
```

---

## 🚀 Como Usar

### `[1]` Claude Code + LM Studio Local
Abre o **Claude Code** já configurado para utilizar um modelo local hospedado no LM Studio.
- **Ideal para:** Máxima privacidade, uso de modelos locais (Qwen, Llama, Mistral) e independência de APIs externas.
- **Como funciona:** Define automaticamente `ANTHROPIC_BASE_URL` e `CLAUDE_MODEL` a partir do seu `.env`.

### `[2]` Codex OpenAI
Inicia a interface do **Codex** configurada para modelos compatíveis com a API da OpenAI.
- **Ideal para:** Utilizar modelos mais robustos via API (como GPT-4o ou Claude 3.5 Sonnet através de proxies).
- **Como funciona:** Carrega o modelo de `CODEX_MODEL` e repassa argumentos adicionais nativamente.

### `[3]` Gemini CLI
Inicia o **terminal do Gemini** para interações diretas com os modelos do Google.
- **Ideal para:** Interações multimodais e uso do ecossistema Google no terminal.
- **Como funciona:** Inicia a sessão interativa com o modelo definido em `GEMINI_MODEL`.

### `[4]` LM Studio (Direct)
Gerenciamento rápido do LM Studio direto do terminal.
- **Ideal para:** Trocas rápidas de modelos e setup automático "mão na roda".
- **Como funciona:** Descarrega modelos antigos, carrega o novo `CLAUDE_MODEL`, inicia o servidor em background e já abre o Claude Code vinculado a ele.

### `[5]` Hermes Agent
Inicia o **Hermes Agent**, um agente autônomo com recursos avançados.
- **Ideal para:** Uso de ferramentas avançadas, agentes locais robustos criados pela Nous Research.
- **Como funciona:** Inicia a interface do `hermes` e repassa o `HERMES_MODEL` se definido.

---

## ⚙️ Configuração Avançada

Todo o controle está no seu arquivo `.env` (criado durante o `setup.py`).

<details>
<summary><strong>Ver variáveis disponíveis no .env</strong></summary>

```env
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Claude Code / LM Studio
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLAUDE_MODEL=qwen2.5:32b
ANTHROPIC_BASE_URL=http://localhost:1234
ANTHROPIC_AUTH_TOKEN=lmstudio

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Gemini CLI
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GEMINI_MODEL=gemini-2.0-flash

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Codex OpenAI
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CODEX_MODEL=gpt-oss:20b
```
</details>

<details>
<summary><strong>Exemplo: Ollama + Claude Code</strong></summary>

Se você prefere o Ollama ao invés do LM Studio:
```env
CLAUDE_MODEL=neural-chat:7b
ANTHROPIC_BASE_URL=http://localhost:11434
ANTHROPIC_AUTH_TOKEN=ollama
```
</details>

---

## 🛠️ Solução de Problemas

- **Comando não encontrado (`claude`, `lms`, `gemini`)**  
  As ferramentas não estão no `PATH`. Reinstale as dependências via NPM e reinicie seu terminal.
- **Erro de Permissão (Linux/macOS)**  
  Execute `chmod +x scripts/*.sh` e `chmod +x launcher.py`.
- **PowerShell não executa o script (Windows)**  
  Abra o PowerShell como Administrador e rode: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.
- **Porta 1234 já em uso (LM Studio)**  
  Feche o servidor ativo do LM Studio ou mate o processo (`netstat -ano | findstr :1234` no Windows).

---

## 📊 Compatibilidade e Testes

| Ferramenta | Windows | Linux | macOS |
|:---|:---:|:---:|:---:|
| **Claude Code** | ✅ | ⚠️ | ⚠️ |
| **LM Studio** | ✅ | ⚠️ | ⚠️ |
| **Gemini CLI** | ⚠️ | ⚠️ | ⚠️ |
| **Codex OpenAI** | ✅ | ⚠️ | ⚠️ |
| **Hermes Agent** | ✅ | ⚠️ | ⚠️ |

*(✅ Testado e funcionando | ⚠️ Estrutura pronta, necessita de feedback)*

**Usa Linux ou macOS?** Teste a ferramenta e [abra uma Issue](https://github.com/dougfeltrim/cli-ai-local/issues) com os resultados!

---

## 🤝 Como Contribuir

1. Faça um **Fork** do projeto.
2. Crie uma branch para sua modificação (`git checkout -b feature/sua-feature`).
3. Faça o commit (`git commit -m 'Add: nova funcionalidade incrivel'`).
4. Faça o push (`git push origin feature/sua-feature`).
5. Abra um **Pull Request**.

Melhorias em testes para Linux/macOS e suporte a novos agentes são muito bem-vindas!

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

<div align="center">
  <br>
  <b>Douglas Feltrim</b><br>
  <a href="https://github.com/dougfeltrim">GitHub</a> • <a href="https://www.linkedin.com/in/douglas-feltrim/">LinkedIn</a>
  <br><br>
  <i>Desenvolvido para simplificar sua jornada com IA local.</i><br>
  Se o projeto foi útil, deixe uma estrela ⭐
</div>