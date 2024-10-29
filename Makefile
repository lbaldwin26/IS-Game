default: client-install server-install

.PHONY: client-install
client-install:
	pip install -r client-requirements.txt

.PHONY: server-install
server-install:
	pip install -r server-requirements.txt


.PHONY: run-server
run-server:

.PHONY: run-client
run-client:

.PHONY: tests
tests:
