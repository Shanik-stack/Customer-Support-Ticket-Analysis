import json
from pathlib import Path
import pandas as pd

from customer_support_tickets import clean_tickets
def main():
    tickets_data_path = Path("data/tickets.json")
    
    with tickets_data_path.open() as f:
        tickets = json.load(f)
    df = pd.DataFrame(tickets)
    print(df)
    cleaned_df = clean_tickets(df)
    print(cleaned_df)
    
if __name__ == "__main__":
    main()
        