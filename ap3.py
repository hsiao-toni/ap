
             
    {
      "c": "ht.Node",
      "i": 1694265,
      "p": {
        "name": "heat point",
        "displayName": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -391.74862,
          "y": -334.97719
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694266,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -391.74862,
          "y": -335.00634
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"1\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"1\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"1\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694267,
      "p": {
        "displayName": "1-2.4G",
        "tag": "a1",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -391.74862,
          "y": -417.19163
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694268,
      "p": {
        "displayName": "1-5G",
        "tag": "b1",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -391.74862,
          "y": -417.19163
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694269,
      "p": {
        "displayName": "1-Busy",
        "tag": "c1",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -391.74862,
          "y": -417.24993
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694270,
      "p": {
        "displayName": "1-Client",
        "tag": "d1",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -391.74862,
          "y": -417.24993
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694272,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -496.88378,
          "y": -334.97719
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694273,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -496.88378,
          "y": -334.94804
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"2\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"2\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"2\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694274,
      "p": {
        "displayName": "2-2.4G",
        "tag": "a2",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -488.68996,
          "y": -268.21514
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694275,
      "p": {
        "displayName": "2-5G",
        "tag": "b2",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -488.68996,
          "y": -268.21514
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694276,
      "p": {
        "displayName": "2-Busy",
        "tag": "c2",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -488.68996,
          "y": -268.27344
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694277,
      "p": {
        "displayName": "2-Client",
        "tag": "d2",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -488.68996,
          "y": -268.27344
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694279,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -598.08278,
          "y": -334.94804
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694280,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -598.08278,
          "y": -334.97719
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"3\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"3\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"3\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694281,
      "p": {
        "displayName": "3-2.4G",
        "tag": "a3",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -589.88896,
          "y": -417.13333
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694282,
      "p": {
        "displayName": "3-5G",
        "tag": "b3",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -589.88896,
          "y": -417.13333
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694283,
      "p": {
        "displayName": "3-Busy",
        "tag": "c3",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -589.88896,
          "y": -417.19163
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694284,
      "p": {
        "displayName": "3-Client",
        "tag": "d3",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -589.88896,
          "y": -417.19163
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694286,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -655.09103,
          "y": -140.02876
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694287,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -655.09103,
          "y": -140.02876
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"4\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"4\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"4\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694288,
      "p": {
        "displayName": "4-2.4G",
        "tag": "a4",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -768.44998,
          "y": -144.62981
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694289,
      "p": {
        "displayName": "4-5G",
        "tag": "b4",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -768.44998,
          "y": -144.62981
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694290,
      "p": {
        "displayName": "4-Busy",
        "tag": "c4",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -768.44998,
          "y": -144.68811
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694291,
      "p": {
        "displayName": "4-Client",
        "tag": "d4",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -768.44998,
          "y": -144.68811
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694293,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -655.09103,
          "y": -45.38214
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694294,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -655.09103,
          "y": -45.38214
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"5\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"5\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"5\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694295,
      "p": {
        "displayName": "5-2.4G",
        "tag": "a5",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -769.47627,
          "y": -45.35299
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694296,
      "p": {
        "displayName": "5-5G",
        "tag": "b5",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -769.47627,
          "y": -45.35299
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694297,
      "p": {
        "displayName": "5-Busy",
        "tag": "c5",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -769.47627,
          "y": -45.41129
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694298,
      "p": {
        "displayName": "5-Client",
        "tag": "d5",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -769.47627,
          "y": -45.41129
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694300,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -655.09103,
          "y": 57.58118
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694301,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -655.09103,
          "y": 57.58118
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"6\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"6\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"6\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694302,
      "p": {
        "displayName": "6-2.4G",
        "tag": "a6",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -769.47627,
          "y": 57.61034
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694303,
      "p": {
        "displayName": "6-5G",
        "tag": "b6",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -769.47627,
          "y": 57.61034
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694304,
      "p": {
        "displayName": "6-Busy",
        "tag": "c6",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -769.47627,
          "y": 57.55203
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694305,
      "p": {
        "displayName": "6-Client",
        "tag": "d6",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -769.47627,
          "y": 57.55203
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694307,
      "p": {
        "name": "heat point",
        "displayName": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -655.09103,
          "y": 167.23871
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694308,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -655.09103,
          "y": 167.23871
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"7\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"7\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"7\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694309,
      "p": {
        "displayName": "7-2.4G",
        "tag": "a7",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -769.47627,
          "y": 167.26787
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694310,
      "p": {
        "displayName": "7-5G",
        "tag": "b7",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -769.47627,
          "y": 167.26787
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694311,
      "p": {
        "displayName": "7-Busy",
        "tag": "c7",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -769.47627,
          "y": 167.20956
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694312,
      "p": {
        "displayName": "7-Client",
        "tag": "d7",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -769.47627,
          "y": 167.20956
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694314,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -655.09103,
          "y": 262.79427
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694315,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -655.09103,
          "y": 262.79427
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"8\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"8\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"8\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694316,
      "p": {
        "displayName": "8-2.4G",
        "tag": "a8",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -769.47627,
          "y": 262.82342
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694317,
      "p": {
        "displayName": "8-5G",
        "tag": "b8",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -769.47627,
          "y": 262.82342
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694318,
      "p": {
        "displayName": "8-Busy",
        "tag": "c8",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -769.47627,
          "y": 262.76512
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694319,
      "p": {
        "displayName": "8-Client",
        "tag": "d8",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -769.47627,
          "y": 262.76512
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694321,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -658.09103,
          "y": 357.59253
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694322,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -658.09103,
          "y": 357.59253
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"9\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"9\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"9\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694323,
      "p": {
        "displayName": "9-2.4G",
        "tag": "a9",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -772.47627,
          "y": 357.62168
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694324,
      "p": {
        "displayName": "9-5G",
        "tag": "b9",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -772.47627,
          "y": 357.62168
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694325,
      "p": {
        "displayName": "9-Busy",
        "tag": "c9",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -772.47627,
          "y": 357.56338
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694326,
      "p": {
        "displayName": "9-Client",
        "tag": "d9",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -772.47627,
          "y": 357.56338
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694328,
      "p": {
        "name": "heat point",
        "displayName": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -517.7582,
          "y": 357.59253
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694329,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -517.7582,
          "y": 357.59253
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"10\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"10\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"10\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694330,
      "p": {
        "displayName": "10-2.4G",
        "tag": "a10",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -391.74862,
          "y": 357.72238
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694331,
      "p": {
        "displayName": "10-5G",
        "tag": "b10",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -391.74862,
          "y": 357.72238
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694332,
      "p": {
        "displayName": "10-Busy",
        "tag": "c10",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -391.74862,
          "y": 357.66408
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694333,
      "p": {
        "displayName": "10-Client",
        "tag": "d10",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -391.74862,
          "y": 357.66408
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694335,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -517.7582,
          "y": 262.79427
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694336,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -517.7582,
          "y": 262.79427
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"11\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"11\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"11\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694337,
      "p": {
        "displayName": "11-2.4G",
        "tag": "a11",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -386.89606,
          "y": 262.76512
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694338,
      "p": {
        "displayName": "11-5G",
        "tag": "b11",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -386.89606,
          "y": 262.76512
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694339,
      "p": {
        "displayName": "11-Busy",
        "tag": "c11",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -386.89606,
          "y": 262.70682
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694340,
      "p": {
        "displayName": "11-Client",
        "tag": "d11",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -386.89606,
          "y": 262.70682
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694342,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -517.7582,
          "y": 167.23871
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694343,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -517.7582,
          "y": 167.23871
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"12\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"12\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"12\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694344,
      "p": {
        "displayName": "12-2.4G",
        "tag": "a12",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -383.5548,
          "y": 167.32618
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694345,
      "p": {
        "displayName": "12-5G",
        "tag": "b12",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -383.5548,
          "y": 167.32618
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694346,
      "p": {
        "displayName": "12-Busy",
        "tag": "c12",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -383.5548,
          "y": 167.26787
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694347,
      "p": {
        "displayName": "12-Client",
        "tag": "d12",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -383.5548,
          "y": 167.26787
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694349,
      "p": {
        "name": "heat point",
        "displayName": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 25.54152,
          "y": -328.19661
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694350,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 25.54152,
          "y": -328.19661
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"13\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"13\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"13\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694351,
      "p": {
        "displayName": "13-2.4G",
        "tag": "a13",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 33.73534,
          "y": -418.21714
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694352,
      "p": {
        "displayName": "13-5G",
        "tag": "b13",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 33.73534,
          "y": -418.21714
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694353,
      "p": {
        "displayName": "13-Busy",
        "tag": "c13",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 33.73534,
          "y": -418.27544
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694354,
      "p": {
        "displayName": "13-Client",
        "tag": "d13",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 25.54152,
          "y": -418.49232
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694356,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 131.0253,
          "y": -329.6076
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694357,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 131.0253,
          "y": -329.6076
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"14\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"14\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"14\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694358,
      "p": {
        "displayName": "14-2.4G",
        "tag": "a14",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 131.0253,
          "y": -266.8333
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694359,
      "p": {
        "displayName": "14-5G",
        "tag": "b14",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 131.0253,
          "y": -266.8333
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694360,
      "p": {
        "displayName": "14-Busy",
        "tag": "c14",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 131.0253,
          "y": -266.8916
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694361,
      "p": {
        "displayName": "14-Client",
        "tag": "d14",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 131.0253,
          "y": -266.8916
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694363,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 236.18608,
          "y": -331.55491
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694364,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 236.18608,
          "y": -331.55491
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"15\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"15\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"15\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694365,
      "p": {
        "displayName": "15-2.4G",
        "tag": "a15",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 236.18608,
          "y": -417.07503
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694366,
      "p": {
        "displayName": "15-5G",
        "tag": "b15",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 236.18608,
          "y": -417.07503
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694367,
      "p": {
        "displayName": "15-Busy",
        "tag": "c15",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 236.18608,
          "y": -417.13333
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694368,
      "p": {
        "displayName": "15-Client",
        "tag": "d15",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 236.18608,
          "y": -417.13333
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694370,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 337.35946,
          "y": -329.6076
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694371,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 337.35946,
          "y": -329.6076
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"16\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"16\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"16\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694372,
      "p": {
        "displayName": "16-2.4G",
        "tag": "a16",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 345.55328,
          "y": -266.77499
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694373,
      "p": {
        "displayName": "16-5G",
        "tag": "b16",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 345.55328,
          "y": -266.77499
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694374,
      "p": {
        "displayName": "16-Busy",
        "tag": "c16",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 345.55328,
          "y": -266.8333
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694375,
      "p": {
        "displayName": "16-Client",
        "tag": "d16",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 345.55328,
          "y": -266.8333
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694377,
      "p": {
        "name": "heat point",
        "displayName": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -558.38858,
          "y": 338.40642
        },
        "anchor": {
          "x": -7.62433,
          "y": 5.92631
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694378,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 438.02445,
          "y": -328.40406
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"17\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"17\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"17\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694379,
      "p": {
        "displayName": "17-2.4G",
        "tag": "a17",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 438.30254,
          "y": -417.01673
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694380,
      "p": {
        "displayName": "17-5G",
        "tag": "b17",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 438.30254,
          "y": -417.01673
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694381,
      "p": {
        "displayName": "17-Busy",
        "tag": "c17",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 438.30254,
          "y": -417.07503
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694382,
      "p": {
        "displayName": "17-Client",
        "tag": "d17",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 438.11715,
          "y": -417.07503
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694384,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 544.32737,
          "y": -330.07931
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694385,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 544.32737,
          "y": -330.07931
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"18\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"18\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"18\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694386,
      "p": {
        "displayName": "18-2.4G",
        "tag": "a18",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 544.32737,
          "y": -265.86609
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694387,
      "p": {
        "displayName": "18-5G",
        "tag": "b18",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 544.32737,
          "y": -265.86609
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694388,
      "p": {
        "displayName": "18-Busy",
        "tag": "c18",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 544.32737,
          "y": -265.92439
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694389,
      "p": {
        "displayName": "18-Client",
        "tag": "d18",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 544.32737,
          "y": -265.92439
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694391,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 24.08533,
          "y": -170.7722
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694392,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 24.08533,
          "y": -170.7722
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"19\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"19\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"19\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694393,
      "p": {
        "displayName": "19-2.4G",
        "tag": "a19",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 3.05337,
          "y": -81.93404
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694394,
      "p": {
        "displayName": "19-5G",
        "tag": "b19",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 3.05337,
          "y": -81.93404
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694395,
      "p": {
        "displayName": "19-Busy",
        "tag": "c19",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 3.05337,
          "y": -81.99233
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694396,
      "p": {
        "displayName": "19-Client",
        "tag": "d19",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 3.05337,
          "y": -81.99233
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694398,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 133.91551,
          "y": -170.7722
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694399,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 133.91551,
          "y": -170.7722
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"20\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"20\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"20\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694400,
      "p": {
        "displayName": "20-2.4G",
        "tag": "a20",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 154.94747,
          "y": -81.87574
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694401,
      "p": {
        "displayName": "20-5G",
        "tag": "b20",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 154.94747,
          "y": -81.87574
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694402,
      "p": {
        "displayName": "20-Busy",
        "tag": "c20",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 154.94747,
          "y": -81.93404
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694403,
      "p": {
        "displayName": "20-Client",
        "tag": "d20",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 154.94747,
          "y": -81.93404
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694405,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 469.91351,
          "y": 167.23871
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694406,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 469.91351,
          "y": 167.23871
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"21\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"21\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"21\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694407,
      "p": {
        "displayName": "21-2.4G",
        "tag": "a21",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 355.52827,
          "y": 167.26787
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694408,
      "p": {
        "displayName": "21-5G",
        "tag": "b21",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 355.52827,
          "y": 167.26787
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694409,
      "p": {
        "displayName": "21-Busy",
        "tag": "c21",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 355.52827,
          "y": 167.20957
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694410,
      "p": {
        "displayName": "21-Client",
        "tag": "d21",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 355.52827,
          "y": 167.20957
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694412,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 469.91351,
          "y": 262.79427
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694413,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 469.91351,
          "y": 262.79427
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"22\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"22\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"22\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694414,
      "p": {
        "displayName": "22-2.4G",
        "tag": "a22",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 355.52827,
          "y": 262.82342
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694415,
      "p": {
        "displayName": "22-5G",
        "tag": "b22",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 355.52827,
          "y": 262.82342
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694416,
      "p": {
        "displayName": "22-Busy",
        "tag": "c22",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 355.52827,
          "y": 262.76512
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694417,
      "p": {
        "displayName": "22-Client",
        "tag": "d22",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 355.52827,
          "y": 262.76512
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694419,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 469.91351,
          "y": 381.67786
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694420,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 469.91351,
          "y": 381.67786
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"23\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"23\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"23\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694421,
      "p": {
        "displayName": "23-2.4G",
        "tag": "a23",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 355.52827,
          "y": 381.70701
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694422,
      "p": {
        "displayName": "23-5G",
        "tag": "b23",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 355.52827,
          "y": 381.70701
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694423,
      "p": {
        "displayName": "23-Busy",
        "tag": "c23",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 355.52827,
          "y": 381.64871
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694424,
      "p": {
        "displayName": "23-Client",
        "tag": "d23",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 355.52827,
          "y": 381.64871
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694426,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 469.91351,
          "y": 468.58613
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694427,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 469.91351,
          "y": 468.58613
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"24\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"24\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"24\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694428,
      "p": {
        "displayName": "24-2.4G",
        "tag": "a24",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 355.52827,
          "y": 468.61528
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694429,
      "p": {
        "displayName": "24-5G",
        "tag": "b24",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 355.52827,
          "y": 468.61528
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694430,
      "p": {
        "displayName": "24-Busy",
        "tag": "c24",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 355.52827,
          "y": 468.55698
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694431,
      "p": {
        "displayName": "24-Client",
        "tag": "d24",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 355.52827,
          "y": 468.55698
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694433,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 469.91351,
          "y": 574.83969
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694434,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 469.91351,
          "y": 574.83969
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"25\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"25\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"25\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694435,
      "p": {
        "displayName": "25-2.4G",
        "tag": "a25",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 355.52827,
          "y": 574.86884
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694436,
      "p": {
        "displayName": "25-5G",
        "tag": "b25",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 355.52827,
          "y": 574.86884
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694437,
      "p": {
        "displayName": "25-Busy",
        "tag": "c25",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 355.52827,
          "y": 574.81054
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694438,
      "p": {
        "displayName": "25-Client",
        "tag": "d25",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 355.52827,
          "y": 574.81054
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694440,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 595.6295,
          "y": 574.83969
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694441,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 595.6295,
          "y": 574.83969
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"26\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"26\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"26\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694442,
      "p": {
        "displayName": "26-2.4G",
        "tag": "a26",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 716.05373,
          "y": 579.49903
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694443,
      "p": {
        "displayName": "26-5G",
        "tag": "b26",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 716.05373,
          "y": 579.49903
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694444,
      "p": {
        "displayName": "26-Busy",
        "tag": "c26",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 716.05373,
          "y": 579.44073
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694445,
      "p": {
        "displayName": "26-Client",
        "tag": "d26",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 716.05373,
          "y": 579.44073
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694447,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 595.6295,
          "y": 469.65941
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694448,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 595.6295,
          "y": 469.65941
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"27\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"27\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"27\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694449,
      "p": {
        "displayName": "27-2.4G",
        "tag": "a27",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 716.05373,
          "y": 465.05837
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694450,
      "p": {
        "displayName": "27-5G",
        "tag": "b27",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 716.05373,
          "y": 465.05837
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694451,
      "p": {
        "displayName": "27-Busy",
        "tag": "c27",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 716.05373,
          "y": 465.00007
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694452,
      "p": {
        "displayName": "27-Client",
        "tag": "d27",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 716.05373,
          "y": 465.00007
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694454,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 595.6295,
          "y": 381.67786
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694455,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 595.6295,
          "y": 381.67786
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"28\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"28\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"28\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694456,
      "p": {
        "displayName": "28-2.4G",
        "tag": "a28",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 710.10969,
          "y": 381.76531
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694457,
      "p": {
        "displayName": "28-5G",
        "tag": "b28",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 710.10969,
          "y": 381.76531
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694458,
      "p": {
        "displayName": "28-Busy",
        "tag": "c28",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 710.10969,
          "y": 381.70701
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694459,
      "p": {
        "displayName": "28-Client",
        "tag": "d28",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 710.10969,
          "y": 381.70701
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694461,
      "p": {
        "name": "heat point",
        "displayName": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 595.6295,
          "y": 262.82342
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694462,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 595.6295,
          "y": 262.79427
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"29\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"29\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"29\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694463,
      "p": {
        "displayName": "29-2.4G",
        "tag": "a29",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 716.05373,
          "y": 258.22238
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694464,
      "p": {
        "displayName": "29-5G",
        "tag": "b29",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 716.05373,
          "y": 258.22238
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694465,
      "p": {
        "displayName": "29-Busy",
        "tag": "c29",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 716.05373,
          "y": 258.16408
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694466,
      "p": {
        "displayName": "29-Client",
        "tag": "d29",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 716.05373,
          "y": 258.16408
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694468,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 595.6295,
          "y": 167.23871
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694469,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 595.6295,
          "y": 167.23871
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"30\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"30\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"30\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694470,
      "p": {
        "displayName": "30-2.4G",
        "tag": "a30",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 716.05373,
          "y": 167.26787
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694471,
      "p": {
        "displayName": "30-5G",
        "tag": "b30",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 716.05373,
          "y": 167.26787
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694472,
      "p": {
        "displayName": "30-Busy",
        "tag": "c30",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 716.05373,
          "y": 167.20956
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694473,
      "p": {
        "displayName": "30-Client",
        "tag": "d30",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 716.05373,
          "y": 167.20956
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694475,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 595.6295,
          "y": 64.23929
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694476,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 595.6295,
          "y": 64.23929
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"31\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"31\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"31\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694477,
      "p": {
        "displayName": "31-2.4G",
        "tag": "a31",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 716.05373,
          "y": 57.66864
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694478,
      "p": {
        "displayName": "31-5G",
        "tag": "b31",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 716.05373,
          "y": 57.66864
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694479,
      "p": {
        "displayName": "31-Busy",
        "tag": "c31",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 716.05373,
          "y": 57.61034
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694480,
      "p": {
        "displayName": "31-Client",
        "tag": "d31",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 716.05373,
          "y": 57.61034
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694482,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 595.6295,
          "y": -54.60927
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694483,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 595.6295,
          "y": -55.84994
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"32\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"32\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"32\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694484,
      "p": {
        "displayName": "32-2.4G",
        "tag": "a32",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 716.05373,
          "y": -49.94993
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694485,
      "p": {
        "displayName": "32-5G",
        "tag": "b32",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 716.05373,
          "y": -49.94993
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694486,
      "p": {
        "displayName": "32-Busy",
        "tag": "c32",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 716.05373,
          "y": -50.00823
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694487,
      "p": {
        "displayName": "32-Client",
        "tag": "d32",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 716.05373,
          "y": -50.00823
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694489,
      "p": {
        "name": "heat point",
        "displayName": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": 595.6295,
          "y": -146.68687
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694490,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": 595.6295,
          "y": -146.68687
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"33\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"33\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"33\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694491,
      "p": {
        "displayName": "33-2.4G",
        "tag": "a33",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": 716.05373,
          "y": -151.28791
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694492,
      "p": {
        "displayName": "33-5G",
        "tag": "b33",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": 716.05373,
          "y": -151.28791
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694493,
      "p": {
        "displayName": "33-Busy",
        "tag": "c33",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": 716.05373,
          "y": -151.34621
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694494,
      "p": {
        "displayName": "33-Client",
        "tag": "d33",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": 716.05373,
          "y": -151.34621
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694496,
      "p": {
        "name": "heat point",
        "displayName": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": true,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/builtIn/map/heat map.json",
        "position": {
          "x": -180.99922,
          "y": -365.72062
        },
        "width": 122.66832,
        "height": 122.66832
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      },
      "a": {
        "heatFloor": "floor",
        "heatValue": 85,
        "heatRadius": 80,
        "valueMax": 100,
        "heatmap.Gradient": {
          "1": "rgb(0,0,255)",
          "0.25": "rgb(0,255,0)",
          "0.55": "rgb(255,255,0)",
          "0.85": "rgb(255,0,0)"
        }
      }
    },
    {
      "c": "ht.Node",
      "i": 1694497,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/wifiap.json",
        "position": {
          "x": -180.99922,
          "y": -365.72062
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"34\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"34\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"34\").s(\"2d.visible\",false);\n }}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694498,
      "p": {
        "displayName": "34-2.4G",
        "tag": "a34",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/2.json",
        "position": {
          "x": -177.22064,
          "y": -292.91517
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694499,
      "p": {
        "displayName": "34-5G",
        "tag": "b34",
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/5.json",
        "position": {
          "x": -177.22064,
          "y": -292.91517
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "interactive": true,
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694500,
      "p": {
        "displayName": "34-Busy",
        "tag": "c34",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/busy.json",
        "position": {
          "x": -177.22064,
          "y": -292.97347
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694501,
      "p": {
        "displayName": "34-Client",
        "tag": "d34",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/client.json",
        "position": {
          "x": -177.22064,
          "y": -292.97347
        },
        "width": 139.05596,
        "height": 57.37274
      },
      "s": {
        "2d.visible": false,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694503,
      "p": {
        "displayName": "btn2.4G",
        "image": "symbols/btn2.4G.json",
        "position": {
          "x": 1258.14041,
          "y": -334.97719
        },
        "width": 230.28081,
        "height": 109.65753,
        "tall": 20
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"a1\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"a1\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a2\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a3\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a4\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a5\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a6\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a7\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a8\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a9\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a10\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a11\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a12\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a13\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a14\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a15\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a16\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a17\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a18\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a19\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a20\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a21\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a22\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a23\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a24\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a25\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a26\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a27\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a28\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a29\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a30\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a31\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a32\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a33\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a34\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"b34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d34\").s(\"2d.visible\",false);\n}\nelse {\n    dataModel.getDataByTag(\"a1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d34\").s(\"2d.visible\",false);\n\n}}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694504,
      "p": {
        "displayName": "btn5G ",
        "image": "symbols/btn5G .json",
        "position": {
          "x": 1258.14041,
          "y": -194.85753
        },
        "width": 230.28081,
        "height": 109.65753,
        "tall": 20
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"b1\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"a1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b1\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b2\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b3\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b4\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b5\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b6\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b7\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b8\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b9\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b10\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b11\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b12\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b13\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b14\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b15\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b16\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b17\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b18\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b19\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b20\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b21\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b22\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b23\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b24\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b25\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b26\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b27\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b28\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b29\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b30\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b31\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b32\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b33\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b34\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"c34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d34\").s(\"2d.visible\",false);\n}\nelse {\n    dataModel.getDataByTag(\"a1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d34\").s(\"2d.visible\",false);\n\n}}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694505,
      "p": {
        "displayName": "btnbusy",
        "image": "symbols/btnbusy.json",
        "position": {
          "x": 1258.14041,
          "y": -55.84994
        },
        "width": 230.28081,
        "height": 109.65753,
        "tall": 20
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"c1\").s(\"2d.visible\")){\n    dataModel.getDataByTag(\"a1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c1\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c2\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c3\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c4\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c5\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c6\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c7\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c8\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c9\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c10\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c11\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c12\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c13\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c14\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c15\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c16\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c17\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c18\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c19\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c20\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c21\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c22\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c23\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c24\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c25\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c26\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c27\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c28\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c29\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c30\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c31\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c32\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c33\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c34\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"d34\").s(\"2d.visible\",false);\n}\nelse {\n    dataModel.getDataByTag(\"a1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d34\").s(\"2d.visible\",false);\n\n}}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694506,
      "p": {
        "displayName": "btnclient",
        "image": "symbols/btnclient.json",
        "position": {
          "x": 1258.14041,
          "y": 88.32462
        },
        "width": 230.28081,
        "height": 109.65753,
        "tall": 20
      },
      "s": {
        "onClick": "__ht__function(event, data, view) {if (!dataModel.getDataByTag(\"d1\").s(\"2d.visible\")){\ndataModel.getDataByTag(\"a1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d1\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d2\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d3\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d4\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d5\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d6\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d7\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d8\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d9\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d10\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d11\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d12\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d13\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d14\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d15\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d16\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d17\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d18\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d19\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d20\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d21\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d22\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d23\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d24\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d25\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d26\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d27\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d28\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d29\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d30\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d31\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d32\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d33\").s(\"2d.visible\",true);\n    dataModel.getDataByTag(\"a34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d34\").s(\"2d.visible\",true);\n}\nelse {\n    dataModel.getDataByTag(\"a1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d1\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d2\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d3\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d4\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d5\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d6\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d7\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d8\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d9\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d10\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d11\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d12\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d13\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d14\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d15\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d16\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d17\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d18\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d19\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d20\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d21\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d22\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d23\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d24\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d25\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d26\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d27\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d28\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d29\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d30\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d31\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d32\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d33\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"a34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"b34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"c34\").s(\"2d.visible\",false);\n    dataModel.getDataByTag(\"d34\").s(\"2d.visible\",false);\n\n}}",
        "interactive": true,
        "2d.movable": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694271,
      "p": {
        "displayName": "1-APinf",
        "tag": "1",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP01#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP01",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -391.74862,
          "y": -487.94696
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694278,
      "p": {
        "displayName": "2-APinf",
        "tag": "2",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP02#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP02",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -496.88378,
          "y": -201.36292
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694285,
      "p": {
        "displayName": "3-APinf",
        "tag": "3",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP03#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP03",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -598.08278,
          "y": -487.94696
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694292,
      "p": {
        "displayName": "4-APinf",
        "tag": "4",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP04#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP04",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -829.9174,
          "y": -144.91129
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694299,
      "p": {
        "displayName": "5-APinf",
        "tag": "5",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP05#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP05",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -829.9174,
          "y": -32.81956
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694306,
      "p": {
        "displayName": "6-APinf",
        "tag": "6",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP06#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP06",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -829.9174,
          "y": 70.14376
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694313,
      "p": {
        "displayName": "7-APinf",
        "tag": "7",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP07#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP07",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -829.9174,
          "y": 179.80129
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694320,
      "p": {
        "displayName": "8-APinf",
        "tag": "8",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP08#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP08",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -829.9174,
          "y": 275.35685
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694327,
      "p": {
        "displayName": "9-APinf",
        "tag": "9",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP09#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP09",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -829.9174,
          "y": 362.32342
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694334,
      "p": {
        "displayName": "10-APinf",
        "tag": "10",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP10#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP10",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -316.2766,
          "y": 357.56338
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694341,
      "p": {
        "displayName": "11-APinf",
        "tag": "11",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP11#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP11",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -316.2766,
          "y": 262.76512
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694348,
      "p": {
        "displayName": "12-APinf",
        "tag": "12",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP12#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP12",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -316.2766,
          "y": 166.18044
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694355,
      "p": {
        "displayName": "13-APinf",
        "tag": "13",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP13#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP13",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 25.54152,
          "y": -487.94696
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694362,
      "p": {
        "displayName": "14-APinf",
        "tag": "14",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP14#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP14",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 131.0253,
          "y": -201.36292
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694369,
      "p": {
        "displayName": "15-APinf",
        "tag": "15",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP15#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP15",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 231.87568,
          "y": -487.88866
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694376,
      "p": {
        "displayName": "16-APinf",
        "tag": "16",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP16#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP16",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 337.35946,
          "y": -201.36292
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694383,
      "p": {
        "displayName": "17-APinf",
        "tag": "17",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP17#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP17",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 438.02445,
          "y": -489.03077
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694390,
      "p": {
        "displayName": "18-APinf",
        "tag": "18",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP18#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP18",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 543.69362,
          "y": -201.36292
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694397,
      "p": {
        "displayName": "19-APinf",
        "tag": "19",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP19#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP19",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 21.6581,
          "y": -9.93804
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694404,
      "p": {
        "displayName": "20-APinf",
        "tag": "20",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP20#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP20",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 131.0253,
          "y": -11.06211
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694411,
      "p": {
        "displayName": "21-APinf",
        "tag": "21",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP21#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP21",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 286.00029,
          "y": 175.85685
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694418,
      "p": {
        "displayName": "22-APinf",
        "tag": "22",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP22#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP22",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 286.00029,
          "y": 275.35685
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694425,
      "p": {
        "displayName": "23-APinf",
        "tag": "23",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP23#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP23",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 286.00029,
          "y": 386.40875
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694432,
      "p": {
        "displayName": "24-APinf",
        "tag": "24",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP24#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP24",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 286.00029,
          "y": 474.35685
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694439,
      "p": {
        "displayName": "25-APinf",
        "tag": "25",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP25#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP25",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 286.00029,
          "y": 585.40875
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694446,
      "p": {
        "displayName": "26-APinf",
        "tag": "26",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP26#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP26",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 785.58171,
          "y": 585.40875
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694453,
      "p": {
        "displayName": "27-APinf",
        "tag": "27",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP27#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP27",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 785.58171,
          "y": 485.90875
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694460,
      "p": {
        "displayName": "28-APinf",
        "tag": "28",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP28#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP28",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 785.58171,
          "y": 390.89319
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694467,
      "p": {
        "displayName": "29-APinf",
        "tag": "29",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP29#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP29",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 785.58171,
          "y": 269.14376
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694474,
      "p": {
        "displayName": "30-APinf",
        "tag": "30",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP30#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP30",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 785.58171,
          "y": 175.85685
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694481,
      "p": {
        "displayName": "31-APinf",
        "tag": "31",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP31#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP31",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 785.58171,
          "y": 70.14376
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694488,
      "p": {
        "displayName": "32-APinf",
        "tag": "32",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP32#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP32",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 785.58171,
          "y": -40.52876
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694495,
      "p": {
        "displayName": "33-APinf",
        "tag": "33",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP33#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP33",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": 785.58171,
          "y": -146.65772
        }
      },
      "s": {
        "2d.visible": false
      }
    },
    {
      "c": "ht.Node",
      "i": 1694502,
      "p": {
        "displayName": "34-APinf",
        "tag": "34",
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": false,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": true,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": true
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_3F_AP34#real",
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_3F_AP34",
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "position": {
          "x": -185.41446,
          "y": -222.15984
        }
      },
      "s": {
        "2d.visible": false
      }
    }
  ],
  "modified": "Thu Feb 16 2023 15:07:26 GMT+0800 (台北標準時間)",
  "contentRect": {
    "x": -1144.5,
    "y": -761.5,
    "width": 2517.78082,
    "height": 1523
  }
}