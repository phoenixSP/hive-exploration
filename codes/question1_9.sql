select distinct z.airport_names[1], y.c from (select dest, count(*) as c from flight_data_denorm where
unix_timestamp(fl_date,'yyyy-MM-dd ') > unix_timestamp('2016-12-20','yyyyMM-dd') GROUP BY dest ORDER BY c DESC limit 3) as y join (select dest, airport_names from
flight_data_denorm) as z on z.dest = y.dest;