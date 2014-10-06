#
# packaging derived from openSUSE, with copyright statement below:
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           v4l-utils
Version:        1.6.0
Release:        0
Summary:        Utilities for video4linux and DVB devices
License:        GPL-2.0+ and GPL-2.0
Group:          Multimedia/Utilities
Url:            http://linuxtv.org/downloads/v4l-utils/
Source0:        %{name}-%{version}.tar.bz2
Source99:       baselibs.conf
# Only needed to patch broken images in the upstream tarball
BuildRequires:  kernel-headers
BuildRequires:  libjpeg-devel
BuildRequires:  sysfsutils
BuildRequires:  udev
BuildRequires:  gettext-devel
Requires:       libv4l = %{version}
Requires:       udev

%description
v4l-utils is a collection of various video4linux (V4L) and DVB utilities. The
main v4l-utils package contains cx18-ctl, ir-keytable, ivtv-ctl, v4l2-ctl and
v4l2-sysfs-path.

%package devel-tools
Summary:        Utilities for v4l2 / DVB driver development and debugging
License:        GPL-2.0+ and GPL-2.0
Group:          Multimedia/Utilities
Requires:       libv4l = %{version}

%description devel-tools
Utilities for v4l2 / DVB driver authors: decode_tm6000, v4l2-compliance and
v4l2-dbg.

%package -n libv4l
Summary:        Collection of video4linux support libraries
License:        LGPL-2.1+ and GPL-2.0
Group:          Multimedia/Libraries

%description -n libv4l
libv4l is a collection of libraries which adds a thin abstraction layer on
top of video4linux2 devices. The purpose of this (thin) layer is to make it
easy for application writers to support a wide variety of devices without
having to write separate code for different devices in the same class. libv4l
consists of 3 different libraries: libv4lconvert, libv4l1 and libv4l2.

%package -n     libdvbv5
Summary:        Libraries to control, scan and zap on Digital TV channels
Group:          Multimedia/Libraries
License:        GPL-2.0

%description -n libdvbv5
Libraries to control, scan and zap on Digital TV channels

%package -n libv4l-devel
Summary:        Development files for libv4l
License:        LGPL-2.1+
Group:          Multimedia/Development
Requires:       libv4l = %{version}

%description -n libv4l-devel
The libv4l-devel package contains libraries and header files for
developing applications that use libv4l.

%package -n     libdvbv5-devel
Summary:        Development files for libdvbv5
Group:          Multimedia/Development
License:        GPL-2.0
Requires:       libdvbv5%{?_isa} = %{version}-%{release}

%description -n libdvbv5-devel
The libdvbv5-devel package contains libraries and header
files for developing applications that use libdvbv5.

%prep
%setup -q
. ./bootstrap.sh

%build
%configure --disable-static --enable-libdvbv5
export CFLAGS="%{optflags} -fno-strict-aliasing"
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir}
#cp -arv utils/keytable/rc_keymaps %{buildroot}/%{_sysconfdir}/

%post -n libv4l -p /sbin/ldconfig

%postun -n libv4l -p /sbin/ldconfig

%files
%license COPYING
%dir %{_sysconfdir}/rc_keymaps
#%config(noreplace) %{_sysconfdir}/rc_keymaps/*
%config(noreplace) %{_sysconfdir}/rc_maps.cfg
%{_bindir}/cx18-ctl
%{_bindir}/dvb-*
%{_bindir}/dvbv5-*
%{_bindir}/ir-keytable
%{_bindir}/ivtv-ctl
%{_bindir}/v4l2-ctl
%{_bindir}/v4l2-sysfs-path
%{_bindir}/media-ctl
%{_bindir}/rds-ctl
%{_prefix}/lib/udev/rules.d/70-infrared.rules
%{_prefix}/lib/udev/rc_keymaps/*
%{_mandir}/man1/*.1%{ext_man}

%files devel-tools
%{_bindir}/decode_tm6000
%{_bindir}/v4l2-compliance
%{_sbindir}/v4l2-dbg

%files -n libv4l
%doc COPYING.libv4l
%{_libdir}/libv4l/
%{_libdir}/libv4l1.so.*
%{_libdir}/libv4l2.so.*
%{_libdir}/libv4lconvert.so.*
%{_libdir}/libv4l2rds.so.*
%{_libdir}/*.so
%{_libdir}/*.la

%files -n libv4l-devel
%doc README.lib-multi-threading
%{_includedir}/libv4l*.h
%{_libdir}/libv4l*.so
%{_libdir}/pkgconfig/*.pc

%files -n libdvbv5
%doc COPYING lib/libdvbv5/README
%{_libdir}/libdvbv5*.so.*

%files -n libdvbv5-devel
%doc COPYING lib/libdvbv5/README
%{_includedir}/libdvbv5/*.h
%{_libdir}/libdvbv5*.so
%{_libdir}/pkgconfig/libdvbv5*.pc
