from datetime import datetime

#função para gravar um log com exceções
def saveLog(filename, text):

    #tenta
    try:

        #abrir o ficheiro log.txt para acrescentar 
        f = open("exceptions.log", "a")

        #escreve a mensagem desejada com a data e hora 
        f.write("\n" + str(text) + '\t' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")

        #fecha o documento
        f.close()

        #retorna verdadeiro em conforme foi guardado o log
        return True

    #em caso de exceção
    except: 

        #retorna false em conforme não foi guardado o log
        return False