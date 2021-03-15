from python_graphql_client import GraphqlClient

client = GraphqlClient(endpoint="https://countries.trevorblades.com")

query = """
    query countryQuery($countryCode: String) {
        country(code:$countryCode) {
            code
            name
        }
    }
"""
variables = {"countryCode": "RU"}

data = client.execute(query=query, variables=variables)
print(data)
