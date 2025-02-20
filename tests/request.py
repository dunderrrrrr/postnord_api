import respx
from httpx import Response
from postnord_api import PostnordAPI


@respx.mock
def test_params():
    route = respx.get(
        "https://api2.postnord.com/rest/shipment/v1/trackingweb/shipmentInformation"
    ).mock(return_value=Response(status_code=200, json={"data": "ok"}))

    response = PostnordAPI("123456789SE").get()

    [call] = route.calls
    params = str(call.request.url.params)

    assert params == "shipmentId=123456789SE&locale=sv&timeZone=Europe%2FStockholm"
    assert response == {"data": "ok"}
