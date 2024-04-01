# Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("token-classification", model="Clinical-AI-Apollo/Medical-NER", aggregation_strategy='simple')
result = pipe('45 year old woman diagnosed with CAD')
result


Output:
[{'entity_group': 'AGE',
  'score': 0.5433549,
  'word': '45 year old',
  'start': 0,
  'end': 11},
 {'entity_group': 'SEX',
  'score': 0.40775427,
  'word': 'woman',
  'start': 11,
  'end': 17},
 {'entity_group': 'DISEASE_DISORDER',
  'score': 0.34644428,
  'word': 'CAD',
  'start': 32,
  'end': 36}]
