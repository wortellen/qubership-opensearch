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

import re

import semver

release_pattern = r'release-(\d{2}|\d{4})\.\d{1}-(.+)'


def parse_version(centos_version: str):
  releaseMatch = re.search(release_pattern, centos_version)
  if releaseMatch:
    return releaseMatch.group(2)
  elif "_" in centos_version:
    return centos_version[:centos_version.index("_")]
  elif "v" in centos_version:
    return centos_version[centos_version.index("v") + 1:]

  return centos_version


if __name__ == '__main__':

  promote_version = "release-2024.1-1.1.1"
  prev_version = "1.1.1"
  if prev_version != {} and semver.compare(parse_version(prev_version),
                                           parse_version(
                                               promote_version)) == -1:
    print("OK")
  else:
    print("Previous version is not set in snippet")
    exit(1)
