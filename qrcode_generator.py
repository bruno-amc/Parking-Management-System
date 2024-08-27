import qrcode
import os

def gerar_qrcode(dados, caminho_arquivo):
    """
    Gera um QR code a partir dos dados fornecidos e salva como imagem.
    
    :param dados: Dados a serem codificados no QR code
    :param caminho_arquivo: Caminho completo onde a imagem do QR code será salva (incluindo o nome do arquivo e extensão)
    """
    # Verifica se o diretório existe, se não, cria-o
    diretorio = os.path.dirname(caminho_arquivo)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    # Configurações do QR Code
    qr = qrcode.QRCode(
        version=1,  # Controle o tamanho do QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro
        box_size=10,  # Tamanho de cada quadrado do QR Code
        border=4,  # Largura da borda em quadrados
    )
    
    # Adiciona os dados ao QR Code
    qr.add_data(dados)
    qr.make(fit=True)
    
    # Cria a imagem do QR Code
    img = qr.make_image(fill_color='black', back_color='white')
    
    # Salva a imagem no caminho especificado
    img.save(caminho_arquivo)
