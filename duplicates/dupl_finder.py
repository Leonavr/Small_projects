import json
import collections
with open(r"C:\Work\acs_patient\Classifiers\IntentStatementClassifierEN.json", "r", encoding = 'utf-8') as read_file:
    data = json.load(read_file)
corpus = data['Corpus']
a = [x.split('|')[1] for x in corpus]
without_dupl = [item for item, count in collections.Counter(a).items() if count > 1]
print(without_dupl)
for j in without_dupl:
    with open("duplicates.txt", "a") as f:
        f.write(f'|{j}"\n')
print(without_dupl)
