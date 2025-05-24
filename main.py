import streamlit as st
from scipy.optimize import fsolve

st.set_page_config(page_title="Simulador de Reações Químicas Inorgânicas", layout="centered")
st.title("Molab 🧪")

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
            }
        }

reaction_name = st.selectbox("Escolha a reação química:", list(reactions.keys()))

reaction = reactions[reaction_name]
st.markdown(f"**Equação da reação:** {reaction['equation']}")

st.write("### Informe as quantidades iniciais dos reagentes (mol):")

# Input das quantidades dos reagentes
reactant_amounts = {}
for reactant in reaction["reactants"]:
    reactant_amounts[reactant] = st.number_input(f"Quantidade de {reactant} (mol):", min_value=0.0, value=1.0, step=0.1)

def calculate_products(reactants, reactant_amounts, reaction):
    # Usar a estequiometria simples para determinar o reagente limitante e calcular os produtos formados
    # Determinar coeficiente estequiométrico dos reagentes
    coef_reactants = reaction["reactants"]
    coef_products = reaction["products"]

    # Calcular o número de vezes que a reação pode ocorrer (baseado no reagente limitante)
    times_reaction = min(reactant_amounts[re] / coef_reactants[re] if coef_reactants[re] > 0 else float('inf') for re in coef_reactants)

    # Quantidades formadas dos produtos
    product_amounts = {prod: coef_products[prod] * times_reaction for prod in coef_products}

    # Quantidades restantes dos reagentes
    reactants_remaining = {re: reactant_amounts[re] - coef_reactants[re] * times_reaction for re in coef_reactants}

    return product_amounts, reactants_remaining

if st.button("Calcular produtos da reação"):
    products_formed, reactants_left = calculate_products(reaction["reactants"], reactant_amounts, reaction)
    st.write("### Produtos formados (mol):")
    for p, amt in products_formed.items():
        st.write(f"{p}: {amt:.2f} mol")

    st.write("### Reagentes restantes (mol):")
    for r, amt in reactants_left.items():
        st.write(f"{r}: {amt:.2f} mol")

