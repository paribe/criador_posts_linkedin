from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from datetime import datetime
import textwrap

def salvar_pdf(texto, caminho):
    """
    Salva o texto em um PDF bem formatado
    """
    try:
        # Configurar documento
        doc = SimpleDocTemplate(caminho, pagesize=A4,
                              rightMargin=72, leftMargin=72,
                              topMargin=72, bottomMargin=18)
        
        # Estilos
        styles = getSampleStyleSheet()
        story = []
        
        # Título
        titulo = Paragraph("Post para LinkedIn", styles['Title'])
        story.append(titulo)
        story.append(Spacer(1, 12))
        
        # Data e informações
        data_atual = datetime.now().strftime('%d/%m/%Y às %H:%M')
        info = Paragraph(f"<b>Gerado em:</b> {data_atual}", styles['Normal'])
        story.append(info)
        story.append(Spacer(1, 12))
        
        # Linha separadora
        linha = Paragraph("_" * 50, styles['Normal'])
        story.append(linha)
        story.append(Spacer(1, 12))
        
        # Conteúdo do post
        conteudo_titulo = Paragraph("<b>Conteúdo do Post:</b>", styles['Heading2'])
        story.append(conteudo_titulo)
        story.append(Spacer(1, 6))
        
        # Texto do post (quebrar linhas longas)
        linhas = texto.split('\n')
        for linha in linhas:
            if linha.strip():
                para = Paragraph(linha, styles['Normal'])
                story.append(para)
                story.append(Spacer(1, 6))
        
        # Estatísticas
        story.append(Spacer(1, 12))
        stats = Paragraph(f"<b>Estatísticas:</b><br/>Caracteres: {len(texto)}", 
                         styles['Normal'])
        story.append(stats)
        
        # Construir PDF
        doc.build(story)
        return True
        
    except Exception as e:
        print(f"Erro ao salvar PDF: {e}")
        return False