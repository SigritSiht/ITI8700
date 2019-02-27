import spacy
#data taken from OntoNotes Release 5.0 (Linguistic Data Consortium)

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
for token in doc:
    print(token.text)
#Named entities are available as the ents property of a Doc
for ent in doc.ents:
    print(ent.text, ent.label_)
#https://pypi.org/project/word2vec-wikification-py/
#matching entities to wiki links (to do)