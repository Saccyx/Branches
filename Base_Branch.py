import Branch.py

class Base_Branch:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.dialogue = []
        self.story = Branch()



    def edit_add(self, text):
        self.dialogue.append(text)
        print(f"Added dialogue: {text}")

    def edit_remove(self, index):
        if 0 <= index < len(self.dialogue):
            removed = self.dialogue.pop(index)
            print(f"Removed dialogue: {removed}")
        else:
            print("Index out of range. No dialogue removed.")
        
    def edit_replace(self, index, text):
        if 0 <= index < len(self.dialogue):
            old_text = self.dialogue[index]
            self.dialogue[index] = text
            print(f"Replaced dialogue at index {index}: {old_text} with {text}")
        else:
            print("Index out of range. No dialogue replaced.")
    
    def edit_clear(self):
        self.dialogue.clear()
        print("Cleared all dialogue.")

    def add_branch(self, name, type):
        branch = Branch(name, type)
        self.story.append(branch)
        
