class No:
    def __init__(self):
        self._conteudo = None
        self._dir = None
        self._esq = None

    @property
    def conteudo(self):
        return self._conteudo
    
    @conteudo.setter
    def conteudo(self, conteudo):
        self._conteudo = conteudo

    @property
    def dir(self):
        return self._dir
    
    @dir.setter
    def dir(self, dir):
        self._dir = dir

    @property
    def esq(self):
        return self._esq
    
    @esq.setter
    def esq(self, esq):
        self._raiz = esq
    

class ArvoreBinariaPesquisa:
    def __init__(self):
        self._raiz = None

    @property
    def raiz(self):
        return self._raiz
    
    @raiz.setter
    def raiz(self, raiz):
        self._raiz = raiz

    def vazia(self):
        return self._raiz is None
    

    def busca(self, no_t, valor):
        if no_t is None:
            return None  # àrvore vazia
        
        if no_t.conteudo == valor:
            return no_t
        elif valor < no_t.conteudo:
            return self.busca(no_t.esq, valor)
        else:
            return self.busca(no_t.dir, valor)
        
    def busca(self, valor):
        return self.busca(self.raiz, valor)
    
    def busca_iterativa(self, valor):
        if self.vazia():
            return None
        
        no_aux = self.raiz
        while no_aux is not None:
            if no_aux.conteudo == valor:
                return no_aux
            elif no_aux.conteudo > valor:
                no_aux = no_aux.esq
            else:
                no_aux = no_aux.dir
        
        return None
    
    def exibe(self, no_t):
        if no_t is not None:
            self.exibe(no_t.esq)
            print(f" {no_t.conteudo}")
            self.exibe(no_t.dir)

    def exibe(self):
        if self.raiz is None:
            print("Árvore vazia")
            pass
        else:
            self.exibe(self._raiz)
            pass

    def exibe_dec(self, no_t):
        if no_t is not None:
            self.exibe_dec(no_t.dir)
            print(f" {no_t.conteudo}")
            self.exibe_dec(no_t.dir)

    def exibe_dec(self):
        if self.raiz is None:
            print("Árvore vazia")
            pass
        else:
            self.exibe_dec(self._raiz)
            pass         

    def insere(self, valor):
        novo_no = No()
        novo_no.conteudo = valor
        novo_no.esq = None
        novo_no.dir = None

        if self.raiz is None:
            self.raiz = novo_no
            return True
        
        no_aux = self.raiz
        no_p = None

        while no_aux is not None:
            no_p = no_aux

            if valor == no_aux.conteudo:
                return False
            
            if valor < no_aux.conteudo:
                no_aux = no_aux.esq
            else:
                no_aux = no_aux.dir
            
        if valor < no_p.conteudo:
            no_p.esq = novo_no
        else:
            no_p.dir = novo_no
            
        return True
    
class NoGrafico:
        def __init__(self, no, pos_x, pos_y):
            self.no = no
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.raio = 20  # O raio do círculo que representa o nó