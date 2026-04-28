srpm:
	dnf install -y git
	$(eval VERSION := $(shell grep "Version:" *.spec | awk '{print $$2}'))
	git clone --depth=1 --branch master https://github.com/vani-tty1/extension-manager.git extension-manager-$(VERSION)
	tar -czf extension-manager-$(VERSION).tar.gz extension-manager-$(VERSION)/
	rm -rf extension-manager-$(VERSION)/
	rpmbuild -bs --define "_sourcedir ." --define "_srcrpmdir $(outdir)" *.spec