from bridge_tv_remote import *

# Test codes

"""
Testing DeviceToshiba with Universal Remote
"""
my_device = DeviceToshiba()
my_remote = UniversalRemote(my_device)

my_remote.power_button_pressed()
my_remote.power_button_pressed()

my_remote.function_button_pressed()
my_remote.function_button_pressed()


print("\n==================[{message}]==================\n".format(
    message="changing device..."))

"""
Testing DeviceAltecLansing with Universal Remote
"""
my_new_device = DeviceAltecLansing()
my_remote = UniversalRemote(my_new_device)

my_remote.power_button_pressed()
my_remote.power_button_pressed()

my_remote.function_button_pressed()
my_remote.function_button_pressed()

print("\n==================[{message}]==================\n".format(
    message="changing device..."))

my_device = DeviceToshiba()
my_remote = ReversalPrankRemote(my_device)

my_remote.power_button_pressed()
my_remote.power_button_pressed()

print("[say] Let's try 'increasing' the volume 5 times")
for i in range(5):
    my_remote.button_plus_pressed()
print("[say] My volume is now ... {my_volume}, EHHHH ???!!".format(
    my_volume=str(my_remote.volume)))

print("[say] Let's try the 'decreasing' volume button")
for i in range(5):
    my_remote.button_minus_pressed()
print("[say] My volume is now ... {my_volume}, EHHHH ???!!".format(
    my_volume=str(my_remote.volume)))
print("[say] Hmm... i think someone is playing a prank on me")