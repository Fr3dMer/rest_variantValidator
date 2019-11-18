import rest_VariantValidator
import VariantValidator
import VariantFormatter
from flask_restplus import Api
# from .hello import api as ns_hello
# from .name import api as ns_name
from .variantvalidator_endpoints import api as ns_vv
from .variantformatter_endpoints import api as ns_vf

# Obtain VariantValidator related metadata
vval = VariantValidator.Validator()
config_dict =  vval.my_config()


# Define the API as api
api = Api(version=rest_VariantValidator.__version__,
          title="rest_VariantValidator",
          description="## By continuing to use this service you agree to our terms and conditions of Use\n"
                      "- [Terms and Conditions](https://github.com/openvar/variantValidator/blob"
                      "/master/README.md)\n\n"
                      "## Powered by\n"
                      "- [VariantValidator](https://github.com/openvar/rest_variantValidator) version "
                      + VariantValidator.__version__ + "\n"
                      "- [VariantFormatter](https://github.com/openvar/variantFormatter) version "
                      + VariantFormatter.__version__ + "\n"
                      " - [vv_hgvs](https://github.com/openvar/vv_hgvs) version "
                      + config_dict['variantvalidator_hgvs_version'] + "\n"
                      " - [UTA](https://github.com/biocommons/uta) release "
                      + config_dict['uta_schema'] + "\n"
                      " - [SeqRepo](https://github.com/biocommons/biocommons.seqrepo) release "
                      + config_dict['seqrepo_db'].split('/')[-1]
          )

# api.add_namespace(ns_hello)
# api.add_namespace(ns_name)
api.add_namespace(ns_vv)
api.add_namespace(ns_vf)


# <LICENSE>
# Copyright (C) 2019 VariantValidator Contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# </LICENSE>
