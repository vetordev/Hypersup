-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mercado
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mercado
-- -----------------------------------------------------
drop database `mercado`;
CREATE SCHEMA IF NOT EXISTS `mercado` DEFAULT CHARACTER SET utf8 ;
USE `mercado` ;

-- -----------------------------------------------------
-- Table `mercado`.`produto`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mercado`.`produto` ;

CREATE TABLE IF NOT EXISTS `mercado`.`produto` (
  `id_produto` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `descricao` VARCHAR(60) NOT NULL,
  `marca` VARCHAR(45) NOT NULL,
  `setor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_produto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mercado`.`lote`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mercado`.`lote` ;

CREATE TABLE IF NOT EXISTS `mercado`.`lote` (
  `id_lote` INT NOT NULL,
  `id_produto` INT NOT NULL,
  `validade_lote` DATE NOT NULL,
  `preco_unidade` FLOAT NOT NULL,
  `preco_lote` FLOAT NOT NULL,
  PRIMARY KEY (`id_lote`),
  CONSTRAINT `id_produtoLote`
    FOREIGN KEY (`id_produto`)
    REFERENCES `mercado`.`produto` (`id_produto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mercado`.`estoque`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mercado`.`estoque` ;

CREATE TABLE IF NOT EXISTS `mercado`.`estoque` (
  `id_estoque` INT NOT NULL,
  `id_lote` INT NOT NULL,
  PRIMARY KEY (`id_estoque`),
  CONSTRAINT `id_loteEstoque`
    FOREIGN KEY (`id_lote`)
    REFERENCES `mercado`.`lote` (`id_lote`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mercado`.`gondola`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mercado`.`gondola` ;

CREATE TABLE IF NOT EXISTS `mercado`.`gondola` (
  `id_gondola` INT NOT NULL,
  `id_estoque` INT NOT NULL,
  `id_produto` INT NOT NULL,
  `quantidade_produto` INT NOT NULL,
  PRIMARY KEY (`id_gondola`),
  CONSTRAINT `id_estoqueGondola`
    FOREIGN KEY (`id_estoque`)
    REFERENCES `mercado`.`estoque` (`id_estoque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_produtoGondola`
    FOREIGN KEY (`id_produto`)
    REFERENCES `mercado`.`produto` (`id_produto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mercado`.`venda`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mercado`.`venda` ;

CREATE TABLE IF NOT EXISTS `mercado`.`venda` (
  `id_venda` INT NOT NULL,
  `preco_total` FLOAT NOT NULL,
  `data_venda` DATE NOT NULL,
  PRIMARY KEY (`id_venda`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mercado`.`item_venda`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mercado`.`item_venda` ;

CREATE TABLE IF NOT EXISTS `mercado`.`item_venda` (
`id_item_venda` INT NOT NULL,
`id_venda` INT NOT NULL,
`id_produto` INT NOT NULL,
`quantidade` INT NOT NULL,
	PRIMARY KEY (`id_item_venda`),
	CONSTRAINT `id_vendaItem`
    FOREIGN KEY (`id_venda`)
    REFERENCES `mercado`.`venda` (`id_venda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	CONSTRAINT `id_itemVendaProduto`
    FOREIGN KEY (`id_produto`)
    REFERENCES `mercado`.`produto` (`id_produto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mercado`.`caixa`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mercado`.`caixa` ;

CREATE TABLE IF NOT EXISTS `mercado`.`caixa` (
  `id_caixa` INT NOT NULL,
  `id_venda` INT NOT NULL,
  `lucro_diario` FLOAT,
  PRIMARY KEY (`id_caixa`),
  CONSTRAINT `id_vendaCaixa`
    FOREIGN KEY (`id_venda`)
    REFERENCES `mercado`.`venda` (`id_venda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mercado`.`cofre`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mercado`.`cofre` ;

CREATE TABLE IF NOT EXISTS `mercado`.`cofre` (
  `id_cofre` INT NOT NULL,
  `id_caixa` INT NOT NULL,
  `lucro_semanal` FLOAT,
  `lucro_mensal` FLOAT,
  PRIMARY KEY (`id_cofre`),
  CONSTRAINT `id_caixaCofre`
    FOREIGN KEY (`id_caixa`)
    REFERENCES `mercado`.`caixa` (`id_caixa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mercado`.`encomenda`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mercado`.`encomenda` ;

CREATE TABLE IF NOT EXISTS `mercado`.`encomenda` (
  `id_encomenda` INT NOT NULL,
  `id_lote` INT NOT NULL,
  `quantidade_lote` INT NOT NULL,
  PRIMARY KEY (`id_encomenda`),
  CONSTRAINT `id_loteEncomenda`
    FOREIGN KEY (`id_lote`)
    REFERENCES `mercado`.`lote` (`id_lote`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;