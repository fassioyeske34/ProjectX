import pandas as pd

data = {
    "name": ["John", "Jane", "Alice"],
    "age": [20, 21, 22],
    "city": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)
print(df)
