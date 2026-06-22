import os
import sys
import subprocess
import platform
import shutil
import json

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich import box
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

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
                    
                    # Handle end of line comments
                    if '#' in val:
                        # Check if quoted
                        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                            pass
                        elif (val.startswith('"') and '"' in val[1:]) or (val.startswith("'") and "'" in val[1:]):
                            q_char = val[0]
                            closing_idx = val.find(q_char, 1)
                            if closing_idx != -1:
                                val = val[:closing_idx + 1].strip()
                        else:
                            val = val.split('#', 1)[0].strip()
                            
                    # Remove surrounding quotes if present
                    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                        val = val[1:-1]
                    os.environ[key] = val

def get_local_models():
    """Returns a list of local LLM models using lms ls --json."""
    if not shutil.which("lms"):
        return []
    try:
        result = subprocess.run(["lms", "ls", "--json"], capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        # Filter only type="llm"
        models = [item['modelKey'] for item in data if item.get('type') == 'llm']
        return models
    except Exception:
        return []

def select_model(provider_name):
    models = get_local_models()
    if not models:
        return None  # No models found, rely on default

    if HAS_RICH:
        console = Console()
        console.print(f"\n[bold cyan]Modelos disponíveis para {provider_name}:[/]")
        table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
        table.add_column("Opção", justify="center", style="bold yellow")
        table.add_column("Modelo", style="bold white")
        for i, m in enumerate(models, 1):
            table.add_row(str(i), m)
        console.print(table)
        choice = console.input("[bold cyan]Escolha o modelo pelo número (pressione Enter para usar o padrão): [/]").strip()
    else:
        print(f"\nModelos disponíveis para {provider_name}:")
        for i, m in enumerate(models, 1):
            print(f"  [{i}] {m}")
        choice = input("Escolha o modelo pelo número (pressione Enter para usar o padrão): ").strip()
        
    if choice.isdigit() and 1 <= int(choice) <= len(models):
        return models[int(choice) - 1]
    return None

def print_menu():
    # Check tool statuses
    status_claude = "[green][OK] Instalado[/]" if shutil.which("claude") else "[red][X] Nao Encontrado[/]"
    status_codex = "[green][OK] Instalado[/]" if shutil.which("codex") else "[red][X] Nao Encontrado[/]"
    status_gemini = "[green][OK] Instalado[/]" if shutil.which("gemini") else "[red][X] Nao Encontrado[/]"
    status_lms = "[green][OK] Instalado[/]" if shutil.which("lms") else "[red][X] Nao Encontrado[/]"

    if HAS_RICH:
        console = Console()
        clear_screen()
        title = Text("CLI Local AI Launcher", style="bold cyan")
        subtitle = Text(f"Sistema Operacional: {platform.system()}", style="italic gray50")
        
        console.print(Panel(
            title, 
            subtitle=subtitle,
            border_style="cyan", 
            box=box.ROUNDED, 
            expand=False
        ))
        
        table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
        table.add_column("Opcao", justify="center", style="bold yellow")
        table.add_column("Provedor de LLM", style="bold white")
        table.add_column("Status no Sistema", justify="center")
        
        table.add_row("1", "Claude Code", status_claude)
        table.add_row("2", "Codex OpenAI", status_codex)
        table.add_row("3", "Gemini CLI", status_gemini)
        table.add_row("4", "LM Studio (Direct)", status_lms)
        table.add_row("Q", "Sair (Quit)", "[bold red]Sair[/]")
        
        console.print(table)
        console.print("")
    else:
        clear_screen()
        print("=============================================")
        print("             CLI Local AI Launcher           ")
        print("=============================================")
        print(f"Detected OS: {platform.system()}")
        
        raw_status_claude = "[OK] Instalado" if shutil.which("claude") else "[X] Nao Encontrado"
        raw_status_codex = "[OK] Instalado" if shutil.which("codex") else "[X] Nao Encontrado"
        raw_status_gemini = "[OK] Instalado" if shutil.which("gemini") else "[X] Nao Encontrado"
        raw_status_lms = "[OK] Instalado" if shutil.which("lms") else "[X] Nao Encontrado"
        
        print("\nSelect LLM Provider:")
        print(f"  [1] Claude Code       ({raw_status_claude})")
        print(f"  [2] Codex OpenAI      ({raw_status_codex})")
        print(f"  [3] Gemini CLI        ({raw_status_gemini})")
        print(f"  [4] LM Studio (Direct) ({raw_status_lms})")
        print("  [Q] Quit")
        print("")

def main():
    load_env()
    os_type = get_os_type()
    if os_type == 'unknown':
        print(f"Unsupported OS: {platform.system()}")
        sys.exit(1)

    print_menu()

    if HAS_RICH:
        console = Console()
        choice = console.input("[bold cyan]Choose option [1-4, Q]: [/]").strip().upper()
    else:
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

    provider_names = {
        '1': 'Claude Code',
        '2': 'Codex OpenAI',
        '3': 'Gemini CLI',
        '4': 'LM Studio (Direct)'
    }
    provider_name = provider_names.get(choice, "Provedor")
    selected_model = select_model(provider_name)
    
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

    env = os.environ.copy()
    if selected_model:
        env['CLAUDE_MODEL'] = selected_model
        env['CODEX_MODEL'] = selected_model
        env['GEMINI_MODEL'] = selected_model
    env['CLAUDE_CODE_ATTRIBUTION_HEADER'] = '0'

    # Sanitize ANTHROPIC_BASE_URL (Claude CLI automatically appends /v1/messages)
    base_url = env.get('ANTHROPIC_BASE_URL', '')
    if base_url:
        base_url = base_url.rstrip('/')
        if base_url.endswith('/v1'):
            env['ANTHROPIC_BASE_URL'] = base_url[:-3]

    try:
        cmd = []
        if os_type == 'win':
            # Use PowerShell to run the .ps1 script, forwarding any extra CLI arguments
            cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path]
            if selected_model:
                cmd.extend(["-Model", selected_model])
        else:
            # Use Bash to run the .sh script, forwarding any extra CLI arguments
            cmd = ["bash", script_path]

        cmd.extend(sys.argv[1:])
        subprocess.run(cmd, env=env, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
