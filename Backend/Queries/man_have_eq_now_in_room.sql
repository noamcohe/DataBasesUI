-- (16) List of all manufacturers that have an equipment,
-- that are exist right now in one of the rooms
select M.Id,
       M.Name,
       count(M.Id)
from Manufacturer M
left join Equipment E on M.Id = E.ManufacturerId
where roomId is not null
group by M.Id, M.Name;