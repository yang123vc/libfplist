Name: libfplist
Version: 20161103
Release: 1
Summary: Library to support the plist formats
Group: System Environment/Libraries
License: LGPL
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libfplist/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
  
  

%description
libfplist is a library to support the plist formats

%package devel
Summary: Header files and libraries for developing applications for libfplist
Group: Development/Libraries
Requires: libfplist = %{version}-%{release}

%description devel
Header files and libraries for developing applications for libfplist.

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libfplist.pc
%{_includedir}/*
%{_mandir}/man3/*

%changelog
* Thu Nov  3 2016 Joachim Metz <joachim.metz@gmail.com> 20161103-1
- Auto-generated

