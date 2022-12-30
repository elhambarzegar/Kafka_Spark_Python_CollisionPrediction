import avro
from avro.io import DatumReader

c_schema = """
{
  "connect.name": "com.github.jcustenborder.kafka.connect.model.Value",
  "fields": [
    {
      "default": null,
      "name": "X",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Y",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "INDEX_",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "ACCNUM",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "YEAR",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "DATE",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "TIME",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "HOUR",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "STREET1",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "STREET2",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "ROAD_CLASS",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "DISTRICT",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "WARDNUM",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "DIVISION",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "LATITUDE",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "LONGITUDE",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "LOCCOORD",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "ACCLOC",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "TRAFFCTL",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "VISIBILITY",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "LIGHT",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "RDSFCOND",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "ACCLASS",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "IMPACTYPE",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "INVTYPE",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "INVAGE",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "INJURY",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "FATAL_NO",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "INITDIR",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "VEHTYPE",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "MANOEUVER",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "DRIVACT",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "DRIVCOND",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "PEDTYPE",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "PEDACT",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "PEDCOND",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "CYCLISTYPE",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "CYCACT",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "CYCCOND",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "PEDESTRIAN",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "CYCLIST",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "AUTOMOBILE",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "MOTORCYCLE",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "TRUCK",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "TRSN_CITY_VEH",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "EMERG_VEH",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "PASSENGER",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "SPEEDING",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "AG_DRIV",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "REDLIGHT",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "ALCOHOL",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "DISABILITY",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "POLICE_DIVISION",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "HOOD_ID",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "NEIGHBOURHOOD",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "ObjectId",
      "type": [
        "null",
        "string"
      ]
    }
  ],
  "name": "Value",
  "namespace": "com.github.jcustenborder.kafka.connect.model",
  "type": "record"
}
"""

w_schema = """
{
  "connect.name": "com.github.jcustenborder.kafka.connect.model.Value",
  "fields": [
    {
      "default": null,
      "name": "Date",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Time",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Temp",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Weather",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Wind",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Humidity",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Visibility",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Barometer",
      "type": [
        "null",
        "string"
      ]
    }
  ],
  "name": "Value",
  "namespace": "com.github.jcustenborder.kafka.connect.model",
  "type": "record"
}"""

pd_schema = """
{
  "connect.name": "com.github.jcustenborder.kafka.connect.model.Value",
  "fields": [
    {
      "default": null,
      "name": "Date",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Time",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Temp",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Weather",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Wind",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Humidity",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Visibility",
      "type": [
        "null",
        "string"
      ]
    },
    {
      "default": null,
      "name": "Barometer",
      "type": [
        "null",
        "string"
      ]
    }
  ],
  "name": "Value",
  "namespace": "com.github.jcustenborder.kafka.connect.model",
  "type": "record"
}"""


collision_reader = DatumReader(avro.schema.parse(c_schema))
weather_reader = DatumReader(avro.schema.parse(w_schema))
