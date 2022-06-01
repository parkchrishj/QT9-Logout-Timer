from SOAP_API import authentication
import zeep


class LoggedinUser:
    def __init__(self) -> None:
        # SOAP request URL
        auth_wsdl_url = "https://kustomseating.qt9app1.com/services/wsAuthenticate.asmx?WSDL"

        auth_method_url = "https://kustomseating.qt9app1.com/services/wsAuthenticate"

        auth_service_url = "https://kustomseating.qt9app1.com/services/wsAuthenticate.asmx"

        header = zeep.xsd.Element(
            "Header",
            zeep.xsd.ComplexType(
                [
                    zeep.xsd.Element(
                        "{http://www.w3.org/2005/08/addressing}Action", zeep.xsd.String()
                    ),
                    zeep.xsd.Element(
                        "{http://www.w3.org/2005/08/addressing}To", zeep.xsd.String()
                    ),
                ]
            ),
        )
        # set the header value from header element
        header_value = header(Action=auth_method_url, To=auth_service_url)

        # initialize zeep client
        client = zeep.Client(wsdl=auth_wsdl_url)

    def check_users(self, usernames):
        # make the service call
        for name in usernames:
            try:
                result = self.client.service.AuthenticateUser(
                    UserName=name,
                    _soapheaders=[self.header_value]
                )
                print({result})
            except:
                print("Not logged in")
