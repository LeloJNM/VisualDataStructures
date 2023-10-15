/*
 * ABP.h
 *
 *  Created on: 11 de abr. de 2023
 *      Author: tiagomaritan
 */

#ifndef ABP_H_
#define ABP_H_

#include "No.h"

class ABP {
	private:
		No *raiz;

		No *busca(No *T, int valor);
		void exibe (No *T);
		void exibeDec(No *T);

	public:
		ABP();
		virtual ~ABP();

		bool vazia ();
		No *busca(int valor);
		No *buscaIterativa(int valor);
		void exibe();
		void exibeDec();
		bool insere(int valor);

};

#endif /* ABP_H_ */
