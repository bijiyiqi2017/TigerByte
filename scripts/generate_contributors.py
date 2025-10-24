#!/usr/bin/env python3
import json
from datetime import datetime
from pathlib import Path

def load_contributors():
    """Load contributors from contributors.json file."""
    with open("contributors.json", "r") as f:
        data = json.load(f)
    return data

def generate_markdown(data):
    """Generate markdown content from contributors data."""
    content = ["# Contributors\n"]
    content.append(f"This file is auto-generated from the contributors.json file. Last updated: {data['last_updated']}\n")
    content.append(f"Project: {data['project']} - {data['event']}\n")
    
    content.append("## Contributors List\n")
    content.append("| Name | GitHub | Issues Resolved |")
    content.append("|------|--------|-----------------|")
    
    # Sort contributors by name (fallback to github_id if name is empty)
    sorted_contributors = sorted(
        data["contributors"],
        key=lambda x: x["name"].strip() if x["name"].strip() else x["github_id"]
    )
    
    for contributor in sorted_contributors:
        name = contributor["name"].strip() or "—"  # Use dash if name is empty
        github_id = contributor["github_id"]
        issues = ", ".join(map(str, contributor["issues_resolved"]))
        
        # Create a row with GitHub profile link
        content.append(
            f"| {name} | [@{github_id}](https://github.com/{github_id}) | {issues} |"
        )
    
    content.append("\n## How to Contribute")
    content.append("1. Fork the repository")
    content.append("2. Create your feature branch")
    content.append("3. Commit your changes")
    content.append("4. Push to your branch")
    content.append("5. Open a Pull Request")
    content.append("\nFor more detailed instructions, please see our [Contributing Guide](CONTRIBUTING.md).")
    
    return "\n".join(content)

def main():
    try:
        # Load contributors data
        data = load_contributors()
        
        # Generate markdown content
        markdown_content = generate_markdown(data)
        
        # Write to CONTRIBUTORS.md
        with open("CONTRIBUTORS.md", "w", encoding="utf-8") as f:
            f.write(markdown_content)
        
        print("✨ Successfully generated CONTRIBUTORS.md!")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()