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
    print(f"\n[1/4] Verificando ambiente Python...")
    print(f"Versão: {platform.python_version()}")

    # 2. Instalar dependências (se houver)
    print(f"\n[2/4] Instalando dependências do requirements.txt...")
    if os.path.exists("requirements.txt"):
        if run_command(f"{sys.executable} -m pip install -r requirements.txt"):
            print("Dependências instaladas com sucesso.")
        else:
            print("Aviso: Falha ao instalar dependências ou requirements.txt está vazio.")
    else:
        print("Arquivo requirements.txt não encontrado. Pulando...")

    # 3. Configurar .env
    print(f"\n[3/4] Configurando arquivo .env...")
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            shutil.copy(".env.example", ".env")
            print("Arquivo .env criado a partir do .env.example.")
            print("DICA: Edite o arquivo .env se precisar mudar URLs ou chaves.")
        else:
            print("Erro: .env.example não encontrado para criar o .env.")
    else:
        print("Arquivo .env já existe. Pulando cópia.")

    # 4. Permissões de Script (Unix)
    if platform.system().lower() != "windows":
        print(f"\n[4/4] Configurando permissões de execução (Unix)...")
        scripts_dir = "scripts"
        if os.path.exists(scripts_dir):
            run_command(f"chmod +x {scripts_dir}/*.sh")
            print("Permissões concedidas aos scripts .sh.")
        else:
            print(f"Aviso: Pasta {scripts_dir} não encontrada.")
    else:
        print(f"\n[4/4] Ambiente Windows detectado. Permissões de script não são necessárias.")

    print("\n=============================================")
    print("        CONFIGURAÇÃO CONCLUÍDA! 🎉")
    print("=============================================")
    print("\nPara iniciar a aplicação, use:")
    if platform.system().lower() == "windows":
        print("python launcher.py")
    else:
        print("python3 launcher.py")
    print("=============================================")

if __name__ == "__main__":
    main()
