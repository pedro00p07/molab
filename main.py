#Importando todas as reações definidas no módulo content.reactions:
from content.reactions import *
# Importando a biblioteca Streamlit para criar a interface web:
import streamlit as st

# Define a configuração inicial das páginas
page = st.sidebar.selectbox("Escolha a página:", ["Simulador", "Tabela Periódica"])

# Condição para página da tabela periodica :
if page == "Tabela Periódica":
    st.title("Tabela Periódica 🔬")
    st.image("assets/tabela.png")
    st.stop() #Para a execução do script aqui, impedindo que a parte do simulador seja exibida

# Lógica condicional para exibir a página do Simulador:
if page != "Tabela Periódica":
    st.title("MolLab 🧪")

st.set_page_config(page_title="Simulador de Reações Químicas Inorgânicas", layout="centered")
# Cria um seletor para o usuário escolher uma reação química da lista carregada
reaction_name = st.selectbox("Escolha a reação química:", list(reactions.keys()))
reaction = reactions[reaction_name]

# Exibe a equação da reação selecionada
st.markdown("---")

st.markdown(f"**Equação da reação:** {reaction['equation']}")

st.write("### Informe as quantidades iniciais dos reagentes (mol):")

# Input das quantidades dos reagentes
reactant_amounts = {}
for reactant in reaction["reactants"]:
    reactant_amounts[reactant] = st.number_input(f"Quantidade de {reactant} (mol):", min_value=0.0, value=1.0, step=0.1)

def calculate_products(reactant_amounts, reaction):
    # Usar a estequiometria simples para determinar o reagente limitante e calcular os produtos formados
    # Determinar coeficiente estequiométrico dos reagentes
    coef_reactants = reaction["reactants"]
    coef_products = reaction["products"]

    # Calcular o número de vezes que a reação pode ocorrer (baseado no reagente limitante)
    limiting_reagent = min(
        coef_reactants,st.warning("⚠️  Atenção! Esta mistura pode ser perigosa.")
        key=lambda r: reactant_amounts[r] / coef_reactants[r] if coef_reactants[r] > 0 else float('inf')
    )
    times_reaction = reactant_amounts[limiting_reagent] / coef_reactants[limiting_reagent] if coef_reactants[limiting_reagent] > 0 else 0

    # Quantidades formadas dos produtos
    product_amounts = {prod: coef_products[prod] * times_reaction for prod in coef_products}

    st.markdown("---")

    # Quantidades restantes dos reagentes
    reactants_remaining = {re: reactant_amounts[re] - coef_reactants[re] * times_reaction for re in coef_reactants}

    return product_amounts, reactants_remaining, limiting_reagent

# Condição para executar a a função calculate_products, criando seções e exibindo os respectivos resultados 
if st.button("Calcular produtos da reação 🖩"):
    products_formed, reactants_left, limiting_reagent = calculate_products(reactant_amounts, reaction)
    st.write("### Produtos formados (mol):")
    for p, amt in products_formed.items():
        st.write(f"{p}: {amt:.2f} mol")

    # Reagentes restantes
    st.write("### Reagentes restantes (mol):")
    for r, amt in reactants_left.items():
        st.write(f"{r}: {amt:.2f} mol")

    # Determinar o reagente limitante
    st.write("### Reagente limitante:")
    st.write(f"{limiting_reagent} é o reagente limitante.")

    # st.bar_chart(products_formed)   

    # if "enthalpy" in reaction:
    #     st.write("### Entalpia de reação:")
    #     st.write(f"{reaction['enthalpy']} kJ/mol")

    #     # Adiciona alerta de segurança com base na entalpia
    #     alerta_entalpia = verificar_entalpia(reaction["enthalpy"])
    #     st.warning(alerta_entalpia)
    st.markdown("---")
    
if not reaction.get("segura", True):
    st.warning("⚠️ Atenção! Esta mistura pode ser perigosa.")
