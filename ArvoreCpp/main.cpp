
#include <iostream>

#include "ABP.h"

using namespace std;

/** Teste arvore binária de pesquisa */
int main() {

	cout << "Arvore Binaria de Pesquisa !\n" << endl;

	ABP arv = ABP();

	arv.insere(20);
	arv.insere(30);
	arv.insere(50);
	arv.insere(15);
	arv.insere(8);
	arv.insere(14);
	arv.insere(23);
	arv.insere(3);
	arv.insere(9);
	arv.insere(67);
	arv.insere(35);

	bool ret = arv.insere(50);
	cout << "Reinsercao do 50 = " << ret << endl;

	No *aux = arv.busca(20);
	if (aux != NULL){
		cout <<  "No = " << aux->getConteudo() << endl;
		cout << "No.esq = " << aux->getEsq()->getConteudo() << endl;
	    cout << "No.dir = " << aux->getDir()->getConteudo() << endl;
	}
	else{
		cout << "No não encontrado" << endl;
	}

	aux = arv.busca(50);
	if (aux != NULL){
		cout <<  "No = " << aux->getConteudo() << endl;
		cout << "No.esq = " << aux->getEsq()->getConteudo() << endl;
		cout << "No.dir = " << aux->getDir()->getConteudo() << endl;
	}
	else{
		cout << "No não encontrado" << endl;
	}

	aux = arv.busca(14);
	if (aux != NULL){
		cout << "\n\nNo = " << aux->getConteudo() << endl;
		if (aux->getEsq() != NULL)
			cout <<  "No.esq = " << aux->getEsq()->getConteudo() << endl;
		if (aux->getDir() != NULL)
			cout << "No.dir = " << aux->getDir()->getConteudo() << endl;
	}else{
    	cout << "No não encontrado" << endl;
	}

	aux = arv.busca(23);
	if (aux != NULL){
		cout << "\n\nNo = " << aux->getConteudo() << endl;
		if (aux->getEsq() != NULL)
			cout << "No.esq = " << aux->getEsq()->getConteudo() << endl;
		if (aux->getDir() != NULL)
			cout << "No.dir = " << aux->getDir()->getConteudo() << endl;
    }else{
    	cout << "No nao encontrado" << endl;
	}

	aux = arv.buscaIterativa(8);
	if (aux != NULL){
		cout << "\n\nNo = " << aux->getConteudo() << endl;
		if (aux->getEsq() != NULL)
			cout << "No.esq = " << aux->getEsq()->getConteudo() << endl;
		if (aux->getDir() != NULL)
			cout << "No.dir = " << aux->getDir()->getConteudo() << endl;
	}else{
	    	cout << "No nao encontrado" << endl;
	}

	cout << "Exibe em ordem crescente" << endl;
	arv.exibe();
	cout << "\nExibe em ordem decrescente" << endl;
	arv.exibeDec();

	return 0;
}
