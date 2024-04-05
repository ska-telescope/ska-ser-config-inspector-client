# Be generous, this is generated code
PYTHON_LINE_LENGTH := 140

## The following should be standard includes
# include core makefile targets for release management
-include .make/base.mk

#
# include makefile to pick up the standard Make targets, e.g., 'make build'
# build, 'make push' docker push procedure, etc. The other Make targets
# ('make interactive', 'make test', etc.) are defined in this file.
#
include .make/python.mk

BUILD_DIR := build
GENERATE_DIR := $(BUILD_DIR)/generated
SCHEMA_URL := https://gitlab.com/ska-telescope/ska-ser-config-inspector/-/raw/main/openapi.json
SCHEMA_FILE := $(BUILD_DIR)/ska-ser-config-inspector-openapi.json

generate:
	wget --quiet -O $(SCHEMA_FILE) $(SCHEMA_URL)
	docker run --rm \
	-v $(PWD):/local openapitools/openapi-generator-cli generate \
    -i /local/$(SCHEMA_FILE) \
    -g python \
    -o /local/$(GENERATE_DIR) \
	--additional-properties=packageName=ska_ser_config_inspector_client,\
	projectName=ska-ser-config-inspector-client,\
	packageVersion=$(VERSION)
	sudo chown -R $(USER) $(BUILD_DIR)
	rm -rf src tests docs
	mkdir -p src
	mv $(GENERATE_DIR)/ska_ser_config_inspector_client src/ska_ser_config_inspector_client
	mv $(GENERATE_DIR)/test tests
	mv $(GENERATE_DIR)/docs docs
	mv $(GENERATE_DIR)/README.md README.md 
.PHONY: generate
