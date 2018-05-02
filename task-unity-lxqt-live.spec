Name:		task-unity-lxqt-live
Version:	0.1.2
Release:	42%{?dist}
Summary:	Metapackage to build a Unity-Linux LXQt install
License:	GPL
URL:		http://lxqt.org/
Group:		Graphical desktop/Other
BuildArch:      noarch
Requires:	desktop-common-data
# components listed at http://wiki.lxde.org/en/Build_LXDE-Qt_From_Source
BuildRequires:	systemd-devel
Requires: 	task-lxqt-minimal
Requires: 	unity-theme
Requires: 	unity-theme-grub
Requires:       qlipper
Requires: 	lightdm
Requires: 	cpupower
Requires: 	volumeicon
Requires: 	xmessage
Requires: 	gpm
Requires: 	task-x11
Requires: 	dbus-x11
Requires: 	x11-driver-video
#Install wireless firmware task package
Requires:	task-wireless-firmware
Requires:	mandi
Requires: 	pulseaudio
#Needed for vbox package below
Requires:	dkms-minimal
#Requires:	vboxadditions-kernel-unity-desktop-latest
Requires:	dnfdragora-qt
Requires:	falkon
Requires:	os-prober
Requires:	acpid
Requires:	grub2
Requires:	grub2-common
Requires:	grub2-mageia-theme
Requires:	x11-driver-input-synaptics
Requires:	wpa_supplicant
%ifarch x86_64
Requires:	grub2-efi
%endif
Requires:	dosfstools

#Temp fix for Monitor Settings until requires is updated on lxqt-config package
Requires:	libkscreen

# We need Icons, but 32M worth?
Requires:	oxygen-icons5
Requires:	drakconf
Requires:	alsa-utils

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running LXQT, the Qt port of the upcoming version
of LXDE, the Lightweight Desktop Environment in a Live Environment.
This package assures that the minimal needed packages are installed
for a viable desktop environment.

%post
/usr/bin/systemctl set-default graphical.target
/usr/bin/systemctl enable xdm
if [ `grep -c ^live /etc/passwd` = "0" ]; then
/usr/sbin/useradd -c 'LiveCD User' -d /home/live -p 'Unity!' -s /bin/bash live
/usr/bin/passwd -d live
mkdir -p /home/live/.config/openbox/
cp /etc/xdg/openbox/lxqt-rc.xml /home/live/.config/openbox/lxqt-rc.xml

#For LightDM
sed -i 's!#autologin-user=!autologin-user=live!g' /etc/lightdm/lightdm.conf
sed -i 's!#autologin-session=!autologin-session=lxqt!g' /etc/lightdm/lightdm.conf
sed -i 's!#greeter-setup-script=!greeter-setup-script=/etc/X11/xdm/Xsetup_0!g' /etc/lightdm/lightdm.conf
chown -R live:live /home/live
echo "FINISH_INSTALL=yes" > /etc/sysconfig/finish-install
fi

%files

%changelog
* Wed May 03 2018 Jeremiah Summers <jsummers@glynlyon.com> 0.1.2-42
- Add temp fix for monitor config tool

* Mon Apr 30 2018 Jeremiah Summers <jsummers@glynlyon.com> 0.1.2-41
- Remove desktop icon
- Build as noarch

* Mon Apr 30 2018 Jeremiah Summers <jsummers@glynlyon.com> 0.1.2-40
- Move to own package and use Mageia task package by default

* Sat Apr 21 2018 Jeremiah Summers <jsummers@glynlyon.com> 0.1.2-39
- Update .travis.yml (jeremiah.summers@unity-linux.org)
- See if we can kick off finish-install
