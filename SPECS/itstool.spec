Name:           itstool
Version:        2.0.6
Release:        2%{?dist}
Summary:        ITS-based XML translation tool

Group:          Development/Tools
License:        GPLv3+
URL:            http://itstool.org/
Source0:        http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  python3-libxml2
BuildRequires:  python3-devel
Requires:       python3-libxml2

%description
ITS Tool allows you to translate XML documents with PO files, using rules from
the W3C Internationalization Tag Set (ITS) to determine what to translate and
how to separate it into PO file messages.

%prep
%setup -q

%build
export PYTHON=%{__python3}
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING COPYING.GPL3 NEWS
%{_bindir}/itstool
%{_datadir}/itstool
%doc %{_mandir}/man1/itstool.1.gz

%changelog
* Fri Jun 05 2020 Sundeep Anand <suanand@redhat.com> - 2.0.6-2
- sync with Fedora package

* Tue May 19 2020 Sundeep Anand <suanand@redhat.com> - 2.0.6-1
- Update to 2.0.6 (rhbz#1836152)
- Remove fix-segfaults.patch, as it is a part of upstream now

* Sat May 09 2020 Sundeep Anand <suanand@redhat.com> - 2.0.4-3
- rebuild for s390x (rhbz#1800548)

* Mon Jul 16 2018 Charalampos Stratakis <cstratak@redhat.com> - 2.0.4-2
- Fix libxml2 related segfaults

* Sun Jul 08 2018 Charalampos Stratakis <cstratak@redhat.com> - 2.0.4-1
- Update to 2.0.4
- Change to python3

* Mon Feb 05 2018 Petr Viktorin <pviktori@redhat.com> - 2.0.2-8
- Be more explicit about Python build dependencies
  (Require python2-devel, tell autotools that PYTHON is python2)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Merlin Mathesius <mmathesi@redhat.com> - 2.0.2-5
- Add BuildRequires: python to fix FTBFS (BZ#1414545).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Kalev Lember <kalevlember@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Kalev Lember <kalevlember@gmail.com> 1.2.0-1
- Update to 1.2.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> 1.1.2-1
- Update to itstool 1.1.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Shaun McCance <shaunm@gnome.org> 1.1.1-1
- Update to itstool 1.1.1

* Sun Aug 07 2011 Rahul Sundaram <sundaram@fedoraproject.org> 1.1.0-2
- Add requires on libxml2-python since itstool uses it
- Drop redundant defattr
- Add NEWS to doc

* Mon Jun 27 2011 Shaun McCance <shaunm@gnome.org> 1.1.0-1
- Update to itstool 1.1.0

* Sun May 8 2011 Shaun McCance <shaunm@gnome.org> 1.0.1-1
- Initial packaging
