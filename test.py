import chromadb
chroma_client = chromadb.api.async_api.AsyncBaseAPI()
# collection = chroma_client.create_collection(name="my_collection")
# collection.add(
#     documents=[
#         "Niggas in Paris",
#         "We're a team bro",
#         "Getting over it",
#         "Back when they thought pink polos would hurt the Roc",
#         "Before Cam got the shit to pop"
#     ],
#     ids=["id1", "id2","id3","id4","id5"]
# )
#
# results = collection.query(
#     query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
#     n_results=5 # how many results to return
# )
# print(results)
