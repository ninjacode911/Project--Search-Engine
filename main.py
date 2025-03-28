from exa_py import Exa
import os

print(os.getenv("API_KEY"))  # Should print your key

exa = Exa("API_KEY")  # my API Key

query = input('Hey, What would you like to know about? \n')

response = exa.search(
    query,
    num_results=10,  # Number of results to return
    category="news",
    use_autoprompt=True,  # Helps you refine the search query
)

'''
# These are for more elaborate search results
for result in response['result']:
    print("Navnit\'s Search Engine")
    print(f"\nTitle: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"published on: {result['published_on'],['N/A']}")
    print(f"Description: {result['description']}")
    print(f"Author: {result['author']}")
    print(f"Source: {result['source']}")
    print("\n")
'''

response = exa.search(
  query,
  num_results=7
)

for result in response.results:
    print(f"Title: {result.title}")
    print(f"URL: {result.url}")
    print()

