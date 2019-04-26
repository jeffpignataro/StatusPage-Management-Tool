# Statuspage Management Tool

## How to setup the management tool

In order to execute these scripts you will need to [generate and API key](https://developer.statuspage.io/#section/Authentication/api_key) from Statuspage.io. Also, you'll need the Statuspage Page ID which can be found under the API tab within the "Manage Account" section of Statuspage. In addition, you may want to create a development Statuspage instance in order to test features without editing the live instance.

Once you have the API key, Page ID, and (optionally) Dev Page ID, you will need to create a file at `/config/environmentVariables.json`. This file should follow the format below.

Sample environment variables configuration file:
```json
{
	"apikey": "<insert key>",
	"devPageId": "<insert development page id>",
	"pageId": "<insert page id>"
}
```
