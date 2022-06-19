-- (14) select all rooms with the duties of its soldiers
select R.rid, D.dName,D.dDescription
from Rooms R join Soldiers S on R.rid = S.roomId
join Duties D on D.did = S.dutyId
group by R.rid, D.dName;