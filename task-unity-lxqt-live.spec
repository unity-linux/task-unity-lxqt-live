# Lightdm or xdm avail
%define login_dm lightdm
Name:		task-unity-lxqt-live
Version:	0.1.2
Release:	54%{?dist}
Summary:	Metapackage to build a Unity-Linux LXQt install
License:	GPL
URL:		http://lxqt.org/
Group:		Graphical desktop/Other
BuildArch:      noarch
Requires:	desktop-common-data
# components listed at http://wiki.lxde.org/en/Build_LXDE-Qt_From_Source
BuildRequires:	systemd-devel
Requires: 	task-lxqt-minimal
Requires: 	sudo
Requires: 	autologin
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
target_path=/etc/systemd/system/display-manager.service
link_path=/usr/lib/systemd/system/%{login_dm}.service
/usr/bin/systemctl set-default graphical.target
if [ ! "$link_path" = "$(readlink $target_path)" ]; then
   /usr/bin/systemctl enable %{login_dm}
fi
if [ ! -f /etc/sysconfig/desktop ]; then
   upper_dm=$(echo %{login_dm} | tr [:lower:] [:upper:])
   echo "DESKTOP=LXQtDesktop" > /etc/sysconfig/desktop
   echo "DISPLAYMANAGER=$upper_dm" >> /etc/sysconfig/desktop
fi
if [ "%{login_dm}" = "lightdm" ]; then
   echo "autologin-session=lxqt" >> /etc/lightdm/lightdm.conf.d/50-mageia-autologin.conf
fi
if grep '^builder:' /etc/passwd; then
/usr/sbin/userdel builder
fi
echo "#Reset Display manager for autologin" >> /etc/X11/xsetup.d/80-stop-matchbox.xsetup
echo "/usr/bin/systemctl restart display-manager" >> /etc/X11/xsetup.d/80-stop-matchbox.xsetup
cp -f /usr/share/mklivecd/finish-install /etc/sysconfig/finish-install
echo "LANGUAGE=no" >> /etc/sysconfig/finish-install

%files

%changelog
* Mon May 07 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-54
- Fix conditional for removing builduser

* Mon May 07 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-53
- Restart dm for user creation after finish install (autologin).

* Mon May 07 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-52
- Set autologin to lxqt if used.

* Fri May 04 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-51
- Set default to graphical

* Fri May 04 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-50
- Try to get autologin to work

* Fri May 04 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-49
- User tr properly

* Fri May 04 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-48
- Try and fix uppcase for post script

* Fri May 04 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-47
- Try and handle dm more intelligently

* Thu May 03 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-46
- Include sudo and autologin

* Thu May 03 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-45
- Disable language settings on finish-install

* Thu May 03 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-44
- Remove live user creation and allow finish install to create

* Thu May 03 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-43
- Try without autologin

* Wed May 02 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-42
- Add temp fix for monitor config tool

* Mon Apr 30 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-41
- Remove desktop icon
- Build as noarch

* Mon Apr 30 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-40
- Move to own package and use Mageia task package by default

* Sat Apr 21 2018 Jeremiah Summers <jmiahman@unity-linux.org> 0.1.2-39
- Update .travis.yml (jeremiah.summers@unity-linux.org)
- See if we can kick off finish-install
