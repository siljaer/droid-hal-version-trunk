# rpm_device is the name of the ported device
%define rpm_device trunk
# rpm_vendor is used in the rpm space
%define rpm_vendor elephone
# Manufacturer and device name to be shown in UI
%define vendor_pretty Elephone
%define device_pretty Trunk
# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 1
%define have_led 1
%include droid-hal-version/droid-hal-version.inc
