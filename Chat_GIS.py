import streamlit as st
import openai


def setup_openai():
    api_key = "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"
    openai.api_key = api_key


def chat_with_openai(prompt, model="text-davinci-003", max_tokens=300, temperature=0.8, stop_sequences=None):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        stop=stop_sequences
    )
    return response.choices[0].text.strip()


def main():
    setup_openai()
    st.title("Bem-vindo(a) ao Chat GIS!")

    st.write("Digite sua pergunta abaixo:")
    user_input = st.text_input("", "")

    if st.button("Enviar"):
        st.subheader("Sua pergunta:")
        st.write(user_input)

        esri_products = ["ArcGIS PRO", "ArcGIS Online", "ArcGIS Enterprise"]
        esri_prompt = f"Produtos ESRI: {', '.join(esri_products)}\n\nVocê: {user_input}\nChatbot:"

        response = chat_with_openai(esri_prompt, max_tokens=2048)  # Ajuste max_tokens para um número maior
        st.subheader("Resposta:")
        st.write(response)


if __name__ == "__main__":
    main()
