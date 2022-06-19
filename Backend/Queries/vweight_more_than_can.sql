-- (11) select all vehicles that hold more heavy equipment than they can
select V.vid, V.maxWight, sum (E.Weight)
from Vehicles V  join Equipment E on V.vid = E.onVehicleId
group by V.vid, V.maxWight
having sum (E.Weight) > V.maxWight;