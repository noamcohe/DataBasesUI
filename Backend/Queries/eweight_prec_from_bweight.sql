-- (5) Select a list of all soldiers that have equipment more than 40% from their weight
select S.SoldierId,
       s.slName,
       s.sfName,
       S.Weight,
       sum(E.Weight)

from Soldiers S natural join Lending L
left outer join Equipment E on L.EquipmentId = E.Id
group by S.SoldierId, S.Weight
having sum(E.Weight) > (S.Weight * 0.4);