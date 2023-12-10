max_capacity_bps = 1000000 * 1000
current_usage_bps = (200000 + 100000) * 200
current_availability_bps = max_capacity_bps - current_usage_bps
new_application_bps = 350000
new_application_usage_bps = new_application_bps * 200
availabilty_Mbps = (current_availability_bps - new_application_usage_bps) / 1000000
print("The bandwidth available with 350000 bps install in Mbps:", availabilty_Mbps,"Mbps")