# SOAP request URL
# ncp_wsdl_url = "https://kustomseating.qt9app1.com/services/wsISOActions.asmx?WSDL"

# ncp_method_url = "https://kustomseating.qt9app1.com/services/wsISOActions"

# ncp_service_url = "https://kustomseating.qt9app1.com/services/wsISOActions.asmx"

# header = zeep.xsd.Element(
#     "Header",
#     zeep.xsd.ComplexType(
#         [
#             zeep.xsd.Element(
#                 "{http://www.w3.org/2005/08/addressing}Action", zeep.xsd.String()
#             ),
#             zeep.xsd.Element(
#                 "{http://www.w3.org/2005/08/addressing}To", zeep.xsd.String()
#             ),
#         ]
#     ),
# )
# # set the header value from header element
# header_value = header(Action=auth_method_url, To=auth_service_url)

# # initialize zeep client
# client = zeep.Client(wsdl=ncp_wsdl_url)

# # make the service call
# result = client.service.AuthenticateUser(
#     UserName="CPP",
#     Password="water6",
#     _soapheaders=[header_value]
# )
# print({result})
