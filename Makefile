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
