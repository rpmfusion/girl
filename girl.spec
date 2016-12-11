Name:           girl
Version:        9.6.0
Release:        1%{?dist}
Summary:        GNOME Internet Radio Locator program
License:        GPLv2+
URL:            http://people.gnome.org/~ole/girl
Group:          Applications/Internet
Source:         http://people.gnome.org/~ole/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  gtk2-devel
BuildRequires:  libgnome-devel
BuildRequires:  libxml2-devel
BuildRequires:  gnome-vfs2-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  gstreamer-devel
Requires:       gstreamer1 >= 1.8.3
Requires:       streamripper >= 1.64.6

%description
GIRL is a GNOME Internet Radio Locator program that allows the user
to easily find and record live radio programs on radio broadcasters
on the Internet.

GIRL is developed on the GNOME platform and it requires at least
one audio player such as Totem to be installed for playback and
streamripper for recording.

Enjoy Internet Radio.

%prep
%setup -q

%build
%configure --with-recording --disable-silent-rules

%install
%make_install
%find_lang %{name} --with-man

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%doc AUTHORS LETTER NEWS README TODO VERSION YP-DIRS ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*
%{_datadir}/help/*/%{name}

%changelog
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
