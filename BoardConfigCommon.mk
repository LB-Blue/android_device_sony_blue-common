# Copyright (C) 2015 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# inherit from msm8960-common
include device/sony/msm8960-common/BoardConfigCommon.mk

TARGET_SPECIFIC_HEADER_PATH += device/sony/blue-common/include

# Kernel properties
TARGET_KERNEL_SOURCE := kernel/sony/msm8x60

# Platform
TARGET_BOOTLOADER_BOARD_NAME := MSM8960
BOARD_VENDOR_PLATFORM := blue

# Kernel information
BOARD_KERNEL_CMDLINE := # This is ignored by sony's bootloader
BOARD_KERNEL_BASE := 0x80200000
BOARD_RECOVERY_BASE := 0x80200000
BOARD_KERNEL_PAGESIZE := 2048
SONY_FORCE_RAMDISK_ADDRESS := 0x81900000
BOARD_MKBOOTIMG_ARGS := --ramdisk_offset 0x01700000

# Time
BOARD_USES_QC_TIME_SERVICES := true

# Dumpstate
BOARD_LIB_DUMPSTATE := libdumpstate.sony

# Include an expanded selection of fonts
EXTENDED_FONT_FOOTPRINT := true

# Wifi
BOARD_HAS_QCOM_WLAN              := true
BOARD_WLAN_DEVICE                := qcwcn
WPA_SUPPLICANT_VERSION           := VER_0_8_X
BOARD_WPA_SUPPLICANT_DRIVER      := NL80211
BOARD_WPA_SUPPLICANT_PRIVATE_LIB := lib_driver_cmd_$(BOARD_WLAN_DEVICE)
BOARD_HOSTAPD_DRIVER             := NL80211
BOARD_HOSTAPD_PRIVATE_LIB        := lib_driver_cmd_$(BOARD_WLAN_DEVICE)
WIFI_DRIVER_MODULE_PATH          := "/system/lib/modules/wlan.ko"
WIFI_DRIVER_MODULE_NAME          := "wlan"
WIFI_DRIVER_FW_PATH_STA          := "sta"
WIFI_DRIVER_FW_PATH_AP           := "ap"

BOARD_USE_SONY_MACUPDATE := true

# Camera
USE_DEVICE_SPECIFIC_CAMERA := true

# GPS
BOARD_VENDOR_QCOM_GPS_LOC_API_HARDWARE := $(TARGET_BOARD_PLATFORM)
TARGET_NO_RPC := true

# RIL
BOARD_PROVIDES_LIBRIL := true
BOARD_HAS_RIL_LEGACY_PAP := true
BOARD_USES_RIL_APPEND_RAT_TO_PLMN := true

# Needed for blobs
TARGET_RELEASE_CPPFLAGS += -DNEEDS_VECTORIMPL_SYMBOLS

# Vold
TARGET_USE_CUSTOM_LUN_FILE_PATH := /sys/devices/platform/msm_hsusb/gadget/lun%d/file

# Custom boot
TARGET_RECOVERY_PIXEL_FORMAT := "RGBX_8888"
BOARD_CUSTOM_BOOTIMG_MK := device/sony/blue-common/custombootimg.mk
TARGET_RELEASETOOLS_EXTENSIONS := device/sony/blue-common
BOARD_USE_CUSTOM_RECOVERY_FONT := \"roboto_15x24.h\"

TARGET_RECOVERY_FSTAB := device/sony/blue-common/rootdir/fstab.qcom

# Audio
BOARD_USES_LEGACY_ALSA_AUDIO := true
TARGET_USES_QCOM_COMPRESSED_AUDIO := true
BOARD_HAVE_NEW_QCOM_CSDCLIENT := true
QCOM_FM_ENABLED := true
AUDIO_FEATURE_ENABLED_FM := true

# Fix Adreno's INVAL
BOARD_USES_LEGACY_MMAP := true

# TWRP flags
DEVICE_RESOLUTION := 720x1280
RECOVERY_GRAPHICS_USE_LINELENGTH := true
TW_HAS_NO_RECOVERY_PARTITION := true
TW_NO_REBOOT_BOOTLOADER := true
TW_FLASH_FROM_STORAGE := true
TW_EXTERNAL_STORAGE_PATH := "/external_sd"
TW_EXTERNAL_STORAGE_MOUNT_POINT := "external_sd"
TW_DEFAULT_EXTERNAL_STORAGE := true
TW_INCLUDE_JB_CRYPTO := true
TW_INCLUDE_FUSE_EXFAT := true
TW_MAX_BRIGHTNESS := 255
TW_BRIGHTNESS_PATH := "/sys/class/leds/lcd-backlight_1/brightness"
TW_SECONDARY_BRIGHTNESS_PATH := "/sys/class/leds/lcd-backlight_2/brightness"

# Include common SE policies
-include device/qcom/sepolicy/sepolicy.mk

BOARD_SEPOLICY_DIRS += \
    device/sony/blue-common/sepolicy

BOARD_SEPOLICY_UNION += \
    file_contexts \
    property_contexts \
    bootanim.te \
    illumination.te \
    init.te \
    init_shell.te \
    mac_update.te \
    mediaserver.te \
    mpdecision.te \
    platform_app.te \
    property.te \
    rmt_storage.te \
    secchand.te \
	sensors.te \
	setup_fs.te \
    surfaceflinger.te \
    system_app.te \
    system_monitor.te \
    system_server.te \
    tad_static.te \
    ta_qmi_service.te \
    updatemiscta.te

# inherit from the proprietary version
-include vendor/sony/blue-common/BoardConfigVendor.mk
