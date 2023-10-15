/*
 * No.cpp
 *
 *  Created on: 11 de abr. de 2023
 *      Author: tiagomaritan
 */

#include <stdlib.h>

#include "No.h"


No::No() {
	esq = NULL;
	dir = NULL;

}

No::~No() {
}

int No::getConteudo() {
	return conteudo;
}

No *No::getEsq() {
	return esq;
}

No *No::getDir() {
	return dir;
}

void No::setConteudo(int conteudo) {
	this->conteudo = conteudo;
}

void No::setEsq(No *esq) {
	this->esq = esq;
}

void No::setDir(No *dir) {
	this->dir = dir;
}

