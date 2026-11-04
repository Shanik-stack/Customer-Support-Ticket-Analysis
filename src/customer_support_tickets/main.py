import json
from pathlib import Path
import pandas as pd

from customer_support_tickets import clean_tickets, analyse_tickets
def main():
    
    # Part A
    
    tickets_data_path = Path("data/tickets.json")
    
    with tickets_data_path.open() as f:
        tickets = json.load(f)
    df = pd.DataFrame(tickets)
    
    cleaned_df = clean_tickets(df)
    
    analysis_statistics = analyse_tickets(cleaned_df)
    print(analysis_statistics)
    
    # Part B
    
    
if __name__ == "__main__":
    main()
        