
listeRecette = { 
    "Pizza": ["Farine", "Eau", "Sel", "Levure", "Tomate", "Fromage"], 
    "Salade": ["Laitue", "Tomate", "Concombre", "Vinaigre", "Huile"],
    "Pâtes Carbonara": ["Pâtes", "Crème", "Lardons", "Fromage", "Sel", "Poivre"], 
    "Omelette": ["Œufs", "Sel", "Poivre", "Fromage", "Herbes"], 
    "Sandwich Jambon-Beurre": ["Pain", "Beurre", "Jambon", "Salade (optionnel)"] 
}


ing = ["Laitue", "Tomate", "Concombre", "Vinaigre", "Huile"]
recettePossible = list(filter(lambda recette: all(ingredient in ing for ingredient in listeRecette[recette]) ,listeRecette))

print(recettePossible)