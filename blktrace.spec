#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : blktrace
Version  : 1.2.0
Release  : 18
URL      : http://brick.kernel.dk/snaps/blktrace-1.2.0.tar.gz
Source0  : http://brick.kernel.dk/snaps/blktrace-1.2.0.tar.gz
Summary  : Block IO tracer
Group    : Development/Tools
License  : GPL-2.0
Requires: blktrace-bin
Requires: blktrace-license
Requires: blktrace-man
BuildRequires : libaio-dev
Patch1: 0001-Makefile-fix-prefix-and-manpath.patch
Patch2: CVE-2018-10689.patch

%description
btrace can show detailed info about what is happening on a block
device io queue. This is valuable for diagnosing and fixing
performance or application problems relating to block layer io.


Authors:
--------
    Jens Axboe <axboe@kernel.dk>

%package bin
Summary: bin components for the blktrace package.
Group: Binaries
Requires: blktrace-license
Requires: blktrace-man

%description bin
bin components for the blktrace package.


%package license
Summary: license components for the blktrace package.
Group: Default

%description license
license components for the blktrace package.


%package man
Summary: man components for the blktrace package.
Group: Default

%description man
man components for the blktrace package.


%prep
%setup -q -n blktrace-1.2.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529024715
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
make CFLAGS="%{optflags}" all

%install
export SOURCE_DATE_EPOCH=1529024715
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/blktrace
cp COPYING %{buildroot}/usr/share/doc/blktrace/COPYING
cp iowatcher/COPYING %{buildroot}/usr/share/doc/blktrace/iowatcher_COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/blkiomon
/usr/bin/blkparse
/usr/bin/blkrawverify
/usr/bin/blktrace
/usr/bin/bno_plot.py
/usr/bin/btrace
/usr/bin/btrecord
/usr/bin/btreplay
/usr/bin/btt
/usr/bin/iowatcher
/usr/bin/verify_blkparse

%files license
%defattr(-,root,root,-)
/usr/share/doc/blktrace/COPYING
/usr/share/doc/blktrace/iowatcher_COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/blkparse.1
/usr/share/man/man1/blkrawverify.1
/usr/share/man/man1/bno_plot.1
/usr/share/man/man1/btt.1
/usr/share/man/man1/iowatcher.1
/usr/share/man/man1/verify_blkparse.1
/usr/share/man/man8/blkiomon.8
/usr/share/man/man8/blktrace.8
/usr/share/man/man8/btrace.8
/usr/share/man/man8/btrecord.8
/usr/share/man/man8/btreplay.8
