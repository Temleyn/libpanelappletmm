Summary:	C++ wrappers for libpanel-applet library
Summary(pl):	Interfejsy C++ dla biblioteki libpanel-applet
Name:		libpanelappletmm
Version:	2.5.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	04d859f1fa1b55fc17709c2c46d53d3d
URL:		http://www.gnome.org/
BuildRequires:	gconfmm-devel >= 2.5.0
BuildRequires:	gnome-panel-devel >= 2.5.0
BuildRequires:	gtkmm-devel >= 2.3.1
BuildRequires:	libgnomemm-devel >= 2.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libpanel-applet library.

%description -l pl
Interfejsy C++ dla biblioteki libpanel-applet.

%package devel
Summary:	Devel files for libpanelappletmm
Summary(pl):	Pliki nag��wkowe dla libpanelappletmm
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gconfmm-devel >= 2.5.0
Requires:	gnome-panel-devel >= 2.5.0
Requires:	gtkmm-devel >= 2.3.1

%description devel
Devel files for libpanelappletmm.

%description devel -l pl
Pliki nag��wkowe dla libpanelappletmm.

%package static
Summary:	libpanelappletmm static library
Summary(pl):	Biblioteka statyczna libpanelappletmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libpanelappletmm static library.

%description static -l pl
Biblioteka statyczna libpanelappletmm.

%prep
%setup -q

%build
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libpanelappletmm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpanelappletmm*.so
%{_libdir}/libpanelappletmm*.la
%{_libdir}/%{name}-2.0
%{_libdir}/%{name}-2.6
%{_includedir}/%{name}-2.*
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpanelappletmm*.a