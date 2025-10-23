import os
import shutil

def mover_com_nome_unico(src, dst_dir):
    os.makedirs(dst_dir, exist_ok=True)
    base = os.path.basename(src)
    nome, ext = os.path.splitext(base)
    destino = os.path.join(dst_dir, base)
    i = 1
    while os.path.exists(destino):
      destino = os.path.join(dst_dir, f"{nome} ({i}){ext}")
      i += 1
    shutil.move(src, destino)
    print(f"Movendo '{os.path.basename(src)}' para '{os.path.dirname(destino)}' como '{os.path.basename(destino)}'")

caminho_da_pasta = r"C:\Users\mateu.MATEUS\Downloads"

mapa_de_pastas = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv"],
    "Músicas": [".mp3", ".wav", ".aac"],
    "Compactados": [".zip", ".rar", ".7z"],
}

try:
    lista_de_arquivos = os.listdir(caminho_da_pasta)
except FileNotFoundError:
    print(f"Erro: O caminho '{caminho_da_pasta}' não foi encontrado. Verifique o nome de usuário.")
    exit()

for arquivo in lista_de_arquivos:
    caminho_completo_arquivo = os.path.join(caminho_da_pasta, arquivo)

    if os.path.isfile(caminho_completo_arquivo):
        
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()
        
        pasta_destino = "Outros" 
        for nome_pasta, extensoes in mapa_de_pastas.items():
            if extensao in extensoes:
                pasta_destino = nome_pasta
                break

        caminho_pasta_destino = os.path.join(caminho_da_pasta, pasta_destino)
        
        if not os.path.exists(caminho_pasta_destino):
            os.makedirs(caminho_pasta_destino)
            print(f"Pasta '{pasta_destino}' criada.")
            
        shutil.move(caminho_completo_arquivo, caminho_pasta_destino)
        print(f"Movendo '{arquivo}' para a pasta '{pasta_destino}'")

print("\nOrganização concluída!")