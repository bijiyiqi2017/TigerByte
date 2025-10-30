# TigerByte Setup Guide for macOS 🐅

Welcome to **TigerByte**! Follow these steps to get the interpreter running on your Mac.  
This guide is beginner-friendly and includes tips to make your coding journey fun.

---

## 1️⃣ Install Dependencies

### 1.1 Install Homebrew (Package Manager for macOS)

Homebrew helps you install software on your Mac easily. If you already have it, skip this step.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Check Homebrew installation:

```bash
brew --version
```

You should see something like:

```bash
Homebrew 4.5.0
```

> 💡 Pro Tip: Homebrew makes installing Python, pip, and other tools super easy.

### 1.2 Install Python 3.x

```bash
brew install python
```

Check Python version:

```bash
python3 --version
```

You should see something like:

```bash
Python 3.11.x
```

## 2️⃣ Clone TigerByte Repository

```bash
git clone https://github.com/your-username/TigerByte.git
cd TigerByte
```

> 💡 Pro Tip: If you forked the repo, use your fork URL. This makes contributing back easier.

## 3️⃣ Run the Interpreter

```bash
python3 tigerbyte.py
```

> 🐅 Fun Tip: Try a simple test command first:

```python
print("🐅 TigerByte is running!")
```

You should see the message printed in the terminal.

## 4️⃣ Common Issues & Fixes

| Issue                                    | Solution                                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Permission denied running `tigerbyte.py` | Run `chmod +x tigerbyte.py`                                                                                         |
| Python version mismatch                  | Run `python3 --version` and ensure Python 3.x is installed                                                          |
| Module not found                         | Install dependencies: `pip install -r requirements.txt`                                                             |
| Homebrew not found                       | Install Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| pipenv not found                         | Install pipenv: `brew install pipenv`                                                                               |

---

# TigerByte Setup Guide for Windows 🐅

## Prerequisites

| Requirement | Version | Download Link |
|-------------|---------|---------------|
| **Windows** | 10 or later (64-bit) | - |
| **Git for Windows** | Latest | [Download](https://git-scm.com/download/win) |
| **Python** | 3.8+ | [Download](https://www.python.org/downloads/) |

**Important**: Check "Add Python to PATH" during Python installation

---

## Installation Steps

### Step 1: Clone the Repository

```cmd
git clone https://github.com/bijiyiqi2017/TigerByte.git
cd TigerByte
```

> **Pro Tip**: If you forked the repo, use your fork URL instead. This makes contributing back easier!

### Step 2: Set Up Virtual Environment

```cmd
python -m venv venv
venv\Scripts\activate
```

**Pro Tip**: You'll see `(venv)` at the start of your command line when active!

### Step 3: Install Dependencies

```cmd
pip install -r requirements.txt
```

### Step 4: Run TigerByte

```cmd
python tigerbyte.py
```

> 🐅 **Fun Tip**: Try a simple test command first:
```python
print("🐅 TigerByte is running!")
```
You should see the message printed in the terminal.

🎉 **Success!** You should see the TigerByte welcome message.

---

## Common Issues & Troubleshooting

| Issue | Solution |
|-------|----------|
| **`python` command not recognized** | Reinstall Python and check "Add Python to PATH" during installation |
| **`pip` not found** | Use `python -m pip install -r requirements.txt` instead |
| **Permission errors** | Run Command Prompt as Administrator (right-click → "Run as administrator") |
| **PowerShell script execution error** | Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| **`git` command not found** | Install Git for Windows from [git-scm.com](https://git-scm.com/download/win) |
| **Module not found after pip install** | Ensure virtual environment is activated: `venv\Scripts\activate` |
| **Long path errors** | Enable long paths: Run as Admin in CMD: `reg add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f` |
| **Antivirus blocking Python** | Add Python and project folder to antivirus exclusions |

---

# TigerByte Setup Guide for Linux 🐅

## Prerequisites

| Requirement | Version | Installation Method |
|-------------|---------|---------------------|
| **Linux/WSL** | Ubuntu 20.04+ (Recommended) | - |
| **Git** | Latest | `sudo apt install git` |
| **Python** | 3.8+ | `sudo apt install python3 python3-venv` |

**Important**: Ensure all commands are run inside the Linux terminal (not Windows CMD/PowerShell).

---

## Installation Steps

### Step 1: Install System Dependencies

If you are using a Debian/Ubuntu-based distribution (including WSL2), run this to ensure all tools are updated:

```bash
sudo apt update
sudo apt install python3 python3-venv git -y
```

### Step 2: Clone the Repository

Navigate to your working directory (`cd ~` is a good start) and clone the repository:

```bash
git clone https://github.com/bijiyiqi2017/TigerByte.git
cd TigerByte
```

**Pro Tip (WSL2)**: Cloning the repo inside the Linux environment (`~`) offers better file system performance than cloning into a shared Windows drive (`/mnt/c/`).

### Step 3: Set Up Virtual Environment

This is crucial for isolating dependencies and avoiding permission errors.

```bash
python3 -m venv venv
source venv/bin/activate
```

**Pro Tip**: You'll see `(venv)` at the start of your terminal prompt when active!

### Step 4: Install Dependencies

With the virtual environment active, install all project requirements:

```bash
pip install -r requirements.txt
```

### Step 5: Run TigerByte

Assuming the entry point is `tigerbyte.py`:

```bash
python3 tigerbyte.py
```

🐅 **Fun Tip**: Try a simple test command first:

```python
print("🐅 TigerByte is running!")
```

You should see the message printed in the terminal.

🎉 **Success!** You should see the TigerByte welcome message.

---

## Common Issues & Troubleshooting

| Issue | Solution |
|-------|----------|
| `python3` command not found | Run `sudo apt install python3` to install the package. |
| `venv/bin/activate` not found | Ensure you installed the venv tool: `sudo apt install python3-venv`. |
| Permissions denied | This often indicates the virtual environment is not active. Run `source venv/bin/activate`. |
| `pip` not found/fails | Use `pip3 install -r requirements.txt` instead, and ensure `python3-pip` is installed. |
| Using different OS | Replace `sudo apt install` with the package manager for your distro (e.g., `dnf` for Fedora, `pacman` for Arch). |

---