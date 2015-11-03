LOCAL_PATH := $(call my-dir)

HIJACK_PATH := $(PRODUCT_OUT)/system/bin/hijack

INSTALLED_BOOTIMAGE_TARGET := $(PRODUCT_OUT)/boot.img
$(INSTALLED_BOOTIMAGE_TARGET): $(INSTALLED_RAMDISK_TARGET) $(PRODUCT_OUT)/utilities/busybox
	$(hide) $(MKBOOTIMG) $(INTERNAL_BOOTIMAGE_ARGS) $(BOARD_MKBOOTIMG_ARGS) --output $@
	$(hide) $(MKBOOTFS) $(TARGET_ROOT_OUT) > $(HIJACK_PATH)/ramdisk.cpio
	$(hide) cp $(PRODUCT_OUT)/utilities/busybox $(HIJACK_PATH)/

INSTALLED_RECOVERYIMAGE_TARGET := $(PRODUCT_OUT)/recovery.img
$(INSTALLED_RECOVERYIMAGE_TARGET): $(MKBOOTIMG) $(recovery_ramdisk) $(recovery_kernel)
	$(hide) $(MKBOOTIMG) $(INTERNAL_RECOVERYIMAGE_ARGS) $(BOARD_MKBOOTIMG_ARGS) --output $@
	$(hide) cp $(recovery_ramdisk) $(HIJACK_PATH)/
