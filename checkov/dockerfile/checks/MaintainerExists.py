from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.dockerfile.base_dockerfile_check import BaseDockerfileCheck


class MaintainerExists(BaseDockerfileCheck):
    def __init__(self):
        name = "Ensure that LABEL maintainer is used instead of MAINTAINER (deprecated)"
        id = "CKV_DOCKER_6"
        supported_instructions = ["MAINTAINER"]
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories, supported_instructions=supported_instructions)

    def scan_entity_conf(self, conf):
        for instruction, content in conf.items():
            if instruction == "MAINTAINER":
                return CheckResult.FAILED, content[0]
        return CheckResult.PASSED, None


check = MaintainerExists()
