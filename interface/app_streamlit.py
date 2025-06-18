import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agentes.pesquisador import pesquisar_tema
from agentes.redator import redigir_post
from agentes.revisor import revisar_post
from agentes.otimizador_linkedin import otimizar_post
from utilitarios.gerador_pdf import salvar_pdf

st.title('🤖 Criador de Post')

tema = st.text_input('Digite o tema do post:')

if st.button('Gerar Post'):
    if tema.strip():  # Verifica se o tema não está vazio
        # Exibe o spinner com mensagem de aguarde
        with st.spinner('Aguarde, estamos gerando seu post...'):
            try:
                # Processo de geração do post
                info = pesquisar_tema(tema)
                rascunho = redigir_post(info)
                revisado = revisar_post(rascunho)
                final = otimizar_post(revisado)
                
                # Salva o PDF
                salvar_pdf(final, 'post_final.pdf')
                
                # Exibe mensagem de sucesso
                st.success('✅ Post gerado com sucesso!')
                
                # Exibe o post gerado
                st.text_area('Post Gerado', final, height=200)
                
                # Cria duas colunas para os botões ficarem lado a lado
                col1, col2 = st.columns(2)
                
                with col1:
                    # Botão de download
                    with open('post_final.pdf', 'rb') as f:
                        st.download_button(
                            '📄 Baixar PDF', 
                            f, 
                            file_name='post_linkedin.pdf',
                            mime='application/pdf'
                        )
                
                with col2:
                    # Botão para limpar a tela
                    if st.button('🧹 Limpar a Tela'):
                        st.rerun()
                        
            except Exception as e:
                st.error(f'❌ Erro ao gerar o post: {str(e)}')
    else:
        st.warning('⚠️ Por favor, digite um tema para gerar o post.')