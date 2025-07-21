
sacred_prophecy = ("First Star Falls", "Second Moon Rises", "Third Realm Unites")
print(f"Original Prophecy: {sacred_prophecy}")

sacred_prophecy[1] = "Second Moon Sets" 
print(f"Attempted Altered Prophecy: {sacred_prophecy}")
# TypeError: 'tuple' object does not support item assignment