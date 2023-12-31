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
        self._esq = esq  # Corrigido aqui
    

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
        return self._busca(self.raiz, valor)

    def _busca(self, no, valor):
        if no is None or no.conteudo == valor:
            return no
        if valor < no.conteudo:
            return self._busca(no.esq, valor)
        else:
            return self._busca(no.dir, valor)
        
    def exibe(self):
        if self.raiz is None:
            print("Árvore vazia")
            pass
        else:
            self._exibe(self.raiz)
            pass

    def _exibe(self, no_t):  # Método auxiliar _exibe
        if no_t is not None:
            self._exibe(no_t.esq)
            print(f" {no_t.conteudo}")
            self._exibe(no_t.dir)

    def exibe_dec(self):
        if self.raiz is None:
            print("Árvore vazia")
            pass
        else:
            self._exibe_dec(self.raiz)
            pass

    def _exibe_dec(self, no_t):  # Método auxiliar _exibe_dec
        if no_t is not None:
            self._exibe_dec(no_t.dir)
            print(f" {no_t.conteudo}")
            self._exibe_dec(no_t.esq)    

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

        # Fora do loop while
        if valor < no_p.conteudo:
            no_p.esq = novo_no
        else:
            no_p.dir = novo_no
        
        return True

    
    def remove(self, valor):
        self.raiz, removed = self._remove(self.raiz, valor)
        return removed

    def _remove(self, no, valor):
        if no is None:
            return no, False

        if valor < no.conteudo:
            no.esq, removed = self._remove(no.esq, valor)
        elif valor > no.conteudo:
            no.dir, removed = self._remove(no.dir, valor)
        else:
            if no.esq is None:
                return no.dir, True
            elif no.dir is None:
                return no.esq, True
            else:
                temp = self._minValueNode(no.dir)
                no.conteudo = temp.conteudo
                no.dir, _ = self._remove(no.dir, temp.conteudo)
                removed = True
        return no, removed

    def _minValueNode(self, no):
        current = no
        while(current.esq is not None):
            current = current.esq
        return current
    
    def pre_ordem(self):
        if self.raiz is None:
            return "Árvore vazia"
        else:
            return self._pre_ordem(self.raiz, "")[:-2]

    def _pre_ordem(self, no, result):
        if no is not None:
            result += str(no.conteudo) + ", "
            result = self._pre_ordem(no.esq, result)
            result = self._pre_ordem(no.dir, result)
        return result
    
    def in_ordem(self):
        if self.raiz is None:
            return "Árvore vazia"
        else:
            return self._in_ordem(self.raiz, "")[:-2]

    def _in_ordem(self, no, result):
        if no is not None:
            result = self._in_ordem(no.esq, result)
            result += str(no.conteudo) + ", "
            result = self._in_ordem(no.dir, result)
        return result
    
    def pos_ordem(self):
        if self.raiz is None:
            return "Árvore vazia"
        else:
            return self._pos_ordem(self.raiz, "")[:-2]

    def _pos_ordem(self, no, result):
        if no is not None:
            result = self._pos_ordem(no.esq, result)
            result = self._pos_ordem(no.dir, result)
            result += str(no.conteudo) + ", "
        return result
    
    
class NoGrafico:
        def __init__(self, no, pos_x, pos_y):
            self.no = no
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.raio = 20  # O raio do círculo que representa o nó