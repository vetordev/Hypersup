use mercado;
/*aqui vai ter uma função pra calcular preço lote + 50% (p ter o lucro)*/
insert into produto value('1','Arroz','Agulhinha Tipo 1 Pacote 5kg','Prato fino','Mercearia','18.00');
insert into produto value('2','Feijão','Carioca 1kg Pacote','Camil','Mercearia','6.00');
insert into produto value('3','Requeijão','Cremoso 200g','Vigor','Mercearia','5.00');


insert into lote value('1','1','2020-04-20','12.00','240');
insert into lote value('2','1','2020-04-20','3.00','60');
insert into lote value('3','1','2020-04-20','2.50','50');


insert into estoque value('1','1');
insert into estoque value('2','2');
insert into estoque value('3','3');


insert into gondola value('1','1','1','100');
insert into gondola value('2','2','2','70');
insert into gondola value('3','3','3','50');


insert into venda value('1','54.00','2020-03-13');
insert into venda value('2','32.00','2020-03-10');
insert into venda value('3','90.00','2020-03-07');

/*mais insert's pra facilitar*/
insert into item_venda value('1','1','1','2');
insert into item_venda value('2','1','2','3');
insert into item_venda value('3','2','3','4');
insert into item_venda value('4','2','2','2');
insert into item_venda value('5','3','1','5');


insert into caixa value('1','1', null); 
insert into caixa value('2','2', null); 
insert into caixa value('3','3', null); 


insert into cofre value('1','1', null, null);
insert into cofre value('2','2', null, null);
insert into cofre value('3','3', null, null);


insert into encomenda value('1','1', '20');

select * from produto;
select * from lote;
select * from estoque;
select * from gondola;
select * from venda;
select * from item_venda;
select * from caixa;
select * from cofre;
select * from encomenda;

CREATE VIEW VENDA_PRODUTO AS 
SELECT c.id_caixa, v.id_venda, p.nome, p.descricao, p.marca, p.setor, p.preco FROM CAIXA as c JOIN VENDA as v JOIN ITEM_VENDA as iv JOIN PRODUTO as p
ON(c.id_venda = v.id_venda and iv.id_venda = v.id_venda and p.id_produto = iv.id_produto );

SELECT * FROM VENDA_PRODUTO;
