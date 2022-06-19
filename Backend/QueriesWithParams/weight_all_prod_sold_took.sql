-- (4) Select the weight of all the products that a specific soldier ever took
select sum(Lending.EquipmentWeight)
from Lending
join Soldiers S on Lending.SoldierId = S.SoldierId
where S.soldierId = :soldierId;