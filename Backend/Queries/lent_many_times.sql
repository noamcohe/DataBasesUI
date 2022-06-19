-- (6) Select names list of all products
-- that lent more than 9 times (for maintenance)
select E.Id, E.Name
from Equipment E
left outer join Lending L on E.Id = L.EquipmentId
group by E.Name
having count(L.EquipmentId) > 9;