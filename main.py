# Assign the variables for exercise 1 here:
engine_indicator_light = "green blinking"
space_suits_on = True
shuttle_cabin_ready = True
crew_status = space_suits_on and shuttle_cabin_ready
computer_status_code = 200
shuttle_speed = 15000
fuel_level = 18000
engine_temperature = 2500
command_override = False

# BEFORE running the code, predict what will be printed to the console by the following statements:

if engine_indicator_light == "green": 
  print("engines have started")
elif engine_indicator_light == "green blinking": 
  print("engines are preparing to start")
else:
  print("engines are off")

if crew_status:
  print("Crew Ready")
else:
  print("Crew Not Ready")

if computer_status_code == 200:
  print("Please stand by. Computer is rebooting.")
elif computer_status_code == 400:
  print("Success! Computer online.")
else:
  print("ALERT: Computer offline!")

if shuttle_speed > 17500:
  print("ALERT: Escape velocity reached!")
elif shuttle_speed < 8000:
  print("ALERT: Cannot maintain orbit!")
else:
  print("Stable speed")

if crew_status and computer_status_code == 200 and space_suits_on:
   print("all systems go")
else:
   print("WARNING. Not ready")

if crew_status != True or computer_status_code != 200 or not(space_suits_on):
   print("WARNING. Not ready")
else:
   print("all systems go")


if fuel_level < 1000 or engine_temperature > 3500 or engine_indicator_light == "red blinking":
   print("ENGINE FAILURE IMMINENT!")
elif fuel_level <= 5000 or engine_temperature > 2500:
   print("Check fuel level. Engines running hot.")
elif fuel_level > 20000 and engine_temperature <= 2500:
   print("Full tank. Engines good.")
elif fuel_level > 10000 and engine_temperature <= 2500:
   print("Fuel level above 50%. Engines good.")
elif fuel_level > 5000 and engine_temperature <= 2500:
   print("Fuel level above 25%. Engines good.")
else:
   print("Fuel and engine status pending...")