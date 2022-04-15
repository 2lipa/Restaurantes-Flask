class Loja():
    def __init__(self, id, nome, descricao, foto, nome_comentario, comentario1, endereco, mapa, site):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__foto = foto
        self.__nome_comentario = nome_comentario
        self.__comentario1 = comentario1
        self.__endereco = endereco
        self.__mapa = mapa
        self.__site = site

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def get_foto(self):
        return self.__foto

    def get_nome_comentario(self):
        return self.__nome_comentario

    def get_comentario(self):
        return self.__comentario1

    def get_endereco(self):
        return self.__endereco

    def get_mapa(self):
        return self.__mapa

    def get_site(self):
        return self.__site
    