# http://lists.x.org/archives/xorg-devel/2009-February/000220.html
Summary:	X.org input driver for MagicTouch devices
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla urządzeń MagicTouch
Name:		xorg-driver-input-magictouch
Version:	1.0.0.5
Release:	4.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-magictouch-%{version}.tar.bz2
# Source0-md5:	d23f2791cd634ef85b7cc5e9da8f8407
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRequires:  rpmbuild(macros) >= 1.389
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for MagicTouch devices.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla urządzeń MagicTouch.

%prep
%setup -q -n xf86-input-magictouch-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/magictouch_drv.so
%{_mandir}/man4/magictouch.4*
