import time
import sys
from colorama import init, Fore, Style
from IPython.display import display, Markdown

init()  # enables colorama on Windows

# Color map for different message types
MSG_COLORS = {
    "human":    Fore.GREEN,
    "ai":       Fore.CYAN,
    "tool":     Fore.YELLOW,
    "system":   Fore.MAGENTA,
    "function": Fore.YELLOW,
}

AGENT_COLOR = Fore.BLUE
SEPARATOR = f"{Fore.WHITE}{Style.DIM}{'─' * 80}{Style.RESET_ALL}"

def plot_mermaid(agent):
    # Get the graph representation
    graph = agent.get_graph()

    # Get Mermaid diagram
    mermaid_code = graph.draw_mermaid()

    # Display in Jupyter Notebook
    display(Markdown(f"```mermaid\n{mermaid_code}\n```"))
    
def typewrite(text: str, delay: float = 0.015):
    """Print text character-by-character like a human typing."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in ".!?\n":
            time.sleep(delay * 3)
        elif char in ",;:":
            time.sleep(delay * 2)
        else:
            time.sleep(delay)
    print()


def stream_invoke(app, input_data: dict, config: dict = None, typing_speed: float = 0.015):
    """
    Stream an agent/graph execution with colored, human-like typed output.

    Drop-in replacement for app.invoke() — takes the same input and config.

    Args:
        app: Compiled LangGraph graph (from .compile())
        input_data: Same dict you'd pass to app.invoke() (e.g., {"messages": [...]})
        config: Optional config dict (e.g., {"configurable": {"thread_id": "..."}})
        typing_speed: Delay between characters (seconds). Set to 0 for instant.

    Returns:
        The final result (same as app.invoke() would return)
    """
    print(f"\n{SEPARATOR}")
    print(f"{Fore.WHITE}{Style.BRIGHT}  STREAMING EXECUTION{Style.RESET_ALL}")
    print(f"{SEPARATOR}\n")

    last_msg_count = 0
    result = None

    for event in app.stream(input_data, config=config, stream_mode="values"):
        messages = event.get("messages", [])

        # Only process new messages since last event
        new_messages = messages[last_msg_count:]
        last_msg_count = len(messages)

        for msg in new_messages:
            msg_type = getattr(msg, "type", "unknown")
            color = MSG_COLORS.get(msg_type, Fore.WHITE)
            name = getattr(msg, "name", None)
            content = getattr(msg, "content", "")

            # Header line
            label = msg_type.upper()
            if name:
                label = f"{label} ({Fore.WHITE}{Style.BRIGHT}{name}{Style.RESET_ALL}{color})"

            print(f"{color}{Style.BRIGHT}┌─ {label}{Style.RESET_ALL}")

            # Content
            if content:
                # Indent each line under the header
                for line in content.split("\n"):
                    sys.stdout.write(f"{color}│ {Style.RESET_ALL}")
                    if typing_speed > 0:
                        typewrite(line, delay=typing_speed)
                    else:
                        print(line)

            # Tool calls (for AI messages that invoke tools)
            tool_calls = getattr(msg, "tool_calls", None)
            if tool_calls:
                for tc in tool_calls:
                    tc_name = tc.get("name", "unknown")
                    tc_args = tc.get("args", {})
                    print(
                        f"{color}│ {Fore.WHITE}{Style.DIM}→ tool: {tc_name}({tc_args}){Style.RESET_ALL}")

            print(f"{color}{Style.BRIGHT}└{'─' * 40}{Style.RESET_ALL}")
            print()

        result = event

    print(f"{SEPARATOR}")
    print(f"{Fore.GREEN}{Style.BRIGHT}  EXECUTION COMPLETE{Style.RESET_ALL}")
    print(f"{SEPARATOR}\n")

    return result