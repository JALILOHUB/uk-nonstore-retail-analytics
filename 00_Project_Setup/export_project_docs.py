"""
Export Project Documentation and Outputs
Automatically exports tables and charts from analysis to 04_Outputs/ folder.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Output directories
OUTPUT_DIR = r"H:\UCI_Online_Retail_Case_Study\04_Outputs"
TABLES_DIR = os.path.join(OUTPUT_DIR, "Tables")
CHARTS_DIR = os.path.join(OUTPUT_DIR, "Charts")

# Create directories if they don't exist
os.makedirs(TABLES_DIR, exist_ok=True)
os.makedirs(CHARTS_DIR, exist_ok=True)

print("="*60)
print("EXPORTING PROJECT OUTPUTS")
print("="*60)

# ============================================================================
# EXPORT TABLES
# ============================================================================

def export_table(df, filename, description=""):
    """
    Export DataFrame to CSV and Excel formats.
    
    Args:
        df: pandas DataFrame to export
        filename: filename without extension
        description: brief description of the table
    """
    csv_path = os.path.join(TABLES_DIR, f"{filename}.csv")
    excel_path = os.path.join(TABLES_DIR, f"{filename}.xlsx")
    
    # Export to CSV
    df.to_csv(csv_path, index=False, encoding='utf-8')
    print(f"✅ Exported: {filename}.csv ({len(df)} rows)")
    
    # Export to Excel
    df.to_excel(excel_path, index=False, engine='openpyxl')
    print(f"✅ Exported: {filename}.xlsx ({len(df)} rows)")
    
    return csv_path, excel_path


# ============================================================================
# EXPORT CHARTS
# ============================================================================

def export_chart(fig, filename, dpi=300):
    """
    Export matplotlib figure to PNG and PDF formats.
    
    Args:
        fig: matplotlib figure object
        filename: filename without extension
        dpi: resolution (default 300 for high quality)
    """
    png_path = os.path.join(CHARTS_DIR, f"{filename}.png")
    pdf_path = os.path.join(CHARTS_DIR, f"{filename}.pdf")
    
    # Export to PNG
    fig.savefig(png_path, dpi=dpi, bbox_inches='tight')
    print(f"✅ Exported: {filename}.png ({dpi} DPI)")
    
    # Export to PDF
    fig.savefig(pdf_path, dpi=dpi, bbox_inches='tight')
    print(f"✅ Exported: {filename}.pdf ({dpi} DPI)")
    
    plt.close(fig)
    
    return png_path, pdf_path


# ============================================================================
# EXAMPLE USAGE (Add your export calls here)
# ============================================================================

if __name__ == "__main__":
    print("\n Ready to export tables and charts")
    print("Add your export calls in the main block above")
    print("="*60)
    
    # Example:
    # export_table(monthly_performance, "monthly_revenue_performance", "Monthly revenue and invoice count")
    # export_chart(fig, "monthly_revenue_trend", dpi=300)