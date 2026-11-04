import pandas as pd

def clean_tickets(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()
    
    mandatory_cols  = ["ticket_id", "customer", "product", "status", "created_at"]
    optional_cols = ["issue", "resolved_at"]
    
    # Clean strings
    for col in cleaned_df.columns:
        cleaned_df[col] = cleaned_df[col].astype("string").str.strip()
        cleaned_df[col] = cleaned_df[col].replace("", pd.NA)
    
    # Remove Duplicates
    cleaned_df = cleaned_df.drop_duplicates()
    if cleaned_df["ticket_id"].duplicated().sum() > 0:
        raise ValueError("Multiple tickets with same ticket ID")
    
    # Checking missing value in mandatory cols
    missing_values = cleaned_df[mandatory_cols].isna().sum()
    missing_values = missing_values[missing_values>0]
    if missing_values.empty is not True:
        raise ValueError(f"Missing values in mandatory columns: {missing_values.to_string()}")
    
    
    # Convert to timestamps
    cleaned_df["created_at"] = pd.to_datetime(cleaned_df["created_at"])
    cleaned_df["resolved_at"] = pd.to_datetime(cleaned_df["resolved_at"])    
    
    
    return cleaned_df
