import re
import config
import pytest
import unittest
import logging
import subprocess
import json
import ib_utils.ib_NIOS as ib_NIOS


class Tacacsplus_Server(unittest.TestCase):

        @pytest.mark.run(order=1)
        def test_1_Start_Discovery_Services(self):
                get_ref = ib_NIOS.wapi_request('GET', object_type="discovery:memberproperties")
                logging.info(get_ref)
                res = json.loads(get_ref)
                ref = json.loads(get_ref)[1]['_ref']
                print ref
                logging.info("Starting Discovery Services")
                data = {"enable_service":True}
                response = ib_NIOS.wapi_request('PUT', object_type=ref, fields=json.dumps(data))
                print response
                logging.info(response)
                read  = re.search(r'201',response)
                for read in  response:
                        assert True
                logging.info("Test Case 1 Execution Completed")
                logging.info("============================")

