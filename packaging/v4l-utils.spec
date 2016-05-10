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
Release:        2
Summary:        Utilities for video4linux and DVB devices
License:        LGPL-2.1+
Group:          Multimedia/Utilities
Url:            http://linuxtv.org/downloads/v4l-utils/
Source0:        %{name}-%{version}.tar.bz2
Source99:       baselibs.conf
# Only needed to patch broken images in the upstream tarball
BuildRequires:  gettext-devel
BuildRequires:  kernel-headers
BuildRequires:  libjpeg-devel
BuildRequires:  sysfsutils
BuildRequires:  systemd-devel
Requires:       libv4l = %{version}-%{release}
Requires:       udev

%description
v4l-utils is a collection of various video4linux (V4L) and DVB utilities. The
main v4l-utils package contains cx18-ctl, ir-keytable, ivtv-ctl, v4l2-ctl and
v4l2-sysfs-path.

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

%package -n libv4l-devel
Summary:        Development files for libv4l
License:        LGPL-2.1+
Group:          Multimedia/Development
Requires:       libv4l = %{version}-%{release}

%description -n libv4l-devel
The libv4l-devel package contains libraries and header files for
developing applications that use libv4l.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%reconfigure --disable-v4l-utils --disable-qv4l2 --disable-libdvbv5
%__make %{?_smp_mflags}

%install
%make_install


%post -n libv4l -p /sbin/ldconfig

%postun -n libv4l -p /sbin/ldconfig

%files
%manifest %{name}.manifest
#%license COPYING
%license COPYING.libv4l
#%config(noreplace) %{_sysconfdir}/rc_maps.cfg
#%{_bindir}/cx18-ctl
#%{_bindir}/dvb-*
#%{_bindir}/dvbv5-*
#%{_bindir}/ir-keytable
#%{_bindir}/*-ctl
#%{_bindir}/v4l2-sysfs-path
%{_libdir}/v4l*.so
#%{_prefix}/lib/udev/rc_keymaps/*
#%{_prefix}/lib/udev/rules.d/70-infrared.rules
#%{_mandir}/man1/ir-keytable.1%{ext_man}

#%files devel-tools
#%license COPYING
#%{_bindir}/decode_tm6000
#%{_bindir}/v4l2-compliance
#%{_sbindir}/v4l2-dbg

%files -n libv4l
%manifest %{name}.manifest
%license COPYING.lib*
%{_libdir}/libv4l/
%{_libdir}/lib*.so.*

%files -n libv4l-devel
%license COPYING.lib*
%doc README.lib-multi-threading
%{_includedir}/libv4l*.h
#%{_includedir}/*/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
#%{_mandir}/*
