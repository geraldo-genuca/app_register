drop database app_test;

create database app_test;

use app_test;

create table cad_pes_fis(
	id INT NOT NULL auto_increment,
    nome VARCHAR(50) NOT NULL,
    data_nasc DATE,
    cpf VARCHAR(15) NOT NULL,
    email VARCHAR(50) NOT NULL,
    sexo CHAR(2) NOT NULL,
    logradouro VARCHAR(50),
    numero INT(10),
    compl VARCHAR(30),
    cep MEDIUMINT(6),
    cep_dig SMALLINT(4),
    ddd_tele TINYINT(3)NOT NULL,
    tele INT(10)NOT NULL,
    ddd_tele_com TINYINT(3),
    tele_com INT(10),    
    PRIMARY KEY(id)
);
    
