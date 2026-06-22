import os
import sys
import subprocess
import platform
import shutil

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("=============================================")
    print("      Local AI CLI Launcher - SETUP")
    print("=============================================")

    # 1. Verificar Python
    print("\n[1/5] Verificando ambiente Python...")
    print(f"Versao: {platform.python_version()}")

    # 2. Criar ambiente virtual e instalar dependencias
    print("\n[2/5] Configurando ambiente virtual e dependencias...")
    is_win = platform.system().lower() == "windows"
    venv_dir = os.path.join(os.getcwd(), ".venv")
    
    if not os.path.exists(venv_dir):
        print("Criando ambiente virtual (.venv)...")
        try:
            subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
            print("Ambiente virtual criado com sucesso.")
        except Exception as e:
            print(f"Erro ao criar ambiente virtual: {e}")
            sys.exit(1)
    else:
        print("Ambiente virtual (.venv) ja existe.")

    # Definir interpretador do ambiente virtual
    if is_win:
        venv_python = os.path.join(venv_dir, "Scripts", "python.exe")
    else:
        venv_python = os.path.join(venv_dir, "bin", "python")

    if os.path.exists("requirements.txt"):
        print("Instalando dependencias do requirements.txt no ambiente virtual...")
        # Atualiza o pip do venv primeiro
        run_command(f'"{venv_python}" -m pip install --upgrade pip')
        if run_command(f'"{venv_python}" -m pip install -r requirements.txt'):
            print("Dependencias instaladas com sucesso no .venv.")
        else:
            print("Aviso: Falha ao instalar dependencias no .venv.")
            
        # Instalar o próprio pacote em modo editável para registrar o comando
        print("Registrando o launcher como comando local (cli-ai)...")
        if run_command(f'"{venv_python}" -m pip install -e .'):
            print("Comando 'cli-ai' registrado com sucesso no .venv.")
    else:
        print("Arquivo requirements.txt nao encontrado. Pulando...")

    # 3. Configurar .env
    print("\n[3/5] Configurando arquivo .env...")
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            shutil.copy(".env.example", ".env")
            print("Arquivo .env criado a partir do .env.example.")
            print("DICA: Edite o arquivo .env se precisar mudar URLs ou chaves.")
        else:
            print("Erro: .env.example nao encontrado para criar o .env.")
    else:
        print("Arquivo .env ja existe. Pulando copia.")

    # 4. Permissoes de Script (Unix)
    if platform.system().lower() != "windows":
        print("\n[4/5] Configurando permissoes de execucao (Unix)...")
        scripts_dir = "scripts"
        if os.path.exists(scripts_dir):
            run_command(f"chmod +x {scripts_dir}/*.sh")
            print("Permissoes concedidas aos scripts .sh.")
        else:
            print(f"Aviso: Pasta {scripts_dir} nao encontrada.")
    else:
        print("\n[4/5] Ambiente Windows detectado. Permissoes de script nao sao necessarias.")

    # 5. Verificar ferramentas de IA
    print("\n[5/5] Verificando se as ferramentas de IA estao instaladas no PATH...")
    tools = {
        "claude": ("Claude Code", "npm install -g @anthropic-ai/claude-code"),
        "lms": ("LM Studio CLI", "Habilite a CLI nas configuracoes do LM Studio"),
        "gemini": ("Gemini CLI", "Instale a CLI oficial do Gemini (gemini)"),
        "codex": ("Codex CLI", "Instale a CLI do Codex (codex)"),
        "hermes": ("Hermes Agent", "Execute: iex (irm https://hermes-agent.nousresearch.com/install.ps1) no Windows")
    }
    for cmd, (name, install_hint) in tools.items():
        if shutil.which(cmd) is not None:
            print(f"  [OK] {name} ({cmd}): Instalado")
        else:
            print(f"  [X] {name} ({cmd}): Nao encontrado no PATH")
            print(f"      Dica de instalacao: {install_hint}")

    print("\n=============================================")
    print("        CONFIGURACAO CONCLUIDA!")
    print("=============================================")
    print("\nPara iniciar a aplicacao no diretorio do projeto, use:")
    if platform.system().lower() == "windows":
        print("  .venv\\Scripts\\cli-ai  (ou python launcher.py)")
    else:
        print("  .venv/bin/cli-ai       (ou python3 launcher.py)")
    print("\nSe desejar instalar globalmente para rodar de QUALQUER terminal, execute:")
    print("  pip install --user -e .")
    print("  (Isso disponibilizara o comando 'cli-ai' ou 'cli-ai-local' globalmente)")
    print("=============================================")

if __name__ == "__main__":
    main()
