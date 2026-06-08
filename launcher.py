import os
import sys
import subprocess
import platform

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_os_type():
    os_name = platform.system().lower()
    if os_name == 'windows':
        return 'win'
    elif os_name == 'linux' or os_name == 'darwin': # Darwin is macOS
        return 'unix'
    else:
        return 'unknown'

def load_env():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(base_dir, '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    key, val = line.split('=', 1)
                    key = key.strip()
                    val = val.strip()
                    # Remove surrounding quotes if present
                    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                        val = val[1:-1]
                    os.environ[key] = val

def main():
    load_env()
    clear_screen()
    print("=============================================")
    print("             CLI Local AI Launcher           ")
    print("=============================================")
    
    os_type = get_os_type()
    if os_type == 'unknown':
        print(f"Unsupported OS: {platform.system()}")
        sys.exit(1)

    print(f"Detected OS: {platform.system()}")
    print("\nSelect LLM Provider:")
    print("  [1] Claude Code")
    print("  [2] Codex OpenAI")
    print("  [3] Gemini CLI")
    print("  [4] LM Studio (Direct)")
    print("  [Q] Quit")
    print("")

    choice = input("Choose option [1-4, Q]: ").strip().upper()

    if choice == 'Q':
        print("Exiting...")
        sys.exit(0)

    # Map choices to script names
    provider_map = {
        '1': 'claude',
        '2': 'codex',
        '3': 'gemini',
        '4': 'lmstudio'
    }

    if choice not in provider_map:
        print("Invalid choice.")
        sys.exit(1)

    provider = provider_map[choice]
    
    # Determine script extension based on OS
    ext = 'ps1' if os_type == 'win' else 'sh'
    script_name = f"start-{provider}.{ext}"
    
    # Path to scripts inside cli-ai-local/scripts
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, 'scripts', script_name)
    
    # Fallback checks (para quando o usuário roda fora da estrutura esperada)
    if not os.path.exists(script_path):
        # Tenta na pasta scripts/ no mesmo nível do launcher
        fallback_path = os.path.join(os.getcwd(), 'scripts', script_name)
        if os.path.exists(fallback_path):
            script_path = fallback_path
        else:
            print(f"Erro: Script {script_name} não encontrado em {script_path}")
            sys.exit(1)

    print(f"Launching {provider} using {script_path}...")

    try:
        if os_type == 'win':
            # Use PowerShell to run the .ps1 script
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path], check=True)
        else:
            # Use Bash to run the .sh script
            subprocess.run(["bash", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
