-- (13) select all soldiers that have a gun, and their duty
-- (to confirm that they really need a gun)
select s.soldierId, s.slname, s.sfName, D.dName, D.dDescription
from Lending L
join Equipment E on E.Id = L.EquipmentId
join Soldiers S on S.soldierId = L.SoldierId
left outer join Duties D on S.dutyId = D.did
where E.Name == 'gun'
group by S.soldierId, s.slname, s.sfName, D.dName, D.dDescription;