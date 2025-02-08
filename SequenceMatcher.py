from difflib import SequenceMatcher
text1 = "My Name  Veena"
text2 = "Hi,Guys"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")