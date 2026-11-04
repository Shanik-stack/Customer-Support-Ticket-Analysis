
import unittest

import pandas as pd

from customer_support_tickets import *


class TestTickets(unittest.TestCase):

    def setUp(self):
        self.raw_df = pd.read_json("data/tickets.json")

    def test_duplicate_removal(self):
        cleaned = clean_tickets(self.raw_df)

        self.assertEqual(len(cleaned), 4)
        self.assertEqual(cleaned["ticket_id"].nunique(), 4)

    def test_missing_issue(self):
        cleaned = clean_tickets(self.raw_df)
        
        t4 = cleaned[cleaned["ticket_id"] == "T4"].iloc[0]

        self.assertTrue(pd.isna(t4["issue"]))

    def test_ticket_analysis(self):
        cleaned = clean_tickets(self.raw_df)
        result = analyse_tickets(cleaned)

        self.assertEqual(
            result["product"]["CloudSync"]["count_open_tickets"], 1
        )
        self.assertEqual(
            result["product"]["InvoicePro"]["count_resolved_tickets"], 1
        )
        self.assertAlmostEqual(
            result["overall_avg_resolution_time"], 13.5
        )

    def test_missing_customer(self):
        invalid_df = self.raw_df.copy()
        #simulate missing customer
        invalid_df.loc[0, "customer"] = None
        
        #Checks if Value Error is raised
        with self.assertRaises(ValueError):
            clean_tickets(invalid_df)

    def test_conflicting_ticket_id(self):
        error_row = self.raw_df.iloc[[0]].copy()
        error_row["product"] = "InvoicePro"
        #Simulate adding duplicate ticket_id with different product
        invalid_df = pd.concat(
            [self.raw_df, error_row],
            ignore_index=True
        )

        with self.assertRaises(ValueError):
            clean_tickets(invalid_df)


if __name__ == "__main__":
    unittest.main()
