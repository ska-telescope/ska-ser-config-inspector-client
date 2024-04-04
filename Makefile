# Chart for testing
# K8S_CHART = umbrella
# K8S_CHARTS = $(K8S_CHART)

## The following should be standard includes
# include core makefile targets for release management
-include .make/base.mk

#
# include makefile to pick up the standard Make targets, e.g., 'make build'
# build, 'make push' docker push procedure, etc. The other Make targets
# ('make interactive', 'make test', etc.) are defined in this file.
#
include .make/python.mk

GENERATE_DIR := build/generated

generate:
	docker run --rm \
	-v $(PWD):/local openapitools/openapi-generator-cli generate \
    -i /local/ska-ser-config-inspector-openapi.json \
    -g python \
    -o /local/$(GENERATE_DIR) \
	--additional-properties=packageName=ska_ser_config_inspector_client,\
	projectName=ska-ser-config-inspector-client,\
	packageVersion=$(VERSION)
	sudo chown -R $(USER) $(GENERATE_DIR)
	rm -rf src tests docs
	mkdir -p src
	mv $(GENERATE_DIR)/ska_ser_config_inspector_client src/ska_ser_config_inspector_client
	mv $(GENERATE_DIR)/test tests
	mv $(GENERATE_DIR)/docs docs
	mv $(GENERATE_DIR)/README.md README.md 
	mv $(GENERATE_DIR)/pyproject.toml pyproject.toml
.PHONY: generate