"""
Project Structure Setup Script
==============================
Creates and verifies the directory structure for the
UCI Online Retail Analysis project.

Version: V1.1 (Validated Analytical Release)
Author: Abdeljalil El Khyati
Date: September 2026

Design principle:
    This script manages project structure only.
    It does NOT overwrite notebooks or documentation files.
"""

from pathlib import Path


# ============================================================================
# PROJECT ROOT
# ============================================================================

# The script lives in:
# <PROJECT_ROOT>/00_Project_Setup/setup_project_structure.py
PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ============================================================================
# REQUIRED PROJECT FOLDERS
# ============================================================================

PROJECT_FOLDERS = [
    "00_Project_Setup",
    "01_Raw_Data",
    "02_Working_Data",
    "03_Notebooks",
    "04_Outputs/Charts",
    "04_Outputs/Reports",
    "04_Outputs/Tables",
    "05_Documentation",
    "06_Portfolio",
]


# ============================================================================
# FOLDERS THAT SHOULD RETAIN .gitkeep
# ============================================================================

GITKEEP_FOLDERS = [
    "01_Raw_Data",
    "02_Working_Data",
    "04_Outputs/Charts",
    "04_Outputs/Tables",
]


# ============================================================================
# CREATE / VERIFY STRUCTURE
# ============================================================================

def create_project_structure():
    """
    Create all required project directories.

    Existing directories are preserved.
    Existing project files are never overwritten.
    """
    print("=" * 70)
    print("UCI ONLINE RETAIL — PROJECT STRUCTURE SETUP")
    print("Version: V1.1")
    print("=" * 70)

    print(f"\nProject root: {PROJECT_ROOT}")

    print("\n📁 Verifying project folders:")
    print("-" * 50)

    for folder in PROJECT_FOLDERS:
        folder_path = PROJECT_ROOT / folder
        folder_path.mkdir(parents=True, exist_ok=True)

        print(f"✅ {folder_path.relative_to(PROJECT_ROOT)}")

    print("\n📌 Verifying .gitkeep files:")
    print("-" * 50)

    for folder in GITKEEP_FOLDERS:
        folder_path = PROJECT_ROOT / folder
        gitkeep_path = folder_path / ".gitkeep"

        if not gitkeep_path.exists():
            gitkeep_path.touch()
            print(
                f"✅ Created: "
                f"{gitkeep_path.relative_to(PROJECT_ROOT)}"
            )
        else:
            print(
                f"↪ Already exists: "
                f"{gitkeep_path.relative_to(PROJECT_ROOT)}"
            )

    print("\n" + "=" * 70)
    print("✅ PROJECT STRUCTURE VERIFICATION COMPLETE")
    print("=" * 70)

    print("\nImportant:")
    print(
        "This script creates and verifies folders only. "
        "It does not overwrite documentation, notebooks, "
        "outputs, or other existing project files."
    )


# ============================================================================
# OPTIONAL STRUCTURE REPORT
# ============================================================================

def print_structure_summary():
    """Print the expected repository structure."""
    print("\nExpected repository structure:\n")

    for folder in PROJECT_FOLDERS:
        print(f"├── {folder}/")

    print("├── .gitignore")
    print("├── CHANGELOG.md")
    print("├── LICENSE")
    print("└── README.md")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    create_project_structure()
    print_structure_summary()