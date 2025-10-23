# 1. Importando as bibliotecas necessárias
import os
import shutil

# 2. Definindo o caminho da pasta a ser organizada
caminho_da_pasta = r"C:\Users\Mateus Melo\Downloads"

# 3. Mapeando tipos de arquivos para nomes de pastas
#    (Pode ser personalizado como você quiser)
mapa_de_pastas = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv"],
    "Músicas": [".mp3", ".wav", ".aac"],
    "Compactados": [".zip", ".rar", ".7z"],
}

# 4. Obtendo a lista de todos os itens na pasta
try:
    lista_de_arquivos = os.listdir(caminho_da_pasta)
except FileNotFoundError:
    print(f"Erro: O caminho '{caminho_da_pasta}' não foi encontrado. Verifique o nome de usuário.")
    exit() # Encerra o script se a pasta não existir

# 5. Iterando sobre cada item encontrado na pasta
for arquivo in lista_de_arquivos:
    # 6. Construindo o caminho completo do arquivo
    caminho_completo_arquivo = os.path.join(caminho_da_pasta, arquivo)

    # 7. Verificando se o item é um arquivo (e não uma pasta)
    if os.path.isfile(caminho_completo_arquivo):
        
        # 8. Extraindo a extensão do arquivo em letras minúsculas
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()
        
        # 9. Encontrando a pasta de destino com base na extensão
        pasta_destino = "Outros" # Pasta padrão se a extensão não for encontrada
        for nome_pasta, extensoes in mapa_de_pastas.items():
            if extensao in extensoes:
                pasta_destino = nome_pasta
                break # Sai do loop assim que encontra a pasta correta

        # 10. Construindo o caminho completo da pasta de destino
        caminho_pasta_destino = os.path.join(caminho_da_pasta, pasta_destino)
        
        # 11. Criando a pasta de destino se ela não existir
        if not os.path.exists(caminho_pasta_destino):
            os.makedirs(caminho_pasta_destino)
            print(f"Pasta '{pasta_destino}' criada.")
            
        # 12. Movendo o arquivo para a pasta de destino
        shutil.move(caminho_completo_arquivo, caminho_pasta_destino)
        print(f"Movendo '{arquivo}' para a pasta '{pasta_destino}'")

print("\nOrganização concluída!")