Name:           girl
Version:        12.0.1
Release:        2%{?dist}
Summary:        GNOME Internet Radio Locator program

# src/gnome-internet-radio-locator-markers.c: GNU General Public License v3.0 or later and/or GNU Lesser General Public License v2.1 or later
# src/gnome-internet-radio-locator-markers.h: GNU General Public License v3.0 or later and/or GNU Lesser General Public License v2.1 or later
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND (GPL-3.0-or-later OR LGPL-2.1-or-later)
URL:            https://github.com/GNOME/gnome-internet-radio-locator
Source0:        https://github.com/GNOME/gnome-internet-radio-locator/archive/refs/tags/%{version}/gnome-internet-radio-locator-%{version}.tar.gz

# These aren't real fixes (waiting upstream for this)
# Just a way to accommodate C code generators.
# See https://gcc.gnu.org/gcc-14/porting_to.html
Patch0:         %{name}-gcc14.patch

BuildRequires:  gtk2-devel
BuildRequires:  libgnome-devel
BuildRequires:  libxml2-devel
BuildRequires:  gnome-vfs2-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(libgeoclue-2.0)
Requires:       gstreamer1%{?_isa} >= 1.8.3
Requires:       gstreamer1-plugins-ugly%{?_isa} >= 1.8.3

%description
GNOME Internet Radio Locator is a Free Software program that allows
you to easily locate and listen to Free Internet Radio stations by
broadcasters on the Internet with the help of map and text search.

GNOME Internet Radio Locator is developed on the GNOME desktop
platform with GNOME Maps, libchamplain and geocode-lib and it
requires gstreamer 1.0 for audio playback.

Enjoy Free Internet Radio.

%prep
%autosetup -n gnome-internet-radio-locator-%{version} -p1

# In Fedora, "geocode-glib > 3.20" has an api version 2.0
sed -e 's|geocode-glib-1.0|geocode-glib-2.0|' -i configure.ac
autoreconf -ivf

%build
%configure --with-recording --disable-silent-rules
%make_build

%install
%make_install
%find_lang gnome-internet-radio-locator
%find_lang gnome-internet-radio-locator --with-man

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/gnome-internet-radio-locator.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/gnome-internet-radio-locator.desktop

%files -f gnome-internet-radio-locator.lang
%doc AUTHORS GEOLOCATION BROADCAST NEWS README
%license COPYING
%{_bindir}/gnome-internet-radio-locator
%{_datadir}/gnome-internet-radio-locator/
%{_metainfodir}/gnome-internet-radio-locator.appdata.xml
%{_datadir}/applications/gnome-internet-radio-locator.desktop
%{_datadir}/icons/hicolor/*/apps/gnome-internet-radio-locator.png
%{_mandir}/man1/gnome-internet-radio-locator.1*

%changelog
* Mon Mar 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 12.0.1-2
- no longer requires streamripper, so drop all references to it
- update description

* Sun Mar 10 2024 Antonio Trande <sagitter@fedoraproject.org> - 12.0.1-1
- Release 12.0.1

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 10.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 10.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 10.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 10.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 10.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 10.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 10.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 10.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 10.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 Leigh Scott <leigh123linux@gmail.com> - 10.0.0-7
- Rebuild for new gstreamer1 version
- Remove Group tag
- Remove scriptlets

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 10.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 10.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 10.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 10.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Martin Gansser <martinkg@fedoraproject.org> - 10.0.0-2
- Rebuild

* Wed Jul 05 2017 Martin Gansser <martinkg@fedoraproject.org> - 10.0.0-1
- Update to 10.0.0

* Sun Mar 26 2017 Martin Gansser <martinkg@fedoraproject.org> - 9.9.1-1
- Update to 9.9.1

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 9.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 9.7.0-1
- Update to 9.7.0
- Changed BR gstreamer-devel to gstreamer1-devel
- Add BR gstreamer1-plugins-bad-free-devel
- Add RR gstreamer1-plugins-ugly >= 1.8.3

* Sun Dec 11 2016 Martin Gansser <martinkg@fedoraproject.org> - 9.6.0-1
- Update to 9.6.0
- Remove dependency on totem
- Add BR gstreamer-devel
- Add Requires gstreamer1

* Fri Oct 07 2016 Martin Gansser <martinkg@fedoraproject.org> - 9.5.2-1
- Update to 9.5.2

* Fri Sep 09 2016 Martin Gansser <martinkg@fedoraproject.org> - 9.5.1-1
- Update to 9.5.1

* Sat Jul 09 2016 Martin Gansser <martinkg@fedoraproject.org> - 9.4.0-1
- Update to 9.4.0

* Thu Jun 09 2016 Martin Gansser <martinkg@fedoraproject.org> - 9.1.0-1
- Update to 9.1.0

* Wed Jan 06 2016 Martin Gansser <martinkg@fedoraproject.org> - 7.0.0-2
- Cleanup
- Rebuild

* Tue Jan 05 2016 Martin Gansser <martinkg@fedoraproject.org> - 7.0.0-1
- Update to 7.0.0
- Update URL

* Mon Nov 30 2015 Martin Gansser <martinkg@fedoraproject.org> - 6.1.0-1
- Update to 6.1.0

* Sun Jul 05 2015 Martin Gansser <martinkg@fedoraproject.org> - 6.0.0-3
- used %%setup -q in %%prep section
- used %%make_install macro in %%install section

* Sat Jul 04 2015 Martin Gansser <martinkg@fedoraproject.org> - 6.0.0-2
- removed %%dir in files section
- get source file with wget to save file size 

* Sat Jul 04 2015 Martin Gansser <martinkg@fedoraproject.org> - 6.0.0-1
- Update to 6.0.0

* Fri Jun 19 2015 Martin Gansser <martinkg@fedoraproject.org> - 5.0.0-1
- dropped release tag in %%changelog
- added BR itstool
- Update to 5.0.0

* Sat Mar 07 2015 Ole Aamot - 1.6.0-1
- Girl 1.6.0 build on Fedora Linux 21

* Sun Mar 01 2015 Ole Aamot - 1.5.1-1
- Cleanup spec file with help from Martin Gansser

* Sat Feb 28 2015 Ole Aamot - 1.5.0-1
- Girl 1.5.0 build on Fedora Linux 22

* Sat Feb 21 2015 Ole Aamot - 1.4.0-1
- Girl 1.4.0 build on Fedora Linux 22

* Sat Feb 14 2015 Ole Aamot - 1.3.0-1
- Girl 1.3.0 build on Fedora Linux 22

* Fri Jan 23 2015 Ole Aamot - 1.2.0-1
- Girl 1.2.0 build on Fedora Linux 22

* Sun Jan 18 2015 Ole Aamot - 1.1.1-1
- Girl 1.1.1 build on Fedora Linux 22

* Sat Jan 17 2015 Ole Aamot - 1.1.0-1
- Girl 1.1.0 build on Fedora Linux 21

* Thu Jan 01 2015 Ole Aamot - 1.0.0-1
- Girl 1.0.0 build on Fedora Linux 21

* Sat Dec 27 2014 Ole Aamot - 0.9.0-1
- Girl 0.9.0 build on Fedora Linux 21

* Sat Dec 20 2014 Ole Aamot - 0.8.0-1
- Girl 0.8.0 build on Fedora Linux 21

* Sun Dec 14 2014 Ole Aamot - 0.7.3-1
- Girl 0.7.3 build on Fedora Linux 21

* Sun Dec 14 2014 Ole Aamot - 0.7.2-1
- Girl 0.7.2 build on Fedora Linux 21

* Sat Dec 13 2014 Ole Aamot - 0.7.1-1
- Girl 0.7.1 build on Fedora Linux 21

* Fri Dec 12 2014 Ole Aamot - 0.7.0-1
- Girl 0.7.0 build on Fedora Linux 21

* Sun Dec 07 2014 Ole Aamot - 0.6.2-1
- Girl 0.6.2 build on Fedora Linux 21

* Sat Dec 06 2014 Ole Aamot - 0.6.1-1
- Girl 0.6.1 build on Fedora Linux 21

* Tue Dec 02 2014 Ole Aamot - 0.6.0-1
- Girl 0.6.0 build on Fedora Linux 21

* Sat Nov 29 2014 Ole Aamot - 0.5.2-1
- Girl 0.5.2 build on Fedora Linux 21

* Sat Nov 29 2014 Ole Aamot - 0.5.1-1
- Girl 0.5.1 build on Fedora Linux 21

* Sat Nov 29 2014 Ole Aamot - 0.5.0-1
- Girl 0.5.0 build on Fedora Linux 21

* Sat Nov 22 2014 Ole Aamot - 0.4.0-1
- Girl 0.4.0 build on Fedora Linux 20

* Sat Nov 15 2014 Ole Aamot - 0.3.0
- Modify description of Girl

* Sat Nov  8 2014 Ole Aamot - 0.2.0
- Add dependency on 'totem'.

* Sat Nov  1 2014 Ole Aamot - 0.1.0
- Initial Girl build on Fedora Core 20
