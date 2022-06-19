-- (1) Select all products that almost out of the stock
select E.Id, E.Name, E.MinOfStack, E.Amount, M.Name as manufacturerName
from Equipment E
join Manufacturer M on M.Id = E.ManufacturerId
where Amount < E.MinOfStack;