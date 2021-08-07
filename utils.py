import unicodedata

# Aplica e limpa os caracteres 
def normalize(value):
  return unicodedata.normalize('NFKD', value).encode('ASCII', 'ignore').decode('utf-8').replace(' De ',' de ').replace(' E ',' e ').replace(' E ',' e ').replace(' Com ',' com ').replace(' Por ',' por ')
