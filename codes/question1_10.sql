select dest, count(*) as c from flight_data_denorm where airport_names[1] like '%, MT:%' GROUP BY dest ORDER BY c DESC limit 1;