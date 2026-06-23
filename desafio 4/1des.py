from stegano import lsb

mensagem = input("Digite a mensagem secreta: ")
imagem_capa = input("Digite o nome/caminho da imagem PNG: ")
imagem_saida = input("Digite o nome da imagem de saída: ")

nova_imagem = lsb.hide(imagem_capa, mensagem)
nova_imagem.save(imagem_saida)

print("Mensagem escondida com sucesso!")
print("Imagem salva como:", imagem_saida)