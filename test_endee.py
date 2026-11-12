from endee import Endee

client = Endee()
index = client.get_index(name="documents")

vector1 = [0.1] * 384
vector2 = [0.2] * 384
query_vector = [0.1] * 384

index.upsert([
    {
        "id": "doc1",
        "vector": vector1,
        "meta": {"title": "First Document"}
    },
    {
        "id": "doc2",
        "vector": vector2,
        "meta": {"title": "Second Document"}
    }
])

results = index.query(
    vector=query_vector,
    top_k=2
)

for item in results:
    print(item)