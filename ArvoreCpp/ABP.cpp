/*
 * ABP.cpp
 *
 *  Created on: 11 de abr. de 2023
 *      Author: tiagomaritan
 */

#include "ABP.h"

#include <iostream>

using namespace std;

ABP::ABP() {
	raiz = NULL;
}

ABP::~ABP() {
}

/** Verifica se a árvore está vazia */
bool ABP::vazia (){
	return (raiz == NULL);
}

/**Buscar recursivamente a partir da raiz.
    Retorna o endereço se o elemento for
    encontrado, caso contrário retorna NULL*/
No *ABP::busca(No *T, int valor) {
	if (T == NULL)
		return NULL;  // Arvore Vazia

	if(T->getConteudo() == valor)
		return T; 	// Elem. encontrado na raiz

	if (valor < T->getConteudo())
		return busca(T->getEsq(), valor);
	else
		return busca(T->getDir(), valor);
}

/**Buscar um elemento na ABP
	Retorna o endereço se o elemento for
    encontrado, caso contrário retorna NULL*/
No *ABP::busca(int valor) {
	return busca(raiz, valor);
}

No *ABP::buscaIterativa(int valor) {
	if (vazia())
		return NULL;

	No *aux = raiz;
	while (aux != NULL) {
		// Verificando se o conteudo do no atual
		// é igual ao valor procurado
		if (aux->getConteudo() == valor)
			return aux;

		// Se o valor procurado for menor que raiz,
		// continue pesquisando na sub-arv da esq.
		if (valor < aux->getConteudo())
			aux = aux->getEsq();
		// Caso contratio, pesquise na sub-arv da direita
		else
			aux = aux->getDir();
	}

		return NULL;
}


/**Exibe o conteúdo de uma árvore no formato in-ordem
    (preserva a ordenação)*/
void ABP::exibe (No *T){
	if (T != NULL) {
		exibe(T->getEsq());
		cout <<  " " << T->getConteudo();
		exibe(T->getDir());
	}
}

void ABP::exibe() {
	if (raiz == NULL)
		cout << "Arvore vazia" << endl;
	else
		exibe(raiz);
}

/**Exibe o conteúdo de uma árvore no formato in-ordem
 (preserva a ordenação)*/
void ABP::exibeDec(No *T){
	if (T != NULL) {
		exibeDec(T->getDir());
		cout << " " << T->getConteudo();
		exibeDec(T->getEsq());
	}
}

void ABP::exibeDec() {
	if (raiz == NULL)
		cout << "Arvore vazia" << endl;
	else
		exibeDec(raiz);
}

/**Insere um nó em uma árvore ABP
   Retorna 1 se a inserção for com sucesso.
    Caso contrário retorna 0*/
bool ABP::insere(int valor){

	No *novoNo = new No();
	novoNo->setConteudo(valor);
	novoNo->setEsq(NULL);
	novoNo->setDir(NULL);

	// Quando a arvore estiver vazia, o novoNó será a raiz da arv
	if (raiz == NULL){
 		raiz = novoNo;
		return true;
	}

    // Procura a posicao correta pra inserir o novo no
    No *aux = raiz;
    No *p = NULL;
    while (aux != NULL) {
    	p = aux;

    	// Se valor inserido for igual a um existente
	    //na arvore, nao insira.
	    if (valor == aux->getConteudo())
			return false;

    	if (valor < aux->getConteudo())
			aux = aux->getEsq();
		else
			aux = aux->getDir();
	}

	// Encontrou um nó folha para inserir
	if (valor < p->getConteudo())
		p->setEsq(novoNo);
	else
		p->setDir(novoNo);

	return true;
}

