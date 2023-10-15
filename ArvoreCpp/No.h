/*
 * No.h
 *
 *  Created on: 11 de abr. de 2023
 *      Author: tiagomaritan
 */

#ifndef NO_H_
#define NO_H_

class No {

	private:
		int conteudo;
		No *esq;
		No *dir;


	public:
		No();
		virtual ~No();

		int getConteudo();
		No *getEsq();
		No *getDir();

		void setConteudo(int conteudo);
		void setEsq(No *esq);
		void setDir(No *dir);

};

#endif /* NO_H_ */
