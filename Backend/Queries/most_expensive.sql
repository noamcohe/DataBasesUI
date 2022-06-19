-- (15) The most expensive product
select E.Id,
       E.Name,
       E.cost
from Equipment E
where cost = (select max(cost) from Equipment);