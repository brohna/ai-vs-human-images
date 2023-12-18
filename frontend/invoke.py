from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/category_chain/")
res = remote_chain.invoke({"text": "countries"})
print(res)
