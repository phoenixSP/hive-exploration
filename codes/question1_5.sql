select sum(dep_delay) from flight_data_denorm where airport_names[0] LIKE "%Beaumont%";