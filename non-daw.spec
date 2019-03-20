
%define	daw_version 1.2.0
%define sequencer_version 1.9.5

Summary:	Non DAW Studio – a digital audio workstation
Name:		non-daw
Version:	%{daw_version}
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://git.tuxfamily.org/non/non.git/snapshot/%{name}-v%{version}.tar.bz2
# Source0-md5:	30b539328ab1b4e698c93ef553c0c4da
URL:		http://non.tuxfamily.org/
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	liblo-devel >= 0.26
BuildRequires:	liblrdf >= 0.4.0
BuildRequires:	libsigc++ >= 2.0.0
BuildRequires:	libsndfile-devel >= 1.0.18
BuildRequires:	ntk-devel >= 1.3.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
Requires:	non-mixer = %{version}-%{release}
Requires:	non-sequencer = %{sequencer_version}-%{release}
Requires:	non-session-manager = %{version}-%{release}
Requires:	non-timeline = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Powerful enough to form a complete studio, fast and light enough to
run on low-end hardware like the eeePC or Raspberry Pi, and so
responsive and reliable that it can be used live, the Non DAW Studio
is a modular system composed of four main parts: Non Timeline, a
non-destructive, non-linear audio recorder and arranger. Non Mixer, a
live mixer with effects plugin hosting and advanced Ambisonics
spatialization control. Non Sequencer, a live, pattern based MIDI
sequencer, and finally, the Non Session Manager to tie together these
applications and more into cohesive song-level units.

Non is the result of one man's desire to build a complete
free-software Digital Audio Workstation on GNU/Linux that really
works--on accessible hardware.

%package -n non-mixer
Summary:	Non-Mixer - a powerful, reliable and fast modular Digital Audio Mixer
Version:	%{daw_version}
Group:		Applications

%description -n non-mixer
The Non Mixer is a powerful, reliable and fast modular Digital Audio
Mixer. It utilizes the JACK Audio Connection Kit for inter-application
audio I/O and the NTK GUI toolkit for a fast and lightweight user
interface.

Non Mixer can be used alone or in concert with Non Timeline and Non
Sequencer to form a complete studio.

%package -n non-timeline
Summary:	Non-Timeline - a powerful, reliable and fast modular Digital Audio Timeline arranger
Version:	%{daw_version}
Group:		Applications

%description -n non-timeline
The Non Timeline is a powerful, reliable and fast modular Digital
Audio Timeline arranger. It utilizes the JACK Audio Connection Kit for
inter-application audio I/O and the NTK GUI toolkit for a fast and
lightweight user interface.

Non Timeline can be used alone or in concert with Non Mixer and Non
Sequencer to form a complete studio.

%package -n non-sequencer
Summary:	Non-Sequencer - a powerful, lightweight, real-time, pattern-based MIDI sequencer
Version:	%{sequencer_version}
Group:		Applications

%description -n non-sequencer
The Non Sequencer is a powerful, lightweight, real-time, pattern-based
MIDI sequencer for Linux. It utilizes the JACK Audio Connection Kit
for MIDI I/O and the NTK GUI toolkit for its user interface.

Everything in Non Sequencer happens on-line, in realtime. Music can be
composed live, while the transport is rolling.

%package -n non-session-manager
Summary:	Session manager for Linux audio
Version:	%{daw_version}
Group:		Applications
URL:		http://non.tuxfamily.org/wiki/Non%20Session%20Manager

%description -n non-session-manager
The Non Session Manager is an API and an implementation for session
management in the context of Linux Audio. NSM clients use a
well-specified OSC protocol to communicate with the session management
daemon.

%prep
%setup -q -n %{name}-v%{version}

%build
CC="%{__cc}" \
CXX="%{__cxx}" \
CPP="%{__cpp}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LINKFLAGS="%{rpmldflags}" \
./waf configure \
	--prefix="%{_prefix}" \
	--libdir="%{_libdir}" \
	--destdir="$RPM_BUILD_ROOT"

./waf build -v

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT \
./waf install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/non-daw

%files -n non-mixer
%defattr(644,root,root,755)
%doc %{_docdir}/non-mixer
%attr(755,root,root) %{_bindir}/non-midi-mapper
%attr(755,root,root) %{_bindir}/non-mixer
%attr(755,root,root) %{_bindir}/non-mixer-noui
%{_desktopdir}/non-mixer.desktop
%{_iconsdir}/hicolor/*/apps/non-mixer.png
%{_pixmapsdir}/non-mixer

%files -n non-timeline
%defattr(644,root,root,755)
%doc %{_docdir}/non-timeline
%attr(755,root,root) %{_bindir}/non-timeline
%{_desktopdir}/non-timeline.desktop
%{_iconsdir}/hicolor/*/apps/non-timeline.png
%{_pixmapsdir}/non-timeline

%files -n non-sequencer
%defattr(644,root,root,755)
%doc %{_docdir}/non-sequencer
%attr(755,root,root) %{_bindir}/non-sequencer
%{_desktopdir}/non-sequencer.desktop
%{_iconsdir}/hicolor/*/apps/non-sequencer.png
%{_datadir}/non-sequencer
%{_pixmapsdir}/non-sequencer

%files -n non-session-manager
%defattr(644,root,root,755)
%doc %{_docdir}/non-session-manager
%attr(755,root,root) %{_bindir}/import-ardour-session
%attr(755,root,root) %{_bindir}/import-ardour-session_gui
%attr(755,root,root) %{_bindir}/jackpatch
%attr(755,root,root) %{_bindir}/nsmd
%attr(755,root,root) %{_bindir}/nsm-proxy
%attr(755,root,root) %{_bindir}/nsm-proxy-gui
%attr(755,root,root) %{_bindir}/non-session-manager
%{_desktopdir}/non-session-manager.desktop
%{_iconsdir}/hicolor/*/apps/non-session-manager.png
%{_pixmapsdir}/non-session-manager
