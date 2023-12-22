```python
from google.cloud import bigquery

# Instantiate a BigQuery client
client = bigquery.Client()

# Define your search query
# Replace 'your_invention_keywords' with keywords related to your invention
query = """
    SELECT publication_number, title_localized, abstract_localized
    FROM `patents-public-data.patents.publications`,
    UNNEST(title_localized) as title_localized,
    UNNEST(abstract_localized) as abstract_localized
    WHERE title_localized.text LIKE '%your_invention_keywords%'
    LIMIT 100
"""

# Run the query
query_job = client.query(query)

# Print the results
for row in query_job:
    print(f"Publication Number: {row.publication_number}")
    print(f"Title: {row.title_localized.text}")
    print(f"Abstract: {row.abstract_localized.text}")
    print("\n")
```
