def Total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


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
    print(Total(**coin), "Knuts")
