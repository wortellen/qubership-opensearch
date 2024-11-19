# Copyright 2024-2025 NetCracker Technology Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import jsonpath
from robot.api import logger

class JsonpathLibrary(object):

    def get_items_by_path(self, json_dict, json_path):
        logger.info(f"Json: {json_dict}, path: {json_path}")
        match_object = jsonpath.jsonpath(json_dict, json_path)
        return match_object[0]

