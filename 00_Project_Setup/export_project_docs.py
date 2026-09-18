"""
Export Project Documents and Data Handoff Module
=================================================
Provides reusable functions for exporting validated DataFrames and
matplotlib figures to the designated project folders.

Version: V1.1 (Validated Analytical Release)
Author: Abdeljalil El Khyati
Date: September 2026

The module is designed to be portable within the repository:
project paths are derived from this file's location rather than from
a machine-specific absolute path.

Usage from the Jupyter Notebook:

    import sys
    from pathlib import Path

    PROJECT_ROOT = Path.cwd().resolve().parent.parent
    sys.path.append(str(PROJECT_ROOT / "00_Project_Setup"))

    from export_project_docs import (
        export_table,
        export_table_csv_only,
        export_chart,
        export_chart_png_only,
        export_working_data,
        export_working_data_batch,
        export_raw_data,
        validate_reconciliation,
        print_reconciliation_report,
    )
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# ============================================================================
# PROJECT PATHS
# ============================================================================

# This file lives in:
# <PROJECT_ROOT>/00_Project_Setup/export_project_docs.py
# Therefore its parent directory's parent is the repository root.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DIR = PROJECT_ROOT / "01_Raw_Data"
WORKING_DIR = PROJECT_ROOT / "02_Working_Data"
TABLES_DIR = PROJECT_ROOT / "04_Outputs" / "Tables"
CHARTS_DIR = PROJECT_ROOT / "04_Outputs" / "Charts"
REPORTS_DIR = PROJECT_ROOT / "04_Outputs" / "Reports"


# Ensure required project directories exist.
for directory in [
    RAW_DIR,
    WORKING_DIR,
    TABLES_DIR,
    CHARTS_DIR,
    REPORTS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)


# ============================================================================
# TABLE EXPORT FUNCTIONS
# ============================================================================

def export_table(df, filename, description=""):
    """
    Export a pandas DataFrame to both CSV and Excel formats.

    Args:
        df (pd.DataFrame): DataFrame to export.
        filename (str): Output filename without extension.
        description (str): Optional logging description.

    Returns:
        tuple[str, str]: (csv_path, excel_path)

    Raises:
        ValueError: If df is not a DataFrame or is empty.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError(
            f"Expected pandas DataFrame, got {type(df).__name__}"
        )

    if df.empty:
        raise ValueError(
            f"DataFrame '{filename}' is empty. Nothing to export."
        )

    csv_path = TABLES_DIR / f"{filename}.csv"
    excel_path = TABLES_DIR / f"{filename}.xlsx"

    # UTF-8 BOM improves compatibility with Excel.
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"✅ Exported: {csv_path.name} ({len(df):,} rows)")

    df.to_excel(excel_path, index=False, engine="openpyxl")
    print(f"✅ Exported: {excel_path.name} ({len(df):,} rows)")

    if description:
        print(f"   📝 {description}")

    return str(csv_path), str(excel_path)


def export_table_csv_only(df, filename, description=""):
    """
    Export a pandas DataFrame to CSV format only.

    Args:
        df (pd.DataFrame): DataFrame to export.
        filename (str): Output filename without extension.
        description (str): Optional logging description.

    Returns:
        str: CSV file path.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError(
            f"Expected pandas DataFrame, got {type(df).__name__}"
        )

    csv_path = TABLES_DIR / f"{filename}.csv"

    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"✅ Exported: {csv_path.name} ({len(df):,} rows)")

    if description:
        print(f"    {description}")

    return str(csv_path)


# ============================================================================
# CHART EXPORT FUNCTIONS
# ============================================================================

def export_chart(fig, filename, dpi=300):
    """
    Export a matplotlib figure to both PNG and PDF formats.

    Args:
        fig (matplotlib.figure.Figure): Figure object to export.
        filename (str): Output filename without extension.
        dpi (int): Resolution in DPI.

    Returns:
        tuple[str, str]: (png_path, pdf_path)

    Raises:
        ValueError: If fig does not provide a savefig method.
    """
    if not hasattr(fig, "savefig"):
        raise ValueError(
            f"Expected matplotlib Figure, got {type(fig).__name__}"
        )

    png_path = CHARTS_DIR / f"{filename}.png"
    pdf_path = CHARTS_DIR / f"{filename}.pdf"

    fig.savefig(
        png_path,
        dpi=dpi,
        bbox_inches="tight",
        facecolor="white",
    )
    print(f"✅ Exported: {png_path.name} ({dpi} DPI)")

    fig.savefig(
        pdf_path,
        dpi=dpi,
        bbox_inches="tight",
        facecolor="white",
    )
    print(f"✅ Exported: {pdf_path.name} ({dpi} DPI)")

    plt.close(fig)

    return str(png_path), str(pdf_path)


def export_chart_png_only(fig, filename, dpi=300):
    """
    Export a matplotlib figure to PNG format only.

    Args:
        fig (matplotlib.figure.Figure): Figure object to export.
        filename (str): Output filename without extension.
        dpi (int): Resolution in DPI.

    Returns:
        str: PNG file path.
    """
    if not hasattr(fig, "savefig"):
        raise ValueError(
            f"Expected matplotlib Figure, got {type(fig).__name__}"
        )

    png_path = CHARTS_DIR / f"{filename}.png"

    fig.savefig(
        png_path,
        dpi=dpi,
        bbox_inches="tight",
        facecolor="white",
    )
    print(f"✅ Exported: {png_path.name} ({dpi} DPI)")

    plt.close(fig)

    return str(png_path)


# ============================================================================
# WORKING DATA EXPORT FUNCTIONS
# ============================================================================

def export_working_data(df, filename, description=""):
    """
    Export a validated working DataFrame to 02_Working_Data.

    Args:
        df (pd.DataFrame): DataFrame to export.
        filename (str): Output filename. '.csv' is added if absent.
        description (str): Optional logging description.

    Returns:
        str: Full file path.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError(
            f"Expected pandas DataFrame, got {type(df).__name__}"
        )

    if not filename.lower().endswith(".csv"):
        filename = f"{filename}.csv"

    filepath = WORKING_DIR / filename

    df.to_csv(filepath, index=False, encoding="utf-8-sig")
    print(f"✅ Exported working data: {filepath.name} ({len(df):,} rows)")

    if description:
        print(f"    {description}")

    return str(filepath)


def export_working_data_batch(data_dict):
    """
    Export multiple working DataFrames.

    Args:
        data_dict (dict):
            Mapping of filenames to DataFrames.

    Returns:
        list[str]: Successfully exported file paths.
    """
    exported_paths = []

    print("\n📦 Exporting Working Data Batch:")
    print("-" * 50)

    for filename, df in data_dict.items():
        try:
            path = export_working_data(df, filename)
            exported_paths.append(path)
        except Exception as exc:
            print(f"️ Failed to export {filename}: {exc}")

    print(
        f"\n✅ Batch export complete: "
        f"{len(exported_paths)}/{len(data_dict)} files"
    )

    return exported_paths


# ============================================================================
# RAW DATA EXPORT FUNCTIONS
# ============================================================================

def export_raw_data(
    df,
    filename="online_retail_raw.csv",
    description="",
):
    """
    Export the reconstructed raw analytical input to 01_Raw_Data.

    Args:
        df (pd.DataFrame): Reconstructed raw DataFrame before cleaning.
        filename (str): Output filename. '.csv' is added if absent.
        description (str): Optional logging description.

    Returns:
        str: Full file path.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError(
            f"Expected pandas DataFrame, got {type(df).__name__}"
        )

    if not filename.lower().endswith(".csv"):
        filename = f"{filename}.csv"

    filepath = RAW_DIR / filename

    df.to_csv(filepath, index=False, encoding="utf-8-sig")
    print(
        f"✅ Exported raw data: "
        f"{filepath.name} ({len(df):,} rows, {len(df.columns)} columns)"
    )

    if description:
        print(f"   📝 {description}")

    return str(filepath)


# ============================================================================
# VALIDATION & RECONCILIATION HELPERS
# ============================================================================

def validate_reconciliation(
    df_sales,
    df_extreme_outliers,
    df_physical_products,
    operational_items,
    expected_physical_rows=None,
):
    """
    Validate row and revenue reconciliation.

    The expected physical-row count is calculated from the analytical inputs.
    An optional expected_physical_rows value can be supplied as an external
    validation target, but it is not hard-coded by default.

    Args:
        df_sales (pd.DataFrame):
            Valid sales population.
        df_extreme_outliers (pd.DataFrame):
            Isolated extreme outlier rows.
        df_physical_products (pd.DataFrame):
            Final physical-product analytical population.
        operational_items (list):
            Operational/non-product descriptions.
        expected_physical_rows (int | None):
            Optional external row-count expectation.

    Returns:
        dict: Reconciliation metrics and status.
    """
    required_columns = {"Description", "Revenue"}

    for name, df in {
        "df_sales": df_sales,
        "df_extreme_outliers": df_extreme_outliers,
        "df_physical_products": df_physical_products,
    }.items():
        if not isinstance(df, pd.DataFrame):
            raise ValueError(f"{name} must be a pandas DataFrame.")

        missing_columns = required_columns.difference(df.columns)
        if missing_columns:
            raise ValueError(
                f"{name} is missing required columns: "
                f"{sorted(missing_columns)}"
            )

    operational_rows_df = df_sales[
        df_sales["Description"].isin(operational_items)
    ]

    calculated_expected_rows = (
        len(df_sales)
        - len(df_extreme_outliers)
        - len(operational_rows_df)
    )

    row_difference = (
        len(df_physical_products) - calculated_expected_rows
    )

    valid_revenue = df_sales["Revenue"].sum()
    outlier_revenue = df_extreme_outliers["Revenue"].sum()
    operational_revenue = operational_rows_df["Revenue"].sum()
    physical_revenue = df_physical_products["Revenue"].sum()

    expected_revenue = (
        valid_revenue
        - outlier_revenue
        - operational_revenue
    )

    revenue_difference = physical_revenue - expected_revenue

    row_count_matches_external_target = True

    if expected_physical_rows is not None:
        row_count_matches_external_target = (
            calculated_expected_rows == expected_physical_rows
        )

    status = (
        "PASSED"
        if (
            row_difference == 0
            and abs(revenue_difference) < 0.01
            and row_count_matches_external_target
        )
        else "FAILED"
    )

    return {
        "status": status,
        "valid_sales_rows": len(df_sales),
        "outlier_rows": len(df_extreme_outliers),
        "operational_rows": len(operational_rows_df),
        "expected_physical_rows": calculated_expected_rows,
        "actual_physical_rows": len(df_physical_products),
        "external_expected_physical_rows": expected_physical_rows,
        "row_difference": row_difference,
        "valid_sales_revenue": valid_revenue,
        "outlier_revenue": outlier_revenue,
        "operational_revenue": operational_revenue,
        "expected_physical_revenue": expected_revenue,
        "actual_physical_revenue": physical_revenue,
        "revenue_difference": revenue_difference,
        "row_count_matches_external_target": row_count_matches_external_target,
    }


def print_reconciliation_report(results):
    """
    Print a formatted reconciliation report.

    Args:
        results (dict):
            Output from validate_reconciliation().
    """
    print("\n" + "=" * 70)
    print("V1.1 DATA LINEAGE & RECONCILIATION REPORT")
    print("=" * 70)

    print("\nROW RECONCILIATION")
    print("-" * 40)
    print(
        f"Valid sales rows              : "
        f"{results['valid_sales_rows']:,}"
    )
    print(
        f"Outlier rows                  : "
        f"{results['outlier_rows']:,}"
    )
    print(
        f"Operational rows              : "
        f"{results['operational_rows']:,}"
    )
    print(
        f"Expected physical rows        : "
        f"{results['expected_physical_rows']:,}"
    )
    print(
        f"Actual physical rows          : "
        f"{results['actual_physical_rows']:,}"
    )
    print(
        f"Row difference                : "
        f"{results['row_difference']:,}"
    )

    if results.get("external_expected_physical_rows") is not None:
        print(
            f"External expected row count  : "
            f"{results['external_expected_physical_rows']:,}"
        )
        print(
            "External row-count check     : "
            f"{'PASS' if results['row_count_matches_external_target'] else 'FAIL'}"
        )

    print("\nREVENUE RECONCILIATION")
    print("-" * 40)
    print(
        f"Valid sales revenue           : "
        f"£{results['valid_sales_revenue']:,.2f}"
    )
    print(
        f"Outlier revenue               : "
        f"£{results['outlier_revenue']:,.2f}"
    )
    print(
        f"Operational revenue           : "
        f"£{results['operational_revenue']:,.2f}"
    )
    print(
        f"Expected physical revenue     : "
        f"£{results['expected_physical_revenue']:,.2f}"
    )
    print(
        f"Actual physical revenue       : "
        f"£{results['actual_physical_revenue']:,.2f}"
    )
    print(
        f"Revenue difference            : "
        f"£{results['revenue_difference']:,.2f}"
    )

    print("\n" + "=" * 70)

    if results["status"] == "PASSED":
        print(
            "✅ RECONCILIATION PASSED — "
            "Dataset lineage is internally consistent."
        )
    else:
        print(
            "⚠️ RECONCILIATION FAILED — "
            "Investigation required before export."
        )

    print("=" * 70 + "\n")


# ============================================================================
# MAIN EXECUTION (STANDALONE TEST)
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("EXPORT PROJECT DOCS MODULE — V1.1")
    print("=" * 60)

    print(f"\nProject root: {PROJECT_ROOT}")
    print(f"Raw data dir: {RAW_DIR}")
    print(f"Working dir:  {WORKING_DIR}")
    print(f"Tables dir:   {TABLES_DIR}")
    print(f"Charts dir:   {CHARTS_DIR}")
    print(f"Reports dir:  {REPORTS_DIR}")

    print("\n✅ All project directories verified.")

    print("\n📋 Available functions:")
    print("   • export_table(df, filename, description)")
    print("   • export_table_csv_only(df, filename, description)")
    print("   • export_chart(fig, filename, dpi=300)")
    print("   • export_chart_png_only(fig, filename, dpi=300)")
    print("   • export_working_data(df, filename, description)")
    print("   • export_working_data_batch(data_dict)")
    print("   • export_raw_data(df, filename, description)")
    print("   • validate_reconciliation(...)")
    print("   • print_reconciliation_report(results)")

    print("\n" + "=" * 60)
    print("Module ready for import from Jupyter Notebook.")
    print("=" * 60)