vowel_list = ['a', 'e', 'i', 'o', 'u']

def vowels(s):
  """
  output: total number of vowels in string s
  input s: string
  """
  if len(s) == 0:
    return 0

  if s[0] in vowel_list:
    return 1 + vowels(s[1:])
  else:
    return vowels(s[1:])

print(vowels('alien')) # 3
print(vowels('python')) # 1
print(vowels('cs')) # 0
