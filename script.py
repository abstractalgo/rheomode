import os
os.environ["OPENAI_API_KEY"] = ''

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
# documents = SimpleDirectoryReader('data').load_data()
# index = GPTSimpleVectorIndex(documents)
# # save to disk
# index.save_to_disk('index.json')

# load from disk
index = GPTSimpleVectorIndex.load_from_disk('index.json')

while (True):
  query = input("> ")
  res = index.query(query)
  print(res)
