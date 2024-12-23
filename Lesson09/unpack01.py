def f(*args, **kwargs):
    print(kwargs)


coins = [
    {
        "galleons": 100,
        "sickles": 50,
        "knuts": 25,
    },
    {
        "galleons": 200,
        "sickles": 150,
        "knuts": 25,
    },
    {
        "galleons": 200,
        "sickles": 200,
        "knuts": 25,
    },
]
for coin in coins:
    f(**coin)
