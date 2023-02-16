import json

#for i in range (19):
 #   i=i+1

#for j in range (19):
  #  j=j+1
i=input("input:")  
for j in range (34) :
 template=[
    {
      "c": "ht.Node",
      "i": 121625,
      "p": {
        "name": "heat point",
        "dataBindings": {
          "a": {
            "heatValue": {
              "id": "1676433783496_0",
              "animatedOptions": {
                "advancedAnimate": True,
                "func": "__ht__function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    ",
                "details": {},
                "advFunc": "function (value, oldValue, option){ \n    \n    if (value>=70)\n    i=100;\n    else if (value<30)\n    i=40;\n    else\n    i=75;\n    return i; } \n    "
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_{}_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
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
        "2d.visible": False
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
      "i": 126856,
      "p": {
        "displayName": "wifiap",
        "dataBindings": {
          "a": {
            "name": {
              "id": "1676432427565_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
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
        "image": "symbols/wifiap.json",
        "position": {
          "x": -658.09103,
          "y": 357.59253
        },
        "width": 48.17066,
        "height": 48.17066
      },
      "s": {
         "onClick": f'__ht__function(event, data, view) {{if (!dataModel.getDataByTag("{j+1}").s("2d.visible")){{\n    dataModel.getDataByTag("{j+1}").s("2d.visible",true);\n}}\nelse {{\n    dataModel.getDataByTag("{j+1}").s("2d.visible",false);\n }}}}',

        "interactive": True
      }
    },
    {
      "c": "ht.Node",
      "i": 445378,
      "p": {
        "displayName": "{}-2.4G".format(j+1),
        "tag": "a{}".format(j+1),
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441375046_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676441420593_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
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
        "interactive": True,
        "2d.visible": False
      }
    },
    {
      "c": "ht.Node",
      "i": 445379,
      "p": {
        "displayName": "{}-5G".format(j+1),
        "tag": "b{}".format(j+1),
        "dataBindings": {
          "a": {
            "5channel": {
              "id": "1676441453617_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            },
            "ap_name": {
              "id": "1676441595251_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
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
        "interactive": True,
        "2d.visible": False
      }
    },
    {
      "c": "ht.Node",
      "i": 445380,
      "p": {
        "displayName": "{}-Busy".format(j+1),
        "tag": "c{}".format(j+1),
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441495832_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676441521210_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
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
        "2d.visible": False
      }
    },
    {
      "c": "ht.Node",
      "i": 445381,
      "p": {
        "displayName": "{}-Client".format(j+1),
        "tag": "d{}".format(j+1),
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676441562159_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            },
            "client": {
              "id": "1676441657954_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
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
        "2d.visible": False
      }
    },
    {
      "c": "ht.Node",
      "i": 445382,
      "p": {
        "displayName": "{}-APinf".format(j+1),
        "tag": "{}".format(j+1),
        "dataBindings": {
          "a": {
            "ap_name": {
              "id": "1676440472380_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#ap_name#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "ap_name",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            },
            "usage": {
              "id": "1676440639115_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#total_data_bytes#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "total_data_bytes",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            },
            "num": {
              "id": "1676440683854_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#sta_count#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "sta_count",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            },
            "2.4channel": {
              "id": "1676440720836_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_2-4G#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_2-4G",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            },
            "5channel": {
              "id": "1676440746927_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_5G#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_5G",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            },
            "busy": {
              "id": "1676440851590_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_busy#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_busy",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            },
            "eirp": {
              "id": "1676440882240_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#eirp_10x#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "eirp_10x",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            },
            "goodput": {
              "id": "1676440915489_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#goodput#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "goodput",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            },
            "intf": {
              "id": "1676440936959_0",
              "animatedOptions": {
                "advancedAnimate": False,
                "func": "__ht__function(value, oldValue, option){\nreturn value;\n}",
                "details": {
                  "directFeed": True,
                  "matchList": []
                },
                "animateCondition": "setMatch",
                "directFeed": True
              },
              "targets": [
                {
                  "sourceType": "IY building",
                  "formatType": "timeseries",
                  "scDataType": "value",
                  "target": "研華專案#2bb7dc7d-f31e-4a5d-92fc-cebe87683215#channel_interference#D1_{}F_AP{:02d}#real".format(i,j+1),
                  "project": "研華專案",
                  "node": "2bb7dc7d-f31e-4a5d-92fc-cebe87683215",
                  "device": "channel_interference",
                  "tag": "D1_{}F_AP{:02d}".format(i,j+1),
                  "dataType": "real"
                }
              ]
            }
          }
        },
        "image": "symbols/AP_inf.json",
        "host": {
          "__i":121626
        },
        "position": {
          "x": -832.9174,
          "y": 370.15511
        }
      },
      "s": {
        "2d.visible": False
      }
    }
 ]

 str1 = json.dumps(template[0],indent=4)+','+json.dumps(template[1],indent=4)+','+json.dumps(template[2],indent=4)+','+json.dumps(template[3],indent=4)+','+json.dumps(template[4],indent=4)+','+json.dumps(template[5],indent=4)+','+json.dumps(template[6],indent=4)
#print(len(template))
 print("\n")
 print(str1)
 str1=str1+','
 path="/Users/xiaotongling/Downloads/txt/data.txt"
 f=open(path,'a')
 f.write(str1)
 f.close()

# print(template)


print("ok")

