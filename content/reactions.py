#Entalpias de formação padrão (ΔHf°) em kJ/mol

entalpias_formacao = {
        "HCl": -92.3,
        "NaOH": -469.15,
        "NaCl": -411.12,
        "H2O": -285.8,
        "CaO": -635.5,
        "Ca(OH)2": -986.2,
        "CO2": -393.5,
        "H2CO3": -699.7,
        "Mg": 0.0,
        "O2": 0.0,
        "MgO": -601.6,
        "H2": 0.0,
        "Cl2": 0.0,
        "Zn": 0.0,
        "ZnCl2": -415.0,
        "H2SO4": -814.0,
        "Na2SO4": -1387.1,
        "AgNO3": -124.4,
        "AgCl": -127.0,
        "NaNO3": -467.8,
        "CaCl2": -795.8,
        "Na2CO3": -1130.7,
        "CaCO3": -1206.9,
        "CuO": -155.2,
        "CuSO4": -769.9
        }

# Reações:
reactions = {
        "Reação 1: Ácido clorídrico + Hidróxido de sódio": {
            "equation": "HCl + NaOH -> NaCl + H2O",
            "reactants": {"HCl": 1, "NaOH": 1},
            "products": {"NaCl": 1, "H2O": 1}
            },
        "Reação 2: Óxido de cálcio + Água": {
            "equation": "CaO + H2O -> Ca(OH)2",
            "reactants": {"CaO": 1, "H2O": 1},
            "products": {"Ca(OH)2": 1}
            },
        "Reação 3: Dióxido de carbono + Água": {
            "equation": "CO2 + H2O -> H2CO3",
            "reactants": {"CO2": 1, "H2O": 1},
            "products": {"H2CO3": 1}
            },
        "Reação 4: Magnésio + Oxigênio": {
            "equation": "2Mg + O2 -> 2MgO",
            "reactants": {"Mg": 2, "O2": 1},
            "products": {"MgO": 2}
            },
        "Reação 5: Hidrogênio + Cloro": {
            "equation": "H2 + Cl2 -> 2HCl",
            "reactants": {"H2": 1, "Cl2": 1},
            "products": {"HCl": 2}
            },
        "Reação 6: Zinco + Ácido clorídrico": {
            "equation": "Zn + 2HCl -> ZnCl2 + H2",
            "reactants": {"Zn": 1, "HCl": 2},
            "products": {"ZnCl2": 1, "H2": 1}
            },
        "Reação 7: Ácido sulfúrico + Hidróxido de sódio": {
            "equation": "H2SO4 + 2NaOH -> Na2SO4 + 2H2O",
            "reactants": {"H2SO4": 1, "NaOH": 2},
            "products": {"Na2SO4": 1, "H2O": 2}
            },
        "Reação 8: Nitrato de prata + Cloreto de sódio": {
            "equation": "AgNO3 + NaCl -> AgCl + NaNO3",
            "reactants": {"AgNO3": 1, "NaCl": 1},
            "products": {"AgCl": 1, "NaNO3": 1}
            },
        "Reação 9: Cloreto de cálcio + Carbonato de sódio": {
            "equation": "CaCl2 + Na2CO3 -> CaCO3 + 2NaCl",
            "reactants": {"CaCl2": 1, "Na2CO3": 1},
            "products": {"CaCO3": 1, "NaCl": 2}
            },
        "Reação 10: Óxido de cobre(II) + Ácido sulfúrico": {
            "equation": "CuO + H2SO4 -> CuSO4 + H2O",
            "reactants": {"CuO": 1, "H2SO4": 1},
            "products": {"CuSO4": 1, "H2O": 1}
            }
}

def calcular_delta_H(reactants, products, entalpias_formacao):
    """
    Calcula a variação de entalpia (ΔH) da reação.
    Parâmetros:
    - reactants: dicionário com substâncias reagentes e suas quantidades
    - products: dicionário com substâncias produtos e suas quantidades
    - entalpias_formacao: dicionário com ΔHf° das substâncias
    """
    try:
        H_reactants = sum(entalpias_formacao[comp] * mol for comp, mol in reactants.items())
        H_products = sum(entalpias_formacao[comp] * mol for comp, mol in products.items())
        return H_products - H_reactants
    except KeyError as e:
        return f"Erro: entalpia de formação desconhecida para '{e.args[0]}'"


for nome, dados in reactions.items():
    delta_H = calcular_delta_H(dados["reactants"], dados["products"], entalpias_formacao)
    print(f"{nome}")
    print(f"Equação: {dados['equation']}")
    print(f"ΔH = {delta_H} kJ/mol")
    print("-" * 50)
