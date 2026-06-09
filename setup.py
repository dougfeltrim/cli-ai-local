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

    # 2. Instalar dependencias (se houver)
    print("\n[2/5] Instalando dependencias do requirements.txt...")
    if os.path.exists("requirements.txt"):
        if run_command(f"{sys.executable} -m pip install -r requirements.txt"):
            print("Dependencias instaladas com sucesso.")
        else:
            print("Aviso: Falha ao instalar dependencias ou requirements.txt esta vazio.")
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
        "codex": ("Codex CLI", "Instale a CLI do Codex (codex)")
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
    print("\nPara iniciar a aplicacao, use:")
    if platform.system().lower() == "windows":
        print("python launcher.py")
    else:
        print("python3 launcher.py")
    print("=============================================")

if __name__ == "__main__":
    main()
