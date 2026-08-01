import streamlit as st

# 1. Configuração da Página (Deve ser o primeiro comando)
st.set_page_config(
    page_title="Soluções em Processamento de Dados",
    page_icon="⚙️",
    layout="centered", # Mantém o design minimalista e responsivo
    initial_sidebar_state="collapsed"
)

# 2. CSS Customizado para visual de "Site Estático"
# Isso esconde o menu superior padrão do Streamlit e o rodapé
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. Cabeçalho Principal (Hero Section)
st.title("Transformamos seus dados em tempo e resultado.")
st.markdown("""
Ajudamos pequenas empresas a crescerem através da **automação de tarefas** e do **processamento inteligente de dados**. 
Deixe o trabalho manual e repetitivo conosco e foque no que realmente importa: o seu negócio.
""")

st.divider() # Linha divisória minimalista

# 4. Nossos Serviços (Com espaço para 2 imagens)
st.header("Nossos Serviços")
st.write("Oferecemos soluções sob medida para a realidade da sua empresa:")

# Criando duas colunas para alinhar os serviços lado a lado no desktop (no mobile, elas empilham automaticamente)
col1, col2 = st.columns(2, gap="large")

with col1:
    # Substitua 'servico1.jpg' pelo nome do seu arquivo de imagem
    # use_container_width=True garante que a imagem se ajuste perfeitamente ao mobile e desktop
    st.image("image1.jpg", use_container_width=True)
    st.subheader("Automação de Processos")
    st.write("""
    Eliminamos planilhas manuais e tarefas repetitivas. Criamos fluxos automatizados que rodam sozinhos, reduzindo erros humanos e economizando dezenas de horas da sua equipe todos os meses.
    """)

with col2:
    # Substitua 'servico2.jpg' pelo nome do seu arquivo de imagem
    st.image("image2.jpg", use_container_width=True)
    st.subheader("Processamento de Dados")
    st.write("""
    Organizamos, limpamos e estruturamos as informações da sua empresa. Transformamos dados soltos em relatórios claros e precisos para facilitar a sua tomada de decisão.
    """)

st.divider()

# 5. Seção de Contato
st.header("Entre em Contato")
st.markdown("""
Pronto para dar o próximo passo na modernização da sua empresa? 
Fale conosco para uma avaliação sem compromisso.
""")

# Informações de contato diretas
st.write("📧 **E-mail:** contato@suaempresa.com.br")
st.write("📱 **WhatsApp:** (11) 99999-9999")
st.write("📍 **Localização:** Atendemos de forma 100% remota.")

# Botão de ação (Call to Action) para o WhatsApp
link_whatsapp = "https://wa.me/5511974760069?text=Olá,%20gostaria%20de%20saber%20mais%20sobre%20os%20serviços%20de%20dados."
st.link_button("Falar com um Consultor via WhatsApp", link_whatsapp, type="primary")