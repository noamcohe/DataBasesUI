-- (9) Select a list of all soldiers who have a product that doesn't work
select S.SoldierId,
       S.sfName,
       S.slName
from Soldiers S natural join Lending L
left join Equipment E on E.Id = L.EquipmentId
where L.EquipmentId == E.Id and E.worker == FALSE
group by S.SoldierId, S.sfName, S.slName;