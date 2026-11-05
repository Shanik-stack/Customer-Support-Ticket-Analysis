# Customer Support Ticket Analysis

A Python project for cleaning support-ticket data, calculating resolution statistics, evaluating LLM-generated summaries, and querying customer–ticket–product relationships in Neo4j.

## Implementation


- **Data cleaning ([cleaning.py](src/customer_support_tickets/cleaning.py)):** Removes exact duplicates, normalizes missing text values, and detects conflicting ticket IDs.
- **Analysis ([analysis.py](src/customer_support_tickets/analysis.py)):** Computes open/resolved counts per product and the average resolution time of resolved tickets.
- **LLM evaluation ([llm_evaluation.md](docs/llm_evaluation.md)):** Scores the three summaries on faithfulness, salient content coverage, clarity/fluency, and conciseness.
- **Knowledge graph ([graph.py](src/customer_support_tickets/graph.py)):** Imports cleaned records using parameterized Cypher and `MERGE`, following `(:Customer)-[:RAISED]->(:Ticket)-[:ABOUT]->(:Product)`.

## Results

Five input records are cleaned into **four unique tickets**.

| Product | Open | Resolved |
| --- | ---: | ---: |
| CloudSync | 1 | 1 |
| InvoicePro | 1 | 1 |

- **Average resolution time:** 13.5 hours across resolved tickets.
- **Neo4j graph:** 3 customers, 4 tickets, 2 products, 8 relationships.
- **Multi-product customer:** Asha Rao (2 products).
- **Summary evaluation:** See [docs/llm_evaluation.md](docs/llm_evaluation.md) for the rubric and individual scores.

## Setup

**Prerequisite:** Docker and Docker Compose.

1. Clone the repository and open a terminal in its root directory.
2. Copy `.env.example` to `.env` and set a password (at least 8 characters):

   ```dotenv
   NEO4J_PASSWORD=your_secure_password
   ```

3. Build and run the application:

   ```bash
   docker compose up --build
   ```

Compose starts Neo4j, waits for its health check, then runs the Python application. The application prints the analysis and graph-query results, then exits on success. Neo4j Browser is available at [http://localhost:7474](http://localhost:7474) (username: `neo4j`; password: the value in `.env`).

## Tests

Five `unittest` tests cover duplicate removal, missing issue descriptions, analysis, missing required fields, and conflicting ticket IDs.

```bash
docker compose run --rm --no-deps app python -m unittest discover -s tests -v
```

The Docker workflow was also verified with a **fresh Neo4j volume**, reproducing the expected results.

## Project Structure

```text
DC_Coding_Assignment/
├── data/
│   └── tickets.json                  # Support tickets data
├── docs/
│   ├── ai_use_documentation.md       # AI use documentation
│   └── llm_evaluation.md             # Summary evaluation and scores
├── src/
│   └── customer_support_tickets/
│       ├── __init__.py               # Python package initialization
│       ├── analysis.py               # Ticket statistics
│       ├── cleaning.py               # Data cleaning and validation
│       ├── graph.py                  # Neo4j graph creation and queries
│       └── main.py                   # Application entry point
├── tests/
│   └── test_tickets.py               # Unit tests
├── .env.example                      
├── compose.yaml                      
├── Dockerfile                        
├── pyproject.toml                    
└── README.md                         
```

**Note:** Customer names are used as graph identifiers because the supplied dataset has no customer IDs.