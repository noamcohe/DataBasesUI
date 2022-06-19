-- (3) Select a list of all the products that a specific soldier ever took
select E.Id,
       E.Name
from Equipment E
join Lending L on E.Id = L.EquipmentId
left join Soldiers S on S.SoldierId = L.SoldierId
where S.soldierId == :soldierId;