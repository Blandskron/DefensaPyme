import subprocess
import shlex
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ShellExecutor")

def run_command_safe(cmd: list | str, timeout: int = 60) -> str:
    try:
        if isinstance(cmd, str):
            cmd = shlex.split(cmd)

        logger.info(f"Ejecutando: {' '.join(cmd)}")

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout
        )

        output = result.stdout.strip() + ("\n" + result.stderr.strip() if result.stderr else "")
        return output or "Sin resultados."

    except subprocess.TimeoutExpired:
        return "Error: El comando superó el tiempo límite."
    except FileNotFoundError:
        return "Error: Comando no encontrado."
    except Exception as e:
        return f"Error inesperado: {str(e)}"
