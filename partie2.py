

listeRecette = { 
    "Pizza": ["Farine", "Eau", "Sel", "Levure", "Tomate", "Fromage"], 
    "Salade": ["Laitue", "Tomate", "Concombre", "Vinaigre", "Huile"],
    "Pâtes Carbonara": ["Pâtes", "Crème", "Lardons", "Fromage", "Sel", "Poivre"], 
    "Omelette": ["Œufs", "Sel", "Poivre", "Fromage", "Herbes"], 
    "Sandwich Jambon-Beurre": ["Pain", "Beurre", "Jambon", "Salade (optionnel)"] 
}

def recette(ing):
    for nom, recette in listeRecette.items():
        res = []
        for ingredient in recette:
            if ingredient in ing:
                res.append(True)
            else:
                res.append(False)
        if all(res):
            print(nom)


ing = ["Laitue", "Tomate", "Concombre", "Vinaigre", "Huile"]
recette(ing)