def pretty_print(results):
    for i,result in enumerate(results): 
        print(f"Document-{i+1}:")
        print("==="*10)
        print(f"Content: \n {result['_source']['text']}")
        print("\n")
        print(f"Metadata: \n {result['_source']['metadata']}")
        print("\n")
        print(f"Score: {result['_score']}")
        print("\n")
        print("-----"*25)