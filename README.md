# PostnordAPI

[![PyPI version](https://img.shields.io/pypi/v/postnord_api?style=for-the-badge)](https://pypi.org/project/postnord_api/) [![License](https://img.shields.io/badge/license-WTFPL-green?style=for-the-badge)](https://github.com/dunderrrrrr/postnord_api/blob/main/LICENSE) [![Python versions](https://img.shields.io/pypi/pyversions/blocket-api?style=for-the-badge)](https://pypi.org/project/postnord_api/)


## ✨ Features

PostnordAPI allows you to query tracking information for shipments from [Postnord](https://postnord.se/), such as:

- Current status
- Events
- Delivery location
- Package size and weight
- Notification types

...and much more, without providing API key.


## 🧑‍💻️ Install

PostnordAPI is available on PyPI.

```sh
pip install postnord-api
```

## 💁‍♀️ Usage
```py
>>> from postnord_api import PostnordAPI
>>> response = PostnordAPI("123456789SE").get()
>>> print(response)
{
   "shipmentId":"123456789SE",
   [...]
   "items":[
      {
         "itemId":"123456789SE",
         "deliveryInformation":{
            "deliveryTo":"YOUR TOBAKSKIOSK",
            "deliveryToInfo":"Paketet kommer att levereras till servicestället där det kan hämtas upp. Vi meddelar dig när paketet är redo för upphämtning."
         },
         "events":[
            {
               "eventDescription":"Vi har fått en beställning på en leverans till dig. Spårningsinformationen uppdateras när försändelsen har ankommit till PostNord.",
               "eventTime":"2024-10-07T13:45:42.000Z",
               "status":"INFORMED",
               "location":{
                  "name":"PostNord"
               }
            },
            [...]
      }
   ]
}
```
## 📝 Notes

- Source repo: https://github.com/dunderrrrrr/postnord_api
- PyPI: https://pypi.org/project/postnord_api/
