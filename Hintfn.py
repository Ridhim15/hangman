import random
def give_hint(hashmap,blanks,hashset):
  hint=random.choice(list(hashmap.keys()))
  for ch in (hashmap[hint]):
    blanks[ch]=hint
  print(f"\nFunction Hint was called \n'{hint}' was chosen")
  print(*blanks,"\n\n")
  hashset.add(hint)
  del hashmap[hint]
