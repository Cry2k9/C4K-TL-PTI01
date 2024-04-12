class Instructions:
    def __init__(self, name, ingredient, amount, key_word, rating):
        self.name = name
        self.ingredient = ingredient
        self.amount = amount
        self.key_word = key_word
        self.rating = rating

    def update(self, new_data:dict):
        for attribute, value, in new_data.items():
            if value:
                setattr(self, attribute, value)

    def element_filtering_method():
        for Cooking_Instruction in Cooking_Instructions:
            print(Cooking_Instruction.name)

    def method_to_delete_element():
        remove_name = "Fried Noodles"
        for Cooking_Instruction in Cooking_Instructions:
            if Cooking_Instruction.name == remove_name:
                Cooking_Instructions.remove(Cooking_Instruction)
            
    def element_update_method():
        new_data = {"rating": "4.7"}
        Cooking_Instruction1.update(new_data)
        print(Cooking_Instruction1.rating)

Cooking_Instruction1 = Instructions("Fried Noodles", "Ingredient", "Amount", "Key word", "Rating")
Cooking_Instruction2 = Instructions("Sweet And Sour Ribs", "Ingredient", "Amount", "Key word", "Rating")
Cooking_Instruction3 = Instructions("Salted Egg Sponge Cake", "Ingredient", "Amount", "Key word", "Rating")
Cooking_Instruction4 = Instructions("Bitter Melon Soup", "Ingredient", "Amount", "Key word", "Rating")
Cooking_Instruction5 = Instructions("Beef Steak", "Ingredient", "Amount", "Key word", "Rating")
Cooking_Instructions = [Cooking_Instruction1, Cooking_Instruction2, Cooking_Instruction3, Cooking_Instruction4, Cooking_Instruction5]

Cooking_Instruction6 = Instructions("Fresh Milk With Brown Sugar Pearls", "Ingredient", "Amount", "Key word", "Rating")
Cooking_Instructions.append(Cooking_Instruction6)

Instructions.element_filtering_method()

Instructions.method_to_delete_element()

Instructions.element_filtering_method()

Instructions.element_update_method()