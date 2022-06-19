-- (2) Select a list of all the products from a specific Manufacturer
select E.Id, E.Name
from Equipment E
join Manufacturer M on M.Id = E.ManufacturerId
where M.Id == :companyId;