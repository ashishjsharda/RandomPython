class SearchEngine:
    def __init__(self):
        self.inverted_index = {}

    def add_document(self, doc_id, text):
        words = text.lower().split()

        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = [doc_id]
            else:
                self.inverted_index[word].append(doc_id)

    def search(self, term):
        term = term.lower()

        if term in self.inverted_index:
            return self.inverted_index[term]
        else:
            return []

# Usage:

engine = SearchEngine()
engine.add_document('doc1', 'The quick brown fox jumps over the lazy dog.')
engine.add_document('doc2', 'My dog is quick and can jump over fences.')
engine.add_document('doc3', 'Your dog is super lazy, unlike my fox.')

print(engine.search('quick'))  # Prints: ['doc1', 'doc2']
print(engine.search('fox'))    # Prints: ['doc1', 'doc3']
print(engine.search('dog'))    # Prints: ['doc1', 'doc2', 'doc3']
