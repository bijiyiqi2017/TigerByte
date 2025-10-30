import random
from pathlib import Path

# Define the path to the banners directory (relative to the project root)
# We assume banners from Issue #25 will be placed in 'assets/banners/'
BANNER_DIR = Path("assets/banners")

def load_all_banners():
    """
    Finds all .txt banner files in the banner directory.
    Returns a list of Path objects.
    """
    if not BANNER_DIR.is_dir():
        print(f"Warning: Banner directory not found at {BANNER_DIR}")
        return []  # Return empty list if directory doesn't exist

    # Find all files ending in .txt
    banner_files = list(BANNER_DIR.glob("*.txt"))
    return banner_files

def get_banner_content(banner_path):
    """Reads and returns the content of a specific banner file."""
    try:
        with open(banner_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"[Error loading banner: {e}]"

def display_random_banner():
    """Selects a random banner from the directory and prints it."""
    banners = load_all_banners()

    if not banners:
        # Fallback text if no banners are found
        print("="*30)
        print(" Welcome to TigerByte! ")
        print("="*30)
        return

    random_banner_path = random.choice(banners)
    print(get_banner_content(random_banner_path))

def display_banner_by_name(file_name):
    """Selects a specific banner by name (e.g., 'banner1.txt') and prints it."""
    banner_path = BANNER_DIR / file_name

    if not banner_path.exists():
        print(f"Error: Banner '{file_name}' not found.")
        # Fallback to a random one
        display_random_banner()
    else:
        print(get_banner_content(banner_path))