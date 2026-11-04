import pandas as pd

def analyse_tickets(df: pd.DataFrame) -> dict:
    product_results = {}
    unique_products = df["product"].unique() 
    
    # Find Open vs Close ticket count per product
    for product in unique_products:
        count_open_tickets = len(df[(df["product"] == product) & (df["status"] == "open")])
        count_resolved_tickets = len(df[(df["product"] == product) & (df["status"] == "resolved")])
        product_count ={"count_open_tickets": count_open_tickets, "count_resolved_tickets": count_resolved_tickets}
        product_results[product] = product_count
    
    # Find avg resolution hours for resolved ticket
    resolved_tickets = df[df["status"] == "resolved"]
    resolution_time = resolved_tickets["resolved_at"] - resolved_tickets["created_at"]
    
    avg_resolution_time = resolution_time.mean()
    
    avg_resolution_hours = (
    avg_resolution_time.total_seconds() / 3600
    )
    
    return {"product": product_results, "overall_avg_resolution_time": avg_resolution_hours}