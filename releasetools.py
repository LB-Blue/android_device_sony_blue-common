# Copyright (C) 2012 The Android Open Source Project
# Copyright (C) 2012 The CyanogenMod Project
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

"""Custom OTA Package commands for blue"""

def FullOTA_InstallEnd(self):
  self.script.AppendExtra('ui_print("Setting metadata");')
  self.script.AppendExtra('set_metadata_recursive("/system", "uid", 0, "gid", 0, "dmode", 0755, "fmode", 0644, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata_recursive("/system/bin", "uid", 0, "gid", 2000, "dmode", 0755, "fmode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/app_process32", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:zygote_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/auditd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:logd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/bdAddrLoader", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:bluetooth_loader_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/bootanimation", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:bootanim_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/bridgemgrd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:bridge_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/cal_data_manager", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:sensors_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/clatd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:clatd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/cnd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:cnd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/debuggerd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:debuggerd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/dex2oat", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:dex2oat_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/dhcpcd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:dhcp_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/dnsmasq", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:dnsmasq_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/drmserver", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:drmserver_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/dumpstate", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:dumpstate_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/gpsone_daemon", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:location_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/gsiff_daemon", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:location_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/hostapd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:hostapd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/hostapd_cli", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:hostapd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/installd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:installd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/irsc_util", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:irsc_util_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/illumination_service", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:illumination_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/keystore", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:keystore_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/lmkd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:lmkd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/logd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:logd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/location-mq", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:location_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/lowi-server", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:location_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/mac-update", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:mac_update_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/mdnsd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:mdnsd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/mediaserver", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:mediaserver_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/mm-pp-daemon", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:mm-pp-daemon_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/mm-qcamera-daemon", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:camera_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/mpdecision", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:mpdecision_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/mtpd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:mtp_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/ndc", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:wpa_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/netcfg", "uid", 0, "gid", 3003, "mode", 02750, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/netd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:netd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/netmgrd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:netmgrd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/patchoat", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:dex2oat_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/ping", "uid", 0, "gid", 0, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/pppd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:ppp_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/qmuxd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:qmuxd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/qseecomd", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:tee_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/quipc_igsn", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:location_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/quipc_main", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:location_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/racoon", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:racoon_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/rild", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:rild_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/rmt_storage", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:rmt_storage_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/run-as", "uid", 0, "gid", 2000, "mode", 0750, "capabilities", 0xc0, "selabel", "u:object_r:runas_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/secchand", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:secchand_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/sdcard", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:sdcardd_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/sensors.qcom", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:sensors_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/setup_fs", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:setup_fs_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/servicemanager", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:servicemanager_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/sh", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:shell_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/subsystem_ramdump", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:ssr_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/surfaceflinger", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:surfaceflinger_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/sysinit", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:sysinit_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/system_monitor", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_monitor_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/ta_qmi_service", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:ta_qmi_service_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/tad_static", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:tad_static_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/thermal-engine-hh", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:thermald_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/time_daemon", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:time_daemon_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/uncrypt", "uid", 0, "gid", 0, "mode", 0750, "capabilities", 0x0, "selabel", "u:object_r:uncrypt_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/updatemiscta", "uid", 0, "gid", 0, "mode", 0750, "capabilities", 0x0, "selabel", "u:object_r:updatemiscta_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/vdc", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vdc_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/vold", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vold_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/wcnss_service", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:wcnss_service_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/wpa_cli", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:wpa_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/wpa_supplicant", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:wpa_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/xtwifi-client", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:location_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/bin/xtwifi-inet-agent", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:location_exec:s0");')
  self.script.AppendExtra('set_metadata("/system/etc/dhcpcd/dhcpcd-run-hooks", "uid", 1014, "gid", 2000, "mode", 0550, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata_recursive("/system/etc/ppp", "uid", 0, "gid", 0, "dmode", 0755, "fmode", 0555, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/recovery-from-boot.p", "uid", 0, "gid", 0, "mode", 0644, "capabilities", 0x0);')
  self.script.AppendExtra('set_metadata("/system/vendor", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata_recursive("/system/vendor/bin", "uid", 0, "gid", 2000, "dmode", 0755, "fmode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/vendor/bin/vss_init", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:vss_exec:s0");')
  self.script.AppendExtra('set_metadata_recursive("/system/vendor/etc", "uid", 0, "gid", 2000, "dmode", 0755, "fmode", 0644, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/vendor/etc/audio_effects.conf", "uid", 0, "gid", 0, "mode", 0644, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/vendor/firmware", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/vendor/firmware/discretix", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/vendor/firmware/keymaster", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/vendor/lib", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata_recursive("/system/vendor/lib/drm", "uid", 0, "gid", 2000, "dmode", 0755, "fmode", 0644, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/vendor/lib/drm/libdrmwvmplugin.so", "uid", 0, "gid", 0, "mode", 0644, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/vendor/lib/egl", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata_recursive("/system/vendor/lib/hw", "uid", 0, "gid", 2000, "dmode", 0755, "fmode", 0644, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/vendor/lib/hw/sensors.msm8960.so", "uid", 0, "gid", 0, "mode", 0644, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/vendor/lib/mediadrm", "uid", 0, "gid", 2000, "mode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata_recursive("/system/xbin", "uid", 0, "gid", 2000, "dmode", 0755, "fmode", 0755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/xbin/librank", "uid", 0, "gid", 0, "mode", 06755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/xbin/procmem", "uid", 0, "gid", 0, "mode", 06755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/xbin/procrank", "uid", 0, "gid", 0, "mode", 06755, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");')
  self.script.AppendExtra('set_metadata("/system/xbin/su", "uid", 0, "gid", 2000, "mode", 04750, "capabilities", 0x0, "selabel", "u:object_r:su_exec:s0");')
