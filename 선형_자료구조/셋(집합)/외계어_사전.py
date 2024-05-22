def solution(spell, dic):
  spell_set = set(spell)
  for word in dic:
    if set(word) == spell_set:
      return 1
    return 2
