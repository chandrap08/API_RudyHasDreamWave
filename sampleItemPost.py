import requests
import json

url = "https://prod-ua.deposco.com/integration/RBY/items/"

headers = {
    'authorization': "Basic YmVudGV4OmJlbnRleHRlc3Q=",
    'cache-control': "no-cache",
    'Content-Type': 'application/xml',
    'Accept-Encoding': "gzip,deflate",
    'Host': 'prod-ua.deposco.com',
    'Content-Length': '3200',
    'Accept-Encoding': 'gzip,deflate'
    }

data = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ns2:items xmlns:ns2="http://integration.deposco.com/item">
    <item>
        <businessUnit>BENTEX</businessUnit>
        <number>TestEliItem</number>
        <name>190071</name>
        <shortDescription>CAT Master UENG (EA)</shortDescription>
        <longDescription>CAT Master UENG (EA)</longDescription>
        <dimension>
            <length>0.0</length>
            <width>0.0</width>
            <height>0.0</height>
            <units>Inch</units>
        </dimension>
        <itemWeight>
            <weight>5.0</weight>
            <units>Pound</units>
        </itemWeight>
        <cycleCount>true</cycleCount>
        <purchaseCost>0.0</purchaseCost>
        <unitPrice>1.0</unitPrice>
        <bornOnDateRequired>false</bornOnDateRequired>
        <expirationDateRequired>true</expirationDateRequired>
        <receiveDateRequired>false</receiveDateRequired>
        <quarantineRequired>false</quarantineRequired>
        <inspectionRequired>false</inspectionRequired>
        <hazmat>false</hazmat>
        <hazmatCode/>
        <inventoryTrackingEnabled>true</inventoryTrackingEnabled>
        <lotTrackingEnabled>true</lotTrackingEnabled>
        <serialTrackingEnabled>false</serialTrackingEnabled>
        <shippable>true</shippable>
        <purchased/>
        <receiveOverTolerance/>
        <receiveUnderTolerance/>
        <cycleCountFrequency>0</cycleCountFrequency>
        <reorderQuantity>1920</reorderQuantity>
        <customFields/>
        <packs>
            <pack>
                <type>Each</type>
                <quantity>1</quantity>
                <weight>5.0</weight>
                <dimension>
                    <length>12.0</length>
                    <width>12.0</width>
                    <height>1.0</height>
                    <units>Inch</units>
                </dimension>
                <customMappings xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
            </pack>
        </packs>
        <upcs/>
        <productCategory>Miscellaneous</productCategory>
        <customMappings xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>
    </item>
</ns2:items>"""

response = requests.request("POST", url, headers=headers,data=data)
print(response)

