use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product;

-- 2. Выбрать названия всех автоматизированных складов
select name from store;

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale;

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select distinct store_id from sale where quantity >= 1;


-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select store.store_id from store left join sale on sale.store_id=store.store_id where sale.store_id is null;

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select name, avg(total/quantity)  frot product join sale on product.product_id=sale.product_id group by name;

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select name from (select name, store_id from product natural join sale group by name, store_id) as t group by name having( count(name)=1);

-- 8. Получить названия всех складов, с которых продавался только один продукт
select name from (select name, product_id from store natural join sale group by name, product_id) as t group by name having(count(name)=1);

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select * from sale where total = (select max(total) from sale);

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select min(date) from sale where total = (select max(total) from sale);
