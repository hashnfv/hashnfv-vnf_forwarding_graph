# Copyright 2015 Futurewei. All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from neutron.common import constants as n_const


INGRESS_DIR = 'ingress'
EGRESS_DIR = 'egress'

STATUS_BUILDING = 'building'
STATUS_ACTIVE = 'active'
STATUS_ERROR = 'error'
STATUS_DELETING = 'deleting'


PORTFLOW_OPT_ADD = 'add-flows'
PROTFLOW_OPT_DELETE = 'delete-flows'
PROTFLOW_OPT_UPDATE = 'update-flows'


SRC_NODE = 'src_node'
DST_NODE = 'dst_node'
SF_NODE = 'sf_node'

RES_TYPE_GROUP = 'group'
RES_TYPE_NSP = 'nsp'

INSERTION_TYPE_L2 = 'l2'
INSERTION_TYPE_L3 = 'l3'
INSERTION_TYPE_BITW = 'bitw'
INSERTION_TYPE_TAP = 'tap'

MAX_HASH = 16

INSERTION_TYPE_DICT = {
    n_const.DEVICE_OWNER_ROUTER_HA_INTF: INSERTION_TYPE_L3,
    n_const.DEVICE_OWNER_ROUTER_INTF: INSERTION_TYPE_L3,
    n_const.DEVICE_OWNER_ROUTER_GW: INSERTION_TYPE_L3,
    n_const.DEVICE_OWNER_FLOATINGIP: INSERTION_TYPE_L3,
    n_const.DEVICE_OWNER_DHCP: INSERTION_TYPE_TAP,
    n_const.DEVICE_OWNER_DVR_INTERFACE: INSERTION_TYPE_L3,
    n_const.DEVICE_OWNER_AGENT_GW: INSERTION_TYPE_L3,
    n_const.DEVICE_OWNER_ROUTER_SNAT: INSERTION_TYPE_TAP,
    n_const.DEVICE_OWNER_LOADBALANCER: INSERTION_TYPE_TAP,
    'compute': INSERTION_TYPE_L2
}
