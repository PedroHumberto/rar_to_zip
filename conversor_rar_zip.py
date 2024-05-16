import os
import rarfile
import zipfile
import tempfile

def rar_to_zip(rar_path, zip_path):
    if not os.path.exists(rar_path):
        print(f"O arquivo {rar_path} não existe.")
        return
    
    # ATENÇÃO: Altere o caminho abaixo para onde o unrar está instalado no seu computador
    rarfile.UNRAR_TOOL = r"C:\\Program Files\WinRAR\\UnRAR.exe"
    
    with tempfile.TemporaryDirectory() as temp_dir:
        with rarfile.RarFile(rar_path) as rar:
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                # Itera sobre cada arquivo/diretório no arquivo RAR
                for rarinfo in rar.infolist():
                    # Extrai o arquivo/diretório
                    rar.extract(rarinfo, temp_dir)
                    extracted_file = os.path.join(temp_dir, rarinfo.filename)
                    
                    # Verifica se é um diretório ou um arquivo
                    if rarinfo.isdir():
                        # Adiciona o diretório ao ZIP (necessário para diretórios vazios)
                        zipf.write(extracted_file, rarinfo.filename)
                    else:
                        with open(extracted_file, 'rb') as f:
                            file_data = f.read()
                        zipf.writestr(rarinfo.filename, file_data)
    
        print(f"Arquivo {zip_path} criado com sucesso.")

# Exemplo de uso
rar_to_zip('NFC_Rar.rar', 'NFC.zip')
